# pages/hypothesistestcompletionrate.py
import pandas as pd
import numpy as np
import scipy.stats as stats  # Correct import for statistical functions
import streamlit as st

# Function to perform a two-proportion z-test
def two_proportion_z_test(p1, p2, n1, n2):
    """
    Perform two-proportion z-test to compare completion rates between two groups.
    Args:
        p1, p2: Completion proportions of control and test groups.
        n1, n2: Sample sizes for control and test groups.
    Returns:
        z-statistic and p-value of the z-test.
    """
    # Calculate pooled proportion
    P = (p1 * n1 + p2 * n2) / (n1 + n2)
    
    # Calculate the standard error
    SE = np.sqrt(P * (1 - P) * (1 / n1 + 1 / n2))
    
    # Calculate the z-statistic
    z = (p1 - p2) / SE
    
    # Calculate the p-value (two-tailed test) using scipy.stats.norm
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))  # Corrected here
    
    return z, p_value

# Show the hypothesis testing page
def show_page(df):
    """
    Show the hypothesis testing page with completion rate analysis.
    Args:
        df: The dataframe containing the data
    """
    # Sort the data by variation and other relevant columns
    df_sorted = df.sort_values(by=['variation', 'client_id', 'visit_id', 'process_step', 'date_time'])

    # Define 'completion' column if not already defined (this should already be defined in data_loader.py)
    if 'completion' not in df_sorted.columns:
        df_sorted['completion'] = df_sorted['process_step'].apply(lambda x: 1 if x in ['confirm', 'completed'] else 0)

    # Define age bins and categorize ages
    bins = [0, 30, 40, 50, 100]  # Adjust intervals as necessary
    labels = ['Under 30', '30-39', '40-49', '50 and above']
    df_sorted['age_group'] = pd.cut(df_sorted['clnt_age'], bins=bins, labels=labels)

    # Define process steps for hypothesis testing
    steps = ['confirm', 'step_1', 'step_2', 'step_3']

    # Create an empty list to store results
    results = []

    # Hypothesis testing for each process step
    for step in steps:
        # Filter data for the current process step in control and test groups
        control_completions = df_sorted[(df_sorted['process_step'] == step) & (df_sorted['variation'] == 'Control')]['completion'].mean() * 100  # Completion rate (%) for control group
        test_completions = df_sorted[(df_sorted['process_step'] == step) & (df_sorted['variation'] == 'Test')]['completion'].mean() * 100  # Completion rate (%) for test group

        control_total = df_sorted[(df_sorted['process_step'] == step) & (df_sorted['variation'] == 'Control')].shape[0]
        test_total = df_sorted[(df_sorted['process_step'] == step) & (df_sorted['variation'] == 'Test')].shape[0]

        # Convert completion rate to proportion
        p_control = control_completions / 100
        p_test = test_completions / 100
        
        # Perform two-proportion z-test
        z_stat, p_value = two_proportion_z_test(p_control, p_test, control_total, test_total)
        
        # Store the results for each step
        results.append({
            'Step': step,
            'Control Completion Rate': control_completions,
            'Test Completion Rate': test_completions,
            'Z-statistic': z_stat,
            'P-value': p_value,
            'Significant': p_value < 0.05
        })

    # Convert results to a DataFrame
    results_df = pd.DataFrame(results)

    # Display the results
    st.subheader("Hypothesis Testing Results for Completion Rates by Step")
    st.dataframe(results_df)

    # Interpret the results for each step
    for idx, row in results_df.iterrows():
        if row['Significant']:
            st.write(f"**Step: {row['Step']}** - The difference in completion rates between control and test groups is statistically significant (Z = {row['Z-statistic']:.4f}, P = {row['P-value']:.4f}).")
        else:
            st.write(f"**Step: {row['Step']}** - There is no significant difference in completion rates between control and test groups (Z = {row['Z-statistic']:.4f}, P = {row['P-value']:.4f}).")

    # Average completion rates comparison (as previously done)
    control_mean = df_sorted[df_sorted['variation'] == 'Control']['completion'].mean() * 100
    test_mean = df_sorted[df_sorted['variation'] == 'Test']['completion'].mean() * 100
    _, p_value = stats.ttest_ind(df_sorted[df_sorted['variation'] == 'Control']['completion'], df_sorted[df_sorted['variation'] == 'Test']['completion'], alternative='two-sided')

    st.subheader("Average Completion Rate Comparison")
    st.write(f"Average completion rate for Control group: {control_mean:.2f}%")
    st.write(f"Average completion rate for Test group: {test_mean:.2f}%")
    st.write(f"T-statistic: {_:.4f}")
    st.write(f"P-value: {p_value:.4f}")

    alpha = 0.05
    if p_value < alpha:
        st.write("**Reject the null hypothesis**: The completion rates are significantly different between the Test and Control groups.")
    else:
        st.write("**Fail to reject the null hypothesis**: The completion rates are not significantly different between the Test and Control groups.")

    completion_rate_increase = test_mean - control_mean
    st.write(f"Completion rate increase: {completion_rate_increase:.2f}%")
    if completion_rate_increase >= 5:
        st.write("The completion rate increase meets the 5% threshold, justifying the cost of the new design.")
    else:
        st.write("The completion rate increase does not meet the 5% threshold. The new design may not justify its cost.")