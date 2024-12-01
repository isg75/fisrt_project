#pages/completion.py
import streamlit as st
import pandas as pd  # Ensure pandas is imported
from data_loader import load_data

def show_completion_time(df):
    st.title("Completion Time Analysis")
    
    # Ensure the 'date_time' column is in datetime format
    if 'date_time' not in df.columns:
        st.error("Missing 'date_time' column in the dataset.")
        return
    
    # Coerce errors to NaT (Not a Time)
    df['date_time'] = pd.to_datetime(df['date_time'], errors='coerce')  

    # Drop rows where 'date_time' is NaT after coercion
    df = df.dropna(subset=['date_time'])

    # Sort the dataset to ensure chronological order by client_id, visit_id, and date_time
    df = df.sort_values(by=['client_id', 'visit_id', 'date_time'])
    
    # Split the data into control and test groups
    control_group = df[df['variation'] == 'Control']
    test_group = df[df['variation'] == 'Test']
    
    # Function to calculate completion time for each step considering multiple visits
    def calculate_completion_time_with_visits(group_df):
        group_df = group_df.sort_values(by=['client_id', 'visit_id', 'date_time'])
        group_df['next_step_time'] = group_df.groupby(['client_id', 'visit_id'])['date_time'].shift(-1)
        group_df = group_df.dropna(subset=['next_step_time'])
        group_df['completion_time'] = group_df['next_step_time'] - group_df['date_time']
        return group_df[['client_id', 'visit_id', 'process_step', 'date_time', 'next_step_time', 'completion_time']]

    # Function to filter out outliers using IQR
    def filter_outliers(group_df):
        # Convert completion_time to minutes for easier interpretation
        group_df['completion_time_minutes'] = group_df['completion_time'].dt.total_seconds() / 60
        
        # Calculate the IQR (Interquartile Range) for completion time
        Q1 = group_df['completion_time_minutes'].quantile(0.25)
        Q3 = group_df['completion_time_minutes'].quantile(0.75)
        IQR = Q3 - Q1

        # Define the upper and lower bounds for outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Filter out the outliers based on IQR
        filtered_data = group_df[
            (group_df['completion_time_minutes'] >= lower_bound) &
            (group_df['completion_time_minutes'] <= upper_bound)
        ]
        return filtered_data

    # Apply the function to both the control and test groups
    control_group_completion_times = calculate_completion_time_with_visits(control_group)
    test_group_completion_times = calculate_completion_time_with_visits(test_group)
    
    # Filter out outliers from both groups
    control_group_filtered = filter_outliers(control_group_completion_times)
    test_group_filtered = filter_outliers(test_group_completion_times)
    
    # Calculate the average completion time in minutes for each process step, after removing outliers
    avg_completion_time_control = control_group_filtered.groupby('process_step')['completion_time_minutes'].mean().reset_index()
    avg_completion_time_test = test_group_filtered.groupby('process_step')['completion_time_minutes'].mean().reset_index()
    
    # Display the results for control and test group average completion times
    st.subheader("Average Completion Time for Control Group (Minutes) - After Outlier Removal")
    st.dataframe(avg_completion_time_control)

    st.subheader("Average Completion Time for Test Group (Minutes) - After Outlier Removal")
    st.dataframe(avg_completion_time_test)
    
    # Display comparison of control vs test group average completion times
    st.subheader("Comparison of Average Completion Time by Process Step")
    comparison_df = pd.merge(avg_completion_time_control, avg_completion_time_test, on='process_step', suffixes=('_control', '_test'))
    st.dataframe(comparison_df)

    # Optional: You could plot the results for better visualization if desired
    # st.bar_chart(comparison_df.set_index('process_step')[['completion_time_minutes_control', 'completion_time_minutes_test']])

    # Additional insights and interpretation
    st.subheader("Insights & Interpretation")
    st.write("""
    In this section, we can derive insights based on the completion time across different groups and process steps:
    
    - **Completion Time Analysis**: Are there significant differences in the time it takes for each process step between the Control and Test groups?
    - **Outlier Removal**: By removing outliers using the IQR method, we can focus on more representative data for process completion times.
    - **Improvement in Test Group**: Does the Test group show faster completion times compared to the Control group after considering the removal of outliers?
    
    Please review the data and interpret the results to drive business decisions and process improvements.
    """)

    # **Process Duration Analysis**: Calculate process duration for start and confirm steps
    st.subheader("Process Duration Analysis")

    # Filter to get the latest start for each client
    starts_only = df[df['process_step'] == 'start']
    latest_starts = starts_only.loc[starts_only.groupby('client_id')['date_time'].idxmax()]

    # Filter to get the last confirmation for each client
    confirmation_only = df[df['process_step'] == 'confirm']
    latest_confirms = confirmation_only.loc[confirmation_only.groupby('client_id')['date_time'].idxmax()]

    # Merge to have both latest start and confirm per client
    latest_start_confirms = pd.merge(latest_starts, latest_confirms, on='client_id', suffixes=('_start', '_confirm'))

    # Calculate process duration for those who completed the process
    latest_start_confirms['process_duration'] = latest_start_confirms['date_time_confirm'] - latest_start_confirms['date_time_start']

    # Convert timedelta to seconds for easier manipulation
    latest_start_confirms['process_duration_seconds'] = latest_start_confirms['process_duration'].dt.total_seconds()

    # Calculate the IQR (Interquartile Range) for process duration
    Q1_duration = latest_start_confirms['process_duration_seconds'].quantile(0.25)
    Q3_duration = latest_start_confirms['process_duration_seconds'].quantile(0.75)
    IQR_duration = Q3_duration - Q1_duration

    # Define the upper and lower bounds for outliers in process duration
    lower_bound_duration = Q1_duration - 1.5 * IQR_duration
    upper_bound_duration = Q3_duration + 1.5 * IQR_duration

    # Filter out the outliers based on IQR for process duration
    filtered_duration_data = latest_start_confirms[
        (latest_start_confirms['process_duration_seconds'] >= lower_bound_duration) &
        (latest_start_confirms['process_duration_seconds'] <= upper_bound_duration)
    ]

    # Convert process_duration back to Timedelta
    filtered_duration_data['process_duration'] = pd.to_timedelta(filtered_duration_data['process_duration_seconds'], unit='s')

    # Calculate the average process duration again after removing outliers
    st.subheader("Average Process Duration (Filtered) - After Outlier Removal")
    st.write(f"Average process duration: {filtered_duration_data['process_duration'].mean()}")
    st.write(f"Median process duration: {filtered_duration_data['process_duration'].median()}")
    
    # Optional: Display filtered duration data
    st.subheader("Filtered Process Duration Data (Outliers Removed)")
    st.dataframe(filtered_duration_data[['client_id', 'process_duration']])