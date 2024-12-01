# pages/about.py
import streamlit as st
from data_loader import load_data

def show_about_project():
    st.title("About the Project")
    
    st.header("Project Overview by Ceci and Eliska")
    st.write(
        """
        An A/B test was conducted from 3/15/2017 to 6/20/2017 by the Vanguard team to evaluate the impact of a new digital interface.

        **Control Group**: Clients interacted with Vanguard’s traditional online process.  
        **Test Group**: Clients experienced the new, spruced-up digital interface.

        ### Project Timeline:
        - **Day 1 & 2 (Week 5)**  
          EDA & Data Cleaning  
          Client behavior analysis – identifying relations and forming hypotheses.

        - **Day 3 (Week 5)**  
          Performance Metrics  
          Success Indicators  
          Redesign Outcome

        - **Day 4 & 5 (Week 5)**  
          Hypothesis Testing  
          Completion Rate  
          Cost-Effectiveness Threshold  
          Additional Hypothesis Examples  
          Experiment Evaluation  
          Design Effectiveness  
          Duration Assessment  
          Further Data Needs

        - **Day 1 & 2 (Week 6)**  
          Tableau  
          Visualization Tasks

        - **Day 3 & 4 (Week 6)**  
          Further Data Analysis and Presentation Preparation
        """
    )

    # About Vanguard Group
    st.subheader("About Vanguard Group")
    st.write(
        """
        The Vanguard Group is one of the world’s largest investment management companies, founded in 1975 by John C. Bogle. It is renowned for pioneering low-cost index funds, which allow investors to track broad market indices with minimal fees. Vanguard’s investor-owned structure means that the company is owned by the funds it manages, aligning its interests with those of its investors. Today, Vanguard manages trillions of dollars in assets, offering a wide range of investment products including mutual funds, ETFs, and retirement plans, with a focus on long-term, passive investing strategies.
        """
    )

    # New Sub-heading: Digital Challenge and Our Role
    st.subheader("Digital Challenge and Our Role")
    st.write(
        """
        **A/B Test Objective:**  
        The goal of this experiment was to evaluate a new, modernized user interface (UI) designed to improve the online client journey through in-context prompts.

        **Experiment Details:**
        - **Control Group**: Clients used the traditional Vanguard user interface.
        - **Test Group**: Clients experienced the new, intuitive UI with contextual prompts designed to guide them through the online process.

        **Timeline:**  
        The experiment took place from **March 15, 2017 – June 20, 2017**.

        **Process Flow:**  
        Clients followed a sequence of steps starting from the initial page, progressing through three key steps, and finishing at the confirmation page.

        *As part of the CX (Customer Experience) team, our job was to evaluate whether the new UI leads to better user engagement and higher completion rates during online processes.*
        """
    )

    # **Did the new UI lead to higher completion rates?**
    st.write("**Did the new UI lead to higher completion rates?**")
    st.write(
        """
        The A/B test was designed to determine whether the new, intuitive UI with contextual prompts improved user engagement and completion rates compared to the traditional Vanguard user interface. The results from hypothesis testing and analysis will help answer this key question.
        """
    )

    # New Section: What Data We Have Been Working With
    st.subheader("What Data We Have Been Working With")
    st.write(
        """
        The analysis is based on a rich set of data that provides insights into both client demographics and their digital interactions with Vanguard's platform. Below is a summary of the key datasets:

        - **Client Profiles**: This includes demographic and account details such as:
          - **Client's Age**: The age of each client.
          - **Client's Tenure**: How long each client has been with Vanguard, in both years and months.
          - **Client's Balance**: The total balance held across all of a client's accounts with Vanguard.
          - **Number of Accounts**: The number of accounts the client holds with Vanguard.

        - **Digital Footprints**: This data captures the client's online activity at each step in the client journey:
          - **Process Steps**: The sequence of steps each client went through in their digital process (e.g., initial page, steps 1-3, and confirmation page).
          - **Date-Time Logs**: Timestamps for each action taken by the client during their online session, allowing us to track the client’s progression through each step.

        - **Experiment Roster**: This dataset indicates which group each client was assigned to (Control or Test), based on their unique **client_id**. It helps us compare the performance of the Control group (traditional UI) against the Test group (new UI with contextual prompts).
        """
    )

    # New Section: Key Performance Indicators (KPIs)
    st.markdown("## **Key Performance Indicators (KPI's)**")
    st.write(
        """
        The following KPIs were tracked to evaluate the effectiveness of the experiment and assess user engagement:
        
        - **Completion Rate**: The percentage of users who completed the process flow from start to finish. This helps to evaluate whether the new interface leads to higher engagement and successful outcomes.
        - **Engagement Metrics**:
          - **Logins**: The frequency with which clients logged into their accounts, a measure of engagement and usage.
          - **Calls**: The number of client service calls made, indicating the level of client support needed.
        - **Average Account Balance**: The average balance held by clients, which provides insights into client wealth and account activity.
        - **Tenure**: The number of years a client has been with Vanguard, reflecting client loyalty and long-term engagement.
        """
    )

    st.header("Getting Started")
    st.write(
        """
        ## Metadata
        This comprehensive set of fields will guide your analysis, helping you uncover insights into client behavior and preferences.

        - **client_id**: A unique identifier for each client.
        - **variation**: Denotes whether a client was part of the experiment (Control or Test).
        - **visitor_id**: A unique ID for each client-device combination.
        - **visit_id**: A unique ID for each web visit/session.
        - **process_step**: The step in the digital process that the client is engaged in.
        - **date_time**: Timestamp of each web activity.
        - **clnt_tenure_yr**: The number of years a client has been with Vanguard.
        - **clnt_tenure_mnth**: The number of months a client has been with Vanguard.
        - **clnt_age**: The client’s age.
        - **gendr**: The client’s gender.
        - **num_accts**: The number of accounts the client holds with Vanguard.
        - **bal**: The total balance across all client accounts.
        - **calls_6_mnth**: The number of times the client reached out over the phone in the last 6 months.
        - **logons_6_mnth**: The number of times the client logged into Vanguard’s platform over the last 6 months.

        ## Bonus: Additional Tasks (Optional)
        If you have extra time after completing the core tasks, explore the following optional questions and activities:

        - **Client Behavior Analysis**: Dive deeper into the data to analyze client behavior patterns and trends.
        - **Power and Effect Size**: Perform power analysis to determine the sample size needed for a reliable test and compute the effect size.
        - **Streamlit Integration**: Add Streamlit widgets to your project to enable real-time analysis and visualization. Customize your app for interactivity.
        """
    )

    # **Data Cleaning & Merging Process** section
    st.subheader("Data Cleaning & Merging Process")
    st.write(
        """
        The data cleaning and merging process is crucial for ensuring the integrity and consistency of the dataset. Here's how we handled the data:

        **Clean Datasets**:
        - **Load Data**: We begin by loading the raw data from various sources.
        - **Drop Missing Values**: Any missing values in critical columns (like `client_id`, `process_step`, etc.) are removed to ensure that we only work with complete data.
        - **Rename Columns**: Columns are renamed to have consistent naming conventions and be more meaningful for analysis.
        - **Remove 'X' Gender Values**: Any rows with 'X' as a gender label are removed as this represents incomplete or erroneous data.
        - **Map Gender Codes to Labels**: Gender codes are mapped to more readable labels (e.g., 'M' -> 'Male', 'F' -> 'Female').
        - **Ensure Proper DateTime Format**: We ensure that the `date_time` column is in the correct format (i.e., datetime objects), allowing for time-based analysis.

        **Merge Datasets**:
        - **Merge Demographic Datasets**: We combine the demographic data (client information such as age, tenure, balance) into a single dataset.
        - **Concatenate Web Interactions Dataset**: The web interactions (client's steps through the online process) are merged with the demographic data based on the `client_id`.
        - **Final Merge on `client_id`**: After all data is cleaned and preprocessed, we merge all datasets on the common `client_id` column to create a comprehensive dataset.

        **Segment by Experiment Group**:
        - **Control and Test Groups**: The dataset is split into two groups based on the `variation` column: the Control group (clients using the traditional UI) and the Test group (clients using the new UI with contextual prompts).

        **Sort Data**:
        - **Sort by client_id, visit_id, process_step, and date_time**: This ensures that the data is ordered by the client's journey through the process, from their first visit to the confirmation step.

        **Age Group Categorization**:
        - **Assign Age Groups**: Based on defined age bins, we categorize clients into age groups (e.g., under 30, 30-39, 40-49, 50+). This categorization is applied to the `df_merged`, as well as to the `control` and `test` datasets to facilitate age-based analysis.
        """
    )

    # **Who are our clients?** section
    st.subheader("Who Are Our Clients?")
    st.write(
        """
        For demographic analysis, we worked with a pool of **70,591 users** after applying the cleaning and merging processes to ensure data quality.

        **Group with highest average tenure and balance**:
        - **Gender**: Male
        - **Age Group**: 50 and above
        - **Client's Tenure**: 16.35 years
        - **Balance**: 294,239.72$
        **Average Persona**:
        - **Gender**: Male
        - **Age Group**: 30-39
        - **Average Tenure**: 11.65 years
        - **Average Balance**: 126,284.41$
        """
    )

    # **Further Observations** section
    st.subheader("Further Observations")
    st.write(
        """
        - Males generally have higher average balances than females, with the highest balances observed in the "50 and above" age group for both genders.
        - Both males and females show similar tenure patterns, with longer tenures seen in older age groups (50+ years), indicating long-term clients.
        - The “Unknown" gender category typically has lower average balances, likely due to potential data gaps or non-disclosure of gender.
        """
    )
    # **Did the new UI lead to higher completion rates?**
    st.write("**Did the new UI lead to higher completion rates?**")
    st.write(
        """
        The A/B test was designed to determine whether the new, intuitive UI with contextual prompts improved user engagement and completion rates compared to the traditional Vanguard user interface. The results from hypothesis testing and analysis will help answer this key question.
        """
    )

    # New Section: What Data We Have Been Working With
    st.subheader("What Data We Have Been Working With")
    st.write(
        """
        The analysis is based on a rich set of data that provides insights into both client demographics and their digital interactions with Vanguard's platform. Below is a summary of the key datasets:

        - **Client Profiles**: This includes demographic and account details such as:
          - **Client's Age**: The age of each client.
          - **Client's Tenure**: How long each client has been with Vanguard, in both years and months.
          - **Client's Balance**: The total balance held across all of a client's accounts with Vanguard.
          - **Number of Accounts**: The number of accounts the client holds with Vanguard.

        - **Digital Footprints**: This data captures the client's online activity at each step in the client journey:
          - **Process Steps**: The sequence of steps each client went through in their digital process (e.g., initial page, steps 1-3, and confirmation page).
          - **Date-Time Logs**: Timestamps for each action taken by the client during their online session, allowing us to track the client’s progression through each step.

        - **Experiment Roster**: This dataset indicates which group each client was assigned to (Control or Test), based on their unique **client_id**. It helps us compare the performance of the Control group (traditional UI) against the Test group (new UI with contextual prompts).
        """
    )

    # New Section: Key Performance Indicators (KPIs)
    st.markdown("## **Key Performance Indicators (KPI's)**")
    st.write(
        """
        The following KPIs were tracked to evaluate the effectiveness of the experiment and assess user engagement:
        
        - **Completion Rate**: The percentage of users who completed the process flow from start to finish. This helps to evaluate whether the new interface leads to higher engagement and successful outcomes.
        - **Engagement Metrics**:
          - **Logins**: The frequency with which clients logged into their accounts, a measure of engagement and usage.
          - **Calls**: The number of client service calls made, indicating the level of client support needed.
        - **Average Account Balance**: The average balance held by clients, which provides insights into client wealth and account activity.
        - **Tenure**: The number of years a client has been with Vanguard, reflecting client loyalty and long-term engagement.
        """
    )

    st.header("Getting Started")
    st.write(
        """
        ## Metadata
        This comprehensive set of fields will guide your analysis, helping you uncover insights into client behavior and preferences.

        - **client_id**: A unique identifier for each client.
        - **variation**: Denotes whether a client was part of the experiment (Control or Test).
        - **visitor_id**: A unique ID for each client-device combination.
        - **visit_id**: A unique ID for each web visit/session.
        - **process_step**: The step in the digital process that the client is engaged in.
        - **date_time**: Timestamp of each web activity.
        - **clnt_tenure_yr**: The number of years a client has been with Vanguard.
        - **clnt_tenure_mnth**: The number of months a client has been with Vanguard.
        - **clnt_age**: The client’s age.
        - **gendr**: The client’s gender.
        - **num_accts**: The number of accounts the client holds with Vanguard.
        - **bal**: The total balance across all client accounts.
        - **calls_6_mnth**: The number of times the client reached out over the phone in the last 6 months.
        - **logons_6_mnth**: The number of times the client logged into Vanguard’s platform over the last 6 months.

        ## Bonus: Additional Tasks (Optional)
        If you have extra time after completing the core tasks, explore the following optional questions and activities:

        - **Client Behavior Analysis**: Dive deeper into the data to analyze client behavior patterns and trends.
        - **Power and Effect Size**: Perform power analysis to determine the sample size needed for a reliable test and compute the effect size.
        - **Streamlit Integration**: Add Streamlit widgets to your project to enable real-time analysis and visualization. Customize your app for interactivity.
        """
    )

    # **Data Cleaning & Merging Process** section
    st.subheader("Data Cleaning & Merging Process")
    st.write(
        """
        The data cleaning and merging process is crucial for ensuring the integrity and consistency of the dataset. Here's how we handled the data:

        **Clean Datasets**:
        - **Load Data**: We begin by loading the raw data from various sources.
        - **Drop Missing Values**: Any missing values in critical columns (like `client_id`, `process_step`, etc.) are removed to ensure that we only work with complete data.
        - **Rename Columns**: Columns are renamed to have consistent naming conventions and be more meaningful for analysis.
        - **Remove 'X' Gender Values**: Any rows with 'X' as a gender label are removed as this represents incomplete or erroneous data.
        - **Map Gender Codes to Labels**: Gender codes are mapped to more readable labels (e.g., 'M' -> 'Male', 'F' -> 'Female').
        - **Ensure Proper DateTime Format**: We ensure that the `date_time` column is in the correct format (i.e., datetime objects), allowing for time-based analysis.

        **Merge Datasets**:
        - **Merge Demographic Datasets**: We combine the demographic data (client information such as age, tenure, balance) into a single dataset.
        - **Concatenate Web Interactions Dataset**: The web interactions (client's steps through the online process) are merged with the demographic data based on the `client_id`.
        - **Final Merge on `client_id`**: After all data is cleaned and preprocessed, we merge all datasets on the common `client_id` column to create a comprehensive dataset.

        **Segment by Experiment Group**:
        - **Control and Test Groups**: The dataset is split into two groups based on the `variation` column: the Control group (clients using the traditional UI) and the Test group (clients using the new UI with contextual prompts).

        **Sort Data**:
        - **Sort by client_id, visit_id, process_step, and date_time**: This ensures that the data is ordered by the client's journey through the process, from their first visit to the confirmation step.

        **Age Group Categorization**:
        - **Assign Age Groups**: Based on defined age bins, we categorize clients into age groups (e.g., under 30, 30-39, 40-49, 50+). This categorization is applied to the `df_merged`, as well as to the `control` and `test` datasets to facilitate age-based analysis.
        """
    )

    # **Who are our clients?** section
    st.subheader("Who Are Our Clients?")
    st.write(
        """
        For demographic analysis, we worked with a pool of **70,591 users** after applying the cleaning and merging processes to ensure data quality.

        **Group with highest average tenure and balance**:
        - **Gender**: Male
        - **Age Group**: 50 and above
        - **Client's Tenure**: 16.35 years
        - **Balance**: 294,239.72$
        **Average Persona**:
        - **Gender**: Male
        - **Age Group**: 30-39
        - **Average Tenure**: 11.65 years
        - **Average Balance**: 126,284.41$
        """
    )

    # **Further Observations** section
    st.subheader("Further Observations")
    st.write(
        """
        - Males generally have higher average balances than females, with the highest balances observed in the "50 and above" age group for both genders.
        - Both males and females show similar tenure patterns, with longer tenures seen in older age groups (50+ years), indicating long-term clients.
        - The “Unknown" gender category typically has lower average balances, likely due to potential data gaps or non-disclosure of gender.
        """
    )
    # New Section: Key Performance Indicators (KPIs)
    st.markdown("## **Key Performance Indicators (KPI's)**")
    st.write(
        """
        The following KPIs were tracked to evaluate the effectiveness of the experiment and assess user engagement:
        
        - **Completion Rate**: The percentage of users who completed the process flow from start to finish. This helps to evaluate whether the new interface leads to higher engagement and successful outcomes.
        - **Engagement Metrics**:
          - **Logins**: The frequency with which clients logged into their accounts, a measure of engagement and usage.
          - **Calls**: The number of client service calls made, indicating the level of client support needed.
        - **Average Account Balance**: The average balance held by clients, which provides insights into client wealth and account activity.
        - **Tenure**: The number of years a client has been with Vanguard, reflecting client loyalty and long-term engagement.
        
        ### Additional Insights:
        
        - **Completion Rate**:  
          If the **Test group** shows a higher completion rate compared to the **Control group**, it suggests that the new design has improved user engagement, making it easier for users to complete the process. This could indicate that the intuitive interface or contextual prompts helped users to feel more confident and successful in completing the steps.

        - **Time Spent on Each Step**:  
          A lower time spent at each step in the **Test group** compared to the **Control group** would suggest that the new design is more efficient. This can be interpreted as users moving through the process more quickly, likely due to the improved clarity or guidance offered by the new UI design.

        - **Error Rates**:  
          A reduction in error rates in the **Test group** would suggest that the new design is more intuitive and user-friendly. This could mean that fewer users encountered confusion or made mistakes during the process, likely because the contextual prompts and simplified steps helped guide them more effectively.

        - **Bounce Rates**:  
          If the **Test group** has a lower bounce rate compared to the **Control group**, it suggests that the new design is better at keeping users engaged throughout the process. A lower bounce rate would indicate that users are more likely to stay in the process, reducing drop-offs or exits at any given step, which is a good indicator of user retention and interest.

        """
    )
        # New Section: Tableau Visuals
    st.markdown("## **Tableau Visuals**")
    st.write(
        """
        You can explore the interactive Tableau dashboard for further insights into the data and visualizations by following the link below:
        
        [**Vanguard CX Story**](https://public.tableau.com/app/profile/eliska.simova/viz/Vanguard_CX/Vanguard_story?publish=yes)
        """
    )

    # New Section: Hypothesis Testing
    st.markdown("## **Hypothesis Testing**")
    
    # Hypothesis 1
    st.subheader("Hypothesis 1: Completion Rate Comparison")
    st.write(
        """
        **Hypothesis**: "Is there a significant difference in the completion rates between the Control group and the Test group at each step of the process?"

        - All steps show statistically significant differences in completion rates between the **Test group** (new UI) and **Control group** (old UI).
        - A **p-value of 0.0000** for each step indicates strong evidence against the null hypothesis.
        - We **reject the null hypothesis** at all steps, meaning that the new design does indeed have a significantly different impact on user completion rates at each step compared to the old design.
        """
    )

    # Hypothesis 2
    st.subheader("Hypothesis 2: Completion Rate Increase")
    st.write(
        """
        **Hypothesis**: "Does the introduction of the new UI design result in a minimum 5% increase in the completion rate compared to the existing design, making it cost-effective?"

        - The completion rate increase of **9.82%** between the **Test** and **Control** groups exceeds the **5%** threshold set by Vanguard.
        - The **new UI design** could be considered **worthwhile from a business perspective** due to this significant increase in the completion rate.
        """
    )

    # Hypothesis 3
    st.subheader("Hypothesis 3: Average Client Tenure Comparison")
    st.write(
        """
        **Hypothesis**: "Is the average client tenure of those engaging with the new process the same as those engaging with the old process?"

        - **Control Group Average Tenure**: 12.09 years
        - **Test Group Average Tenure**: 11.98 years
        - **p-value**: 0.0868, **Statistic**: 1.7124 (indicates how much the means differ relative to variability)
        - We **fail to reject the null hypothesis**, meaning the **average tenure is not significantly different** between the two groups.
        - The lack of significant difference in **average tenure** supports the validity of the A/B test results.
        """
    )

    # Hypothesis 4
    st.subheader("Hypothesis 4: Average Client Age Comparison")
    st.write(
        """
        **Hypothesis**: "Is the average client age of those engaging with the new process the same as those engaging with the old process?"

        - **Control Average Age**: 47.50 years
        - **Test Average Age**: 47.16 years
        - **p-value**: 0.0160
        - Since the **p-value is less than 0.05**, we **reject the null hypothesis**, indicating that there is a **statistical difference** in the average age between the Test and Control groups.
        """
    )

    # Hypothesis 5
    st.subheader("Hypothesis 5: Error Rate Comparison")
    st.write(
        """
        **Hypothesis**: "Does the new UI design lead to a reduction in error rates compared to the old design, and is this reduction statistically significant?"

        - **Control Error Rate**: 19.21%
        - **Test Error Rate**: 17.64%
        - **Percentage Difference**: 1.57%
        - **p-value**: 0.0000
        - We **reject the null hypothesis** that there is no difference between the groups, indicating that the **new UI** has a **significantly lower error rate** than the old UI.
        """
    )

    # Hypothesis 6
    st.subheader("Hypothesis 6: Bounce Rate Comparison")
    st.write(
        """
        **Hypothesis**: “Is the bounce rate of the Test group lower than the Control group across all steps?”

        - The **Test group** showed a **statistically significant lower bounce rate** only at **Step 1**.
        - For **Steps 0**, **2**, and **3**, there were **no statistically significant differences** between the Control and Test groups.
        """
    )

    # New Section: Experiment Evaluation
    st.markdown("## **Experiment Evaluation**")
    st.write(
        """
        - **Average Ages**: The average age is statistically different between the Test and Control groups, as indicated by the **p-value of 0.0160**, which is less than the **0.05 threshold**.
        - This means the distribution of **ages** between the two groups is **not uniform**, and age differences could potentially introduce a **bias in the observed completion rate**.
        """
    )
    # New Section: Recommendations
    st.markdown("## **_Recommendations_**")
    
    # Recommendation 1
    st.subheader("1. **Simplify the Process**")
    st.write(
        """
        All age groups may benefit from a more straightforward flow.

        💡 **Reduce unnecessary steps and minimize user decisions to streamline the experience**.
        """
    )

    # Recommendation 2
    st.subheader("2. **Provide Contextual Help**")
    st.write(
        """
        High bounce rates may suggest confusion or hesitation; users might benefit from guidance or support.

        💡 **Add tooltips, help icons, and live support to guide users**.
        """
    )

    # Recommendation 3
    st.subheader("3. **Improve Visual Design**")
    st.write(
        """
        Bounce rates at certain steps suggest that users might find some of the content unclear.

        💡 **Ensure readability and consistency in font size, contrast, and button design**.
        """
    )

    # Recommendation 4
    st.subheader("4. **Personalize Experience**")
    st.write(
        """
        Users might lose track of where they are in the process or forget to complete it.

        💡 **Offer reminders and allow users to save their progress for later completion**.
        """
    )