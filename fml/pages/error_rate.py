#pages/error_rate.py
import streamlit as st
import pandas as pd
from scipy.stats import binomtest, ttest_ind
from data_loader import load_data

# Function to calculate errors
def calculate_errors(group):
    group['step_index'] = group['process_step'].map({'start': 0, 'step_1': 1, 'step_2': 2, 'step_3': 3, 'confirm': 4})
    group['error'] = group['step_index'].diff().apply(lambda x: x < 0)  # Negative diff indicates a backward step
    return group

# Function to calculate error rates for both groups
def calculate_error_rates(control_group, test_group):
    # Calculate errors
    control_group = calculate_errors(control_group)
    test_group = calculate_errors(test_group)

    # Calculate Error Rates
    control_error_rate = control_group['error'].mean() * 100
    test_error_rate = test_group['error'].mean() * 100

    # Error rate difference
    error_rate_difference = control_error_rate - test_error_rate  # Difference between control and test error rates
    threshold = 5  # 5% threshold for the difference

    # Perform hypothesis testing: binomial test
    control_errors = control_group['error'].sum()
    control_total = len(control_group)
    test_errors = test_group['error'].sum()
    test_total = len(test_group)

    # Perform a one-tailed binomial test
    result = binomtest(test_errors, test_total, control_errors / control_total, alternative='less')

    # Perform independent t-test for error rates
    control_error_rate_values = control_group['error'].astype(int)
    test_error_rate_values = test_group['error'].astype(int)

    # Perform the independent t-test
    t_stat, t_p_value = ttest_ind(control_error_rate_values, test_error_rate_values, equal_var=False, alternative='two-sided')

    return {
        'control_error_rate': control_error_rate,
        'test_error_rate': test_error_rate,
        'error_rate_difference': error_rate_difference,
        'binomial_p_value': result.pvalue,
        't_statistic': t_stat,
        't_p_value': t_p_value,
    }

# Function to display the results
def show_error_rate_analysis(df):
    st.title("Error Rate Hypothesis Testing")

    # Split the data into control and test groups
    control_group = df[df['variation'] == 'Control']
    test_group = df[df['variation'] == 'Test']

    # Calculate error rates and perform hypothesis testing
    results = calculate_error_rates(control_group, test_group)

    # Display results
    st.subheader("Error Rates Comparison")
    st.write(f"Control Group Error Rate: {results['control_error_rate']:.2f}%")
    st.write(f"Test Group Error Rate: {results['test_error_rate']:.2f}%")
    st.write(f"Error Rate Difference: {results['error_rate_difference']:.2f}%")

    # Display hypothesis testing results
    st.subheader("Hypothesis Testing Results")

    # Binomial Test Results
    st.write(f"Binomial Test p-value: {results['binomial_p_value']:.4f}")
    if results['binomial_p_value'] < 0.05:
        st.write("The test group has significantly lower error rate than the control group (p-value < 0.05).")
    else:
        st.write("There is no significant difference in error rates between the test and control groups.")

    # T-test Results
    st.write(f"T-test Statistic: {results['t_statistic']:.4f}")
    st.write(f"T-test p-value: {results['t_p_value']:.4f}")
    if results['t_p_value'] < 0.05:
        st.write("There is a significant difference in error rates between the control and test groups.")
    else:
        st.write("There is no significant difference in error rates between the control and test groups.")

    # Conclusion based on practical significance (error rate difference)
    st.subheader("Practical Significance")
    if results['error_rate_difference'] >= 5:
        st.write("The test group has at least a 5% lower error rate than the control group, which is practically significant.")
    else:
        st.write("The error rate difference is less than 5%, which may not be practically significant for making decisions.")

    # Conclusion
    st.subheader("Conclusion")
    if results['binomial_p_value'] < 0.05 and results['error_rate_difference'] >= 5:
        st.write("The test group shows both statistical and practical significance. The improvement in error rates may justify action.")
    else:
        st.write("Although the test group shows statistically significant differences, the practical significance (error rate difference) may not justify making significant changes.")