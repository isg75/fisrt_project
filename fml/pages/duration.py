#pages/duration.py
import streamlit as st
import pandas as pd  # Ensure pandas is imported
from data_loader import load_data

def show_process_duration(df):
    st.title("Process Duration Analysis")
    
    # Check if the necessary columns exist
    if 'process_step' not in df.columns or 'date_time' not in df.columns or 'client_id' not in df.columns:
        st.error("Missing required columns: 'process_step', 'date_time', or 'client_id'.")
        return
    
    # Define the custom sorting order for the process steps
    process_step_order = ['start', 'step_1', 'step_2', 'step_3', 'confirm']
    df['process_step'] = pd.Categorical(df['process_step'], categories=process_step_order, ordered=True)

    # Filter groups based on test/control
    control_group = df[df['variation'] == 'Control']
    test_group = df[df['variation'] == 'Test']

    # Sort control group and test group
    control_group_sorted = control_group.sort_values(by=['client_id', 'visit_id', 'process_step', 'date_time'])
    test_group_sorted = test_group.sort_values(by=['client_id', 'visit_id', 'process_step', 'date_time'])

    # Function to get the latest starts
    def filter_latest_starts(group_df):
        starts_only = group_df[group_df['process_step'] == 'start']
        latest_starts = starts_only.loc[starts_only.groupby('visit_id')['date_time'].idxmax()]
        return group_df.merge(latest_starts[['visit_id', 'date_time']], on=['visit_id', 'date_time'], how='inner')

    # Apply to both groups (Control and Test)
    filtered_control = filter_latest_starts(control_group_sorted)
    filtered_test = filter_latest_starts(test_group_sorted)

    # Display the complete tables for the filtered groups
    st.title("Control Group Sorted and Filtered")
    st.dataframe(filtered_control)

    st.title("Test Group Sorted and Filtered")
    st.dataframe(filtered_test)

    # Check if it works for a specific client (e.g., client_id == 2304905)
    client_total_entries = df[df["client_id"] == 2304905]
    client_last_start_control = filtered_control[filtered_control['client_id'] == 2304905]
    client_last_start_test = filtered_test[filtered_test['client_id'] == 2304905]

    # Display the results for the specific client
    st.title("Total Entries for Client 2304905")
    st.dataframe(client_total_entries)

    st.title("Last Start for Client 2304905 in Control Group")
    st.dataframe(client_last_start_control)

    st.title("Last Start for Client 2304905 in Test Group")
    st.dataframe(client_last_start_test)