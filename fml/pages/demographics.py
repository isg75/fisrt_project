# pages/demographics.py
import pandas as pd
import plotly.express as px
import streamlit as st
from data_loader import load_data

# Function to perform demographic analysis
def analyze_demographics(df, control_group_sorted, test_group_sorted):
    """
    Function to perform demographic analysis and generate interactive plots using Plotly.
    """
    # Ensure 'clnt_age' is present and numeric
    if 'clnt_age' not in df.columns:
        st.error("The DataFrame does not contain the 'clnt_age' column.")
        return

    if not pd.api.types.is_numeric_dtype(df['clnt_age']):
        st.error("The 'clnt_age' column is not numeric.")
        return

    # Create the 'age_group' column based on 'clnt_age' ranges
    bins = [0, 18, 30, 40, 50, 60, 100]  # Define the age group ranges
    labels = ['0-18', '19-30', '31-40', '41-50', '51-60', '60+']  # Age group labels
    df['age_group'] = pd.cut(df['clnt_age'], bins=bins, labels=labels, right=False)

    # Debugging: Show first few rows of the dataframe to confirm 'age_group' column
    st.write("First few rows of the dataframe with 'age_group':")
    st.write(df[['clnt_age', 'age_group']].head())

    # Check if 'age_group' column exists now
    if 'age_group' not in df.columns:
        st.error("The 'age_group' column was not created.")
        return

    # Aggregating based on 'gender' and 'age_group'
    logs_calls_accounts = df.groupby(['gender', 'age_group']).agg({
        'num_accts': 'mean',
        'calls_6_mnth': 'mean',
        'logons_6_mnth': 'mean'
    }).reset_index().round(2)

    # Debugging: Show the aggregated result
    st.write("Aggregated data (grouped by 'gender' and 'age_group'):")
    st.write(logs_calls_accounts)

    # Plot for Average Number of Accounts
    fig1 = px.line(
        logs_calls_accounts, 
        x='age_group', 
        y='num_accts', 
        color='gender',
        title="Average Number of Accounts by Age Group and Gender",
        labels={'num_accts': 'Average Number of Accounts'},
        markers=True
    )
    st.plotly_chart(fig1)

    # Plot for Calls in the Last 6 Months
    fig2 = px.line(
        logs_calls_accounts, 
        x='age_group', 
        y='calls_6_mnth', 
        color='gender',
        title="Average Calls in Last 6 Months by Age Group and Gender",
        labels={'calls_6_mnth': 'Average Calls in Last 6 Months'},
        line_shape='linear',
        markers=True
    )
    st.plotly_chart(fig2)

    # Plot for Logons in the Last 6 Months
    fig3 = px.line(
        logs_calls_accounts, 
        x='age_group', 
        y='logons_6_mnth', 
        color='gender',
        title="Average Logons in Last 6 Months by Age Group and Gender",
        labels={'logons_6_mnth': 'Average Logons in Last 6 Months'},
        line_shape='linear',
        markers=True
    )
    st.plotly_chart(fig3)

    # *** Age Group by Test & Control ***
    st.write("### Test & Control Grouped by Age Group")
    # Filter based on unique client_id in control and test groups
    control_unique = control_group_sorted.drop_duplicates(subset='client_id')
    test_unique = test_group_sorted.drop_duplicates(subset='client_id')

    # Calculate age group distribution for each group
    control_age_group = control_unique["age_group"].value_counts()
    test_age_group = test_unique["age_group"].value_counts()

    # Combine data into one table
    age_groups_concat = pd.concat(
        [control_age_group, test_age_group], 
        axis=1, 
        keys=["Control Group Count", "Test Group Count"]
    )

    # Rename the columns for clarity
    age_groups_concat = age_groups_concat.sort_values(by="age_group", ascending=True)  # sort values
    age_groups_concat = age_groups_concat.reset_index()

    st.write(age_groups_concat)

    # *** Age Group x Gender ***
    st.write("### Age Group x Gender")
    control_age_group_gender = control_unique.groupby("age_group")["gender"].value_counts().unstack()
    test_age_group_gender = test_unique.groupby("age_group")["gender"].value_counts().unstack()

    # Reset the index to create a proper DataFrame structure
    control_age_group_gender = control_age_group_gender.reset_index()
    test_age_group_gender = test_age_group_gender.reset_index()

    st.write("Control Group - Age Group x Gender:")
    st.write(control_age_group_gender)

    st.write("Test Group - Age Group x Gender:")
    st.write(test_age_group_gender)

    # *** Age Group x Balances ***
    st.write("### Age Group x Balances")
    # Filter control and test group based on unique client_id
    control_age_group_balance = control_unique.groupby("age_group")["balance"].mean().round(2)
    test_age_group_balance = test_unique.groupby("age_group")["balance"].mean().round(2)

    # Convert the grouped Series to DataFrames
    control_age_group_balance_df = control_age_group_balance.reset_index()
    test_age_group_balance_df = test_age_group_balance.reset_index()

    # Rename the columns for clarity
    control_age_group_balance_df.rename(columns={"age_group": "Age Group", "balance": "Control Group Balance"}, inplace=True)
    test_age_group_balance_df.rename(columns={"age_group": "Age Group", "balance": "Test Group Balance"}, inplace=True)

    # Merge both control and test balance data into a single table
    balance_concat = pd.merge(control_age_group_balance_df, test_age_group_balance_df, on="Age Group")

    st.write(balance_concat)

# Function to display the demographics analysis in Streamlit
def show_demographics(df, control_group_sorted, test_group_sorted):
    """
    Show Demographics Analysis in the Streamlit app.
    This function is used to call the analysis and display the results.
    """
    st.title("Demographics Analysis")

    # Perform the demographic analysis (aggregation and plotting)
    analyze_demographics(df, control_group_sorted, test_group_sorted)

    # Additional notes or user guidance
    st.write("""
        This page provides demographic analysis, including average number of accounts, calls, 
        and logons, based on age groups and gender. The plots above allow you to explore how 
        these variables differ across age groups and between genders.
    """)

# Sorting Control and Test Groups in the main app.py or wherever necessary:
def sort_groups(df_merged):
    """
    Function to sort control and test groups based on client_id, visit_id, process_step, and date_time.
    """
    control_group = df_merged[df_merged['variation'] == 'Control']
    test_group = df_merged[df_merged['variation'] == 'Test']

    # Sort control group
    control_group_sorted = control_group.sort_values(by=['client_id', 'visit_id', 'process_step', 'date_time'])

    # Sort test group
    test_group_sorted = test_group.sort_values(by=['client_id', 'visit_id', 'process_step', 'date_time'])

    return control_group_sorted, test_group_sorted