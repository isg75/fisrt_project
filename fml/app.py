# app.py
# app.py
import streamlit as st
from data_loader import load_data  # Assuming load_data is in the data_loader.py file
from pages import about, summary, unique_values, stats, demographics, hypothesistestcompletionrate, duration, completion, error_rate

def main():
    """
    Main function to run the Streamlit app for A/B Test Demo.
    
    Sets up the page configuration, loads data, and manages navigation
    through different pages of the app.
    """
    st.set_page_config(page_title="A/B Test Demo for Group 7")
    
    # Provide the correct path to the CSV
    data_path = "path_to_your_data.csv"  # Make sure this path is correct

    # Load the data from data_loader
    df = load_data(data_path)

    if df is None:
        st.error("Data could not be loaded. Please check your file path or data source.")
        return

    # Sort the data into control and test groups
    control_group = df[df['variation'] == 'Control']
    test_group = df[df['variation'] == 'Test']

    control_group_sorted = control_group.sort_values(by=['client_id', 'visit_id', 'process_step', 'date_time'])
    test_group_sorted = test_group.sort_values(by=['client_id', 'visit_id', 'process_step', 'date_time'])

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page:", [
        "About the Project", 
        "Data Summary", 
        "Unique Values", 
        "Basic Statistics", 
        "Demographics Analysis", 
        "Hypothesis Testing Completion Rate", 
        "Process Duration Analysis",  
        "Completion Time Analysis",
        "Error Rate Hypothesis Testing"
    ])

    # Handle page navigation and pass the df and sorted groups to the page
    if page == "About the Project":
        about.show_about_project()
    elif page == "Data Summary":
        summary.show_data_summary(df)
    elif page == "Unique Values":
        unique_values.show_unique_values_in_categorical_columns(df)
    elif page == "Basic Statistics":
        stats.show_basic_statistics(df)
    elif page == "Demographics Analysis":
        demographics.show_demographics(df, control_group_sorted, test_group_sorted)
    elif page == "Hypothesis Testing Completion Rate":
        hypothesistestcompletionrate.show_page(df)
    elif page == "Process Duration Analysis":
        duration.show_process_duration(df)
    elif page == "Completion Time Analysis":
        completion.show_completion_time(df)
    elif page == "Error Rate Hypothesis Testing":
        error_rate.show_error_rate_analysis(df)

if __name__ == "__main__":
    main()