#bounce_rate.py
import streamlit as st
import pandas as pd
from scipy.stats import norm
from data_loader import load_data

# Function to calculate counts for z-test
def calculate_counts(group):
    steps = ['start', 'step_1', 'step_2', 'step_3', 'confirm']
    counts = []  # Store counts as tuples (N_started, N_dropped)
    
    for i in range(len(steps) - 1):
        current_step = steps[i]
        next_step = steps[i + 1]
        # Total users who started at this step
        started = group[group['process_step'] == current_step]['client_id'].nunique()
        # Total users who dropped off at this step
        reached_next = group[group['process_step'] == next_step]['client_id'].nunique()
        dropped = started - reached_next
        counts.append((started, dropped))
    
    return counts

# Function to perform two-proportion z-test
def two_proportion_z_test(n1, x1, n2, x2):
    # Calculate proportions
    p1 = x1 / n1 if n1 > 0 else 0
    p2 = x2 / n2 if n2 > 0 else 0
    
    # Pooled proportion
    p = (x1 + x2) / (n1 + n2)
    
    # Calculate z-statistic
    z = (p1 - p2) / ((p * (1 - p) * (1 / n1 + 1 / n2)) ** 0.5)
    
    # Calculate two-tailed p-value
    p_value = 2 * (1 - norm.cdf(abs(z)))
    
    return z, p_value

# Main function to display the bounce rate analysis page
def show_bounce_rate(df):
    st.title("Bounce Rate Analysis")

    # Ensure that the necessary columns exist in the dataframe
    if 'clnt_age' not in df.columns or 'process_step' not in df.columns or 'client_id' not in df.columns:
        st.error("Required columns ('clnt_age', 'process_step', 'client_id') are missing.")
        return
    
    # Create age groups based on 'clnt_age'
    bins = [0, 30, 40, 50, 100]  # You can adjust the age bins as needed
    labels = ['Under 30', '30-39', '40-49', '50 and above']
    df['age_group'] = pd.cut(df['clnt_age'], bins=bins, labels=labels)
    
    # Split the data into Control and Test groups
    control_group = df[df['variation'] == 'Control']
    test_group = df[df['variation'] == 'Test']
    
    # Sort Control and Test groups
    control_group_sorted = control_group.sort_values(by=['client_id', 'visit_id', 'process_step', 'date_time'])
    test_group_sorted = test_group.sort_values(by=['client_id', 'visit_id', 'process_step', 'date_time'])
    
    # Calculate the drop-off rates for both Control and Test groups
    control_dropoff_rate = calculate_dropoff_rate(control_group_sorted)
    test_dropoff_rate = calculate_dropoff_rate(test_group_sorted)

    # Display Bounce Rates for Control and Test Groups
    st.subheader("Bounce Rates for Control and Test Groups (Overall)")
    st.write("Control Group Bounce Rates (%):")
    for step, rate in control_dropoff_rate.items():
        st.write(f"{step}: {rate:.2f}%")
    
    st.write("\nTest Group Bounce Rates (%):")
    for step, rate in test_dropoff_rate.items():
        st.write(f"{step}: {rate:.2f}%")
    
    # Calculate and display drop-off rates by Age Group for Control and Test groups
    st.subheader("Bounce Rates by Age Group")

    control_dropoff_rate_by_age = calculate_dropoff_rate_by_age(control_group_sorted)
    test_dropoff_rate_by_age = calculate_dropoff_rate_by_age(test_group_sorted)

    # Display Control group drop-off rates by Age
    st.write("Control Group Bounce Rates by Age Group:")
    for age_group, rates in control_dropoff_rate_by_age.items():
        st.write(f"Age Group: {age_group}")
        for step, rate in rates.items():
            st.write(f"  {step}: {rate:.2f}%")
    
    # Display Test group drop-off rates by Age
    st.write("Test Group Bounce Rates by Age Group:")
    for age_group, rates in test_dropoff_rate_by_age.items():
        st.write(f"Age Group: {age_group}")
        for step, rate in rates.items():
            st.write(f"  {step}: {rate:.2f}%")

    # **Hypothesis Testing (Z-Test) Section**
    st.subheader("Hypothesis Test using Z-Test")
    
    # Null Hypothesis: H₀ = The bounce rates for the control and test groups are the same for a given step.
    # Alternative Hypothesis: H₁ = The bounce rates for the control and test groups are different for a given step.
    
    st.write("""
    **Null Hypothesis (H₀)**: The bounce rates for the control and test groups are the same for a given step.  
    **Alternative Hypothesis (H₁)**: The bounce rates for the control and test groups are different for a given step.
    """)

    # Calculate counts for Control and Test groups
    control_counts = calculate_counts(control_group_sorted)
    test_counts = calculate_counts(test_group_sorted)

    # Perform z-tests for each step and decide on hypothesis
    z_test_results = []

    steps = ['start', 'step_1', 'step_2', 'step_3']
    for i, step in enumerate(steps):
        n1, x1 = control_counts[i]  # Control group: (N_started, N_dropped)
        n2, x2 = test_counts[i]     # Test group: (N_started, N_dropped)
        
        # Perform z-test for proportions
        z_stat, p_value = two_proportion_z_test(n1, x1, n2, x2)
        
        # Decide whether to reject the null hypothesis
        reject_null = p_value < 0.05
        
        # Store results
        z_test_results.append({
            'Step': step,
            'Control Bounce Rate (%)': (x1 / n1) * 100 if n1 > 0 else 0,
            'Test Bounce Rate (%)': (x2 / n2) * 100 if n2 > 0 else 0,
            'Z-Statistic': z_stat,
            'P-Value': p_value,
            'Reject Null Hypothesis': reject_null
        })

    # Convert results to DataFrame for display
    z_test_results_df = pd.DataFrame(z_test_results)

    # Display Z-Test Results
    st.write(z_test_results_df)

    # Optional: Provide a brief explanation of the Z-Test
    st.write("""
    The Z-Test is used here to test if there is a significant difference between the bounce rates for the control and test groups at each process step.
    
    - A Z-Statistic closer to 0 indicates that the difference between the two groups is small.
    - A p-value below 0.05 suggests that we reject the null hypothesis and conclude that the bounce rates are significantly different.
    - If the p-value is greater than 0.05, we fail to reject the null hypothesis, meaning the bounce rates are similar.
    """)