# About the Project

## Project Overview by Ceci and Eliska

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

## About Vanguard Group

The Vanguard Group is one of the world’s largest investment management companies, founded in 1975 by John C. Bogle. It is renowned for pioneering low-cost index funds, which allow investors to track broad market indices with minimal fees. Vanguard’s investor-owned structure means that the company is owned by the funds it manages, aligning its interests with those of its investors. Today, Vanguard manages trillions of dollars in assets, offering a wide range of investment products including mutual funds, ETFs, and retirement plans, with a focus on long-term, passive investing strategies.

## Digital Challenge and Our Role

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

### Did the new UI lead to higher completion rates?

The A/B test was designed to determine whether the new, intuitive UI with contextual prompts improved user engagement and completion rates compared to the traditional Vanguard user interface. The results from hypothesis testing and analysis will help answer this key question.

## What Data We Have Been Working With

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

## Key Performance Indicators (KPI's)

The following KPIs were tracked to evaluate the effectiveness of the experiment and assess user engagement:
  
- **Completion Rate**: The percentage of users who completed the process flow from start to finish. This helps to evaluate whether the new interface leads to higher engagement and successful outcomes.
- **Engagement Metrics**:
  - **Logins**: The frequency with which clients logged into their accounts, a measure of engagement and usage.
  - **Calls**: The number of client service calls made, indicating the level of client support needed.
- **Average Account Balance**: The average balance held by clients, which provides insights into client wealth and account activity.
- **Tenure**: The number of years a client has been with Vanguard, reflecting client loyalty and long-term engagement.

## Getting Started

### Metadata

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

### Bonus: Additional Tasks (Optional)

If you have extra time after completing the core tasks, explore the following optional questions and activities:

- **Client Behavior Analysis**: Dive deeper into the data to analyze client behavior patterns and trends.
- **Power and Effect Size**: Perform power analysis to determine the sample size needed for a reliable test and compute the effect size.
- **Streamlit Integration**: Add Streamlit widgets to your project to enable real-time analysis and visualization. Customize your app for interactivity.

## Data Cleaning & Merging Process

The data cleaning and merging process is crucial for ensuring the integrity and consistency of the dataset. Here's how we handled the data:

### Clean Datasets:
- **Load Data**: We begin by loading the raw data from various sources.
- **Drop Missing Values**: Any missing values in critical columns (like `client_id`, `process_step`, etc.) are removed to ensure that we only work with complete data.
- **Rename Columns**: Columns are renamed to have consistent naming conventions and be more meaningful for analysis.
- **Remove 'X' Gender Values**: Any rows with 'X' as a gender label are removed as this represents incomplete or erroneous data.
- **Map Gender Codes to Labels**: Gender codes are mapped to more readable labels (e.g., 'M' -> 'Male', 'F' -> 'Female').
- **Ensure Proper DateTime Format**: We ensure that the `date_time` column is in the correct format (i.e., datetime objects), allowing for time-based analysis.

### Merge Datasets:
- **Merge Demographic Datasets**: We combine the demographic data (client information such as age, tenure, balance) into a single dataset.
- **Concatenate Web Interactions Dataset**: The web interactions (client's steps through the online process) are merged with the demographic data based on the `client_id`.
- **Final Merge on `client_id`**: After all data is cleaned and preprocessed, we merge all datasets on the common `client_id` column to create a comprehensive dataset.

### Segment by Experiment Group:
- **Control and Test Groups**: The dataset is split into two groups based on the `variation` column: the Control group (clients using the traditional UI) and the Test group (clients using the new UI with contextual prompts).

### Sort Data:
- **Sort by client_id, visit_id, process_step, and date_time**: This ensures that the data is ordered by the client's journey through the process, from their first visit to the confirmation step.

### Age Group Categorization:
- **Assign Age Groups**: Based on defined age bins, we categorize clients into age groups (e.g., under 30, 30-39, 40-49, 50+). This categorization is applied to the `df_merged`, as well as to the `control` and `test` datasets to facilitate age-based analysis.

## Who Are Our Clients?

For demographic analysis, we worked with a pool of **70,591 users** after applying the cleaning and merging processes to ensure data quality.

### Group with highest average tenure and balance:
- **Gender**: Male
- **Age Group**: 50 and above
- **Client's Tenure**: 16.35 years
- **Balance**: 294,239.72$

### Average Persona:
- **Gender**: Male
- **Age Group**: 30-39
- **Average Tenure**: 11.65 years
- **Average Balance**: 126,284.41$

## Further Observations

- Males generally have higher average balances than females, with the highest balances observed in the "50 and above" age group for both genders.
- Both males and females show similar tenure patterns, with longer tenures seen in older age groups (50+ years), indicating long-term clients.
- The “Unknown" gender category typically has lower average balances, likely due to potential data gaps or non-disclosure of gender.

## **Did the new UI lead to higher completion rates?**
The A/B test was designed to determine whether the new, intuitive UI with contextual prompts improved user engagement and completion rates compared to the traditional Vanguard user interface. The results from hypothesis testing and analysis will help answer this key question.

## What Data We Have Been Working With
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

## Key Performance Indicators (KPI's)
The following KPIs were tracked to evaluate the effectiveness of the experiment and assess user engagement:
  
- **Completion Rate**: The percentage of users who completed the process flow from start to finish. This helps to evaluate whether the new interface leads to higher engagement and successful outcomes.
- **Engagement Metrics**:
  - **Logins**: The frequency with which clients logged into their accounts, a measure of engagement and usage.
  - **Calls**: The number of client service calls made, indicating the level of client support needed.
- **Average Account Balance**: The average balance held by clients, which provides insights into client wealth and account activity.
- **Tenure**: The number of years a client has been with Vanguard, reflecting client loyalty and long-term engagement.

## Getting Started
### Metadata
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

### Bonus: Additional Tasks (Optional)
If you have extra time after completing the core tasks, explore the following optional questions and activities:

- **Client Behavior Analysis**: Dive deeper into the data to analyze client behavior patterns and trends.
- **Power and Effect Size**: Perform power analysis to determine the sample size needed for a reliable test and compute the effect size.
- **Streamlit Integration**: Add Streamlit widgets to your project to enable real-time analysis and visualization. Customize your app for interactivity.

## Data Cleaning & Merging Process
The data cleaning and merging process is crucial for ensuring the integrity and consistency of the dataset. Here's how we handled the data:

### Clean Datasets:
- **Load Data**: We begin by loading the raw data from various sources.
- **Drop Missing Values**: Any missing values in critical columns (like `client_id`, `process_step`, etc.) are removed to ensure that we only work with complete data.
- **Rename Columns**: Columns are renamed to have consistent naming conventions and be more meaningful for analysis.
- **Remove 'X' Gender Values**: Any rows with 'X' as a gender label are removed as this represents incomplete or erroneous data.
- **Map Gender Codes to Labels**: Gender codes are mapped to more readable labels (e.g., 'M' -> 'Male', 'F' -> 'Female').
- **Ensure Proper DateTime Format**: We ensure that the `date_time` column is in the correct format (i.e., datetime objects), allowing for time-based analysis.

### Merge Datasets:
- **Merge Demographic Datasets**: We combine the demographic data (client information such as age, tenure, balance) into a single dataset.
- **Concatenate Web Interactions Dataset**: The web interactions (client's steps through the online process) are merged with the demographic data based on the `client_id`.
- **Final Merge on `client_id`**: After all data is cleaned and preprocessed, we merge all datasets on the common `client_id` column to create a comprehensive dataset.

### Segment by Experiment Group:
- **Control and Test Groups**: The dataset is split into two groups based on the `variation` column: the Control group (clients using the traditional UI) and the Test group (clients using the new UI with contextual prompts).

### Sort Data:
- **Sort by client_id, visit_id, process_step, and date_time**: This ensures that the data is ordered by the client's journey through the process, from their first visit to the confirmation step.

### Age Group Categorization:
- **Assign Age Groups**: Based on defined age bins, we categorize clients into age groups (e.g., under 30, 30-39, 40-49, 50+). This categorization is applied to the `df_merged`, as well as to the `control` and `test` datasets to facilitate age-based analysis.

## Who Are Our Clients?
For demographic analysis, we worked with a pool of **70,591 users** after applying the cleaning and merging processes to ensure data quality.

### Group with highest average tenure and balance:
- **Gender**: Male
- **Age Group**: 50 and above
- **Client's Tenure**: 16.35 years
- **Balance**: 294,239.72$

### Average Persona:
- **Gender**: Male
- **Age Group**: 30-39
- **Average Tenure**: 11.65 years
- **Average Balance**: 126,284.41$

## Further Observations
- Males generally have higher average balances than females, with the highest balances observed in the "50 and above" age group for both genders.
- Both males and females show similar tenure patterns, with longer tenures seen in older age groups (50+ years), indicating long-term clients.
- The “Unknown" gender category typically has lower average balances, likely due to potential data gaps or non-disclosure of gender.

## Key Performance Indicators (KPI's)
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

- **Bounce Rates**  
If the **Test group** has a lower bounce rate compared to the **Control group**, it suggests that the new design is better at keeping users engaged throughout the process. A lower bounce rate would indicate that users are more likely to stay in the process, reducing drop-offs or exits at any given step, which is a good indicator of user retention and interest.

---

## **Tableau Visuals**  
You can explore the interactive Tableau dashboard for further insights into the data and visualizations by following the link below:

[**Vanguard CX Story**](https://public.tableau.com/app/profile/eliska.simova/viz/Vanguard_CX/Vanguard_story?publish=yes)

---

## **Hypothesis Testing**

### Hypothesis 1: Completion Rate Comparison  
**Hypothesis**: "Is there a significant difference in the completion rates between the Control group and the Test group at each step of the process?"

- All steps show statistically significant differences in completion rates between the **Test group** (new UI) and **Control group** (old UI).
- A **p-value of 0.0000** for each step indicates strong evidence against the null hypothesis.
- We **reject the null hypothesis** at all steps, meaning that the new design does indeed have a significantly different impact on user completion rates at each step compared to the old design.

### Hypothesis 2: Completion Rate Increase  
**Hypothesis**: "Does the introduction of the new UI design result in a minimum 5% increase in the completion rate compared to the existing design, making it cost-effective?"

- The completion rate increase of **9.82%** between the **Test** and **Control** groups exceeds the **5%** threshold set by Vanguard.
- The **new UI design** could be considered **worthwhile from a business perspective** due to this significant increase in the completion rate.

### Hypothesis 3: Average Client Tenure Comparison  
**Hypothesis**: "Is the average client tenure of those engaging with the new process the same as those engaging with the old process?"

- **Control Group Average Tenure**: 12.09 years
- **Test Group Average Tenure**: 11.98 years
- **p-value**: 0.0868, **Statistic**: 1.7124 (indicates how much the means differ relative to variability)
- We **fail to reject the null hypothesis**, meaning the **average tenure is not significantly different** between the two groups.
- The lack of significant difference in **average tenure** supports the validity of the A/B test results.

### Hypothesis 4: Average Client Age Comparison  
**Hypothesis**: "Is the average client age of those engaging with the new process the same as those engaging with the old process?"

- **Control Average Age**: 47.50 years
- **Test Average Age**: 47.16 years
- **p-value**: 0.0160
- Since the **p-value is less than 0.05**, we **reject the null hypothesis**, indicating that there is a **statistical difference** in the average age between the Test and Control groups.

### Hypothesis 5: Error Rate Comparison  
**Hypothesis**: "Does the new UI design lead to a reduction in error rates compared to the old design, and is this reduction statistically significant?"

- **Control Error Rate**: 19.21%
- **Test Error Rate**: 17.64%
- **Percentage Difference**: 1.57%
- **p-value**: 0.0000
- We **reject the null hypothesis** that there is no difference between the groups, indicating that the **new UI** has a **significantly lower error rate** than the old UI.

### Hypothesis 6: Bounce Rate Comparison  
**Hypothesis**: “Is the bounce rate of the Test group lower than the Control group across all steps?”

- The **Test group** showed a **statistically significant lower bounce rate** only at **Step 1**.
- For **Steps 0**, **2**, and **3**, there were **no statistically significant differences** between the Control and Test groups.

---
# **Dataset**

There are three datasets that we were provided:

### 1. **Client Profiles (df_final_demo)**  
This dataset contains demographic information about our clients, including:

- **Age**
- **Gender**
- **Account details** (e.g., account type, account balance, etc.)

This dataset provides valuable context for understanding client characteristics and can be used to segment clients for analysis or identify patterns in behavior.

### 2. **Digital Footprints (df_final_web_data)**  
This dataset provides a detailed trace of client interactions online, including:

- **pt_1**: The first part of the data, which likely captures initial interactions with the platform.
- **pt_2**: The second part of the data, which includes additional details of the user’s interactions.

It is recommended to **merge these two parts** (pt_1 and pt_2) before conducting any comprehensive data analysis. Merging these datasets will give a complete view of the client's online activity and interactions with the platform.

### 3. **Experiment Roster (df_final_experiment_clients)**  
This dataset contains a list of the clients who participated in the grand experiment, including details such as:

- **Client IDs**
- **Group assignment** (Test or Control group)
- **Participation dates**

This dataset is crucial for linking client demographics and behavior to the experiment results, ensuring that we correctly associate clients with their respective experimental conditions.

## **Main Dataset Issues**

The datasets provided for analysis did not have many missing values, which made the initial steps of cleaning and preparation relatively straightforward. However, there were some notable issues that needed to be addressed before proceeding with any in-depth analysis:

### 1. **Formatting Issues**
   - **Inconsistent column names**: Several columns had different naming conventions or were not aligned across the different datasets. For example, some columns had underscores while others used camelCase, making it necessary to standardize the column names.
   - **Date/Time formatting**: Some datasets had **date** or **timestamp** columns in different formats. Ensuring consistency in the **date_time** field (e.g., converting them all to a datetime format) was essential for performing time-based analyses and comparisons.
   - **Categorical data encoding**: There were also inconsistencies in categorical data, such as the **gender** field, where some rows had 'X' as a placeholder for missing data. These were removed or corrected as part of the cleaning process.

### 2. **Merging Datasets**
   - **Merging the datasets**: While merging the datasets (Client Profiles, Digital Footprints, and Experiment Roster) was a relatively easy task due to well-defined unique identifiers like **client_id**, it required careful attention to ensure that records from different sources aligned correctly.
   - **Handling duplicates**: A small number of duplicate rows were found during the merging process, mostly in the **Digital Footprints** dataset, where clients had multiple entries for the same session. These were handled by deduplicating the records based on session ID and timestamps.
   - **Time-based alignment**: Merging the **Digital Footprints** (pt_1 and pt_2) required aligning timestamps across the two parts of the dataset, ensuring that the interactions were in chronological order. This was relatively simple given that both parts shared a common identifier.

### 3. **Other Considerations**
   - **Age group categorization**: For better analysis and comparison, **age** data was divided into groups (e.g., under 30, 30-39, 40-49, 50+), which required the creation of custom bins to segment clients into meaningful categories.
   - **Test/Control Group Assignment**: It was important to ensure that the **Experiment Roster** was properly mapped to the **Client Profiles** and **Digital Footprints** to make sure that we correctly identified which clients were assigned to the test group (new UI) and which were in the control group (old UI). 

While these issues were relatively minor and manageable, they still required careful attention to ensure the datasets were clean, merged correctly, and ready for analysis.

---

## **Experiment Evaluation**  
- **Average Ages**: The average age is statistically different between the Test and Control groups, as indicated by the **p-value of 0.0160**, which is less than the **0.05 threshold**.
- This means the distribution of **ages** between the two groups is **not uniform**, and age differences could potentially introduce a **bias in the observed completion rate**.

---

## **_Recommendations_**

### 1. **Simplify the Process**  
All age groups may benefit from a more straightforward flow.

💡 **Reduce unnecessary steps and minimize user decisions to streamline the experience**.

### 2. **Provide Contextual Help**  
High bounce rates may suggest confusion or hesitation; users might benefit from guidance or support.

💡 **Add tooltips, help icons, and live support to guide users**.

### 3. **Improve Visual Design**  
Bounce rates at certain steps suggest that users might find some of the content unclear.

💡 **Ensure readability and consistency in font size, contrast, and button design**.

### 4. **Personalize Experience**  
Users might lose track of where they are in the process or forget to complete it.

💡 **Offer reminders and allow users to save their progress for later completion**.

---

## **Slides**

The presentation summarizing the key findings, analysis, and recommendations from the experiment can be found at the following link:

[**Vanguard UI Experiment Presentation on Canva**](https://www.canva.com/design/DAGW14YnvRA/iUNuG-K4g5jfRtQ90P658A/edit)

Additionally, the presentation slides are available in the **Slides folder** for easy access.

The slides provide an overview of the experiment setup, hypothesis testing, key results, and actionable recommendations based on the A/B test comparing the traditional UI (Control group) with the new UI (Test group). They are designed to help stakeholders quickly grasp the main insights and decisions derived from the data analysis.

Feel free to review the slides for further details, including visualizations, statistical tests, and recommendations for next steps.

---

## **Organization Materials**

To facilitate collaboration and ensure smooth execution throughout the project, several organizational tools and resources were used:

- **Project Structure Preview**: We started by outlining the structure of the project in a Google Doc to ensure alignment on goals and tasks.
  - [**Google Doc - Project Structure Preview**](https://docs.google.com/document/d/1RWtetDbxPTHrrh62swZrF2_VPFs23U0dYrxwRwlTH9I/edit?tab=t.0)

- **Kanban Board**: As the project progressed, we used a Trello board to track tasks, milestones, and progress. This helped maintain clear visibility on individual and group responsibilities.
  - [**Trello - Kanban Board**](https://trello.com/b/UocZX25f/kanban-template)

- **Collaboration and Communication**: We held regular check-ins and point-of-work meetings to share progress, review work, and identify any challenges. Whenever we encountered roadblocks, we either sought assistance from team members or conducted independent and group research to resolve issues.
  
These tools helped streamline the workflow and fostered collaboration across different stages of the project.

---

## **Streamlit App**

The development of the **Streamlit app** went through several iterations, organizational changes, and challenges before we arrived at the current structure. These iterations were necessary due to the complexity of the data and the dynamic nature of the A/B test results we were working with.

### **Development Challenges**
- **Initial Designs**: The first versions of the app were simple, but we quickly encountered limitations in scalability and functionality. As the complexity of the experiment grew, it became clear that the app would need more structured navigation and interactive features to accommodate a range of analysis.
- **Reorganization**: The app structure underwent several revisions, adjusting both the layout and the organization of different pages to better serve the data visualization needs. This process was iterative and required refining of how the data would be presented to users.
- **Technical Issues**: During development, there were multiple technical hurdles related to performance, data loading, and the integration of different components. These issues required debugging and adapting the code to ensure smooth user interactions, particularly for large datasets.
- **Complexity of Implementation**: As new features were added (such as hypothesis testing, demographic analysis, and error rate tracking), it became increasingly complex to implement and maintain the app. Despite these challenges, the final iteration provides a more robust and dynamic user experience.

### **App Structure**

The app is now organized as follows:

- **Main Script**: 
  - `app.py`: The entry point to the app, handling navigation and page routing.
  
- **Pages**: Each page focuses on a specific analysis or dataset, and includes interactive visualizations.
  - `about.py`: Overview of the project and its objectives.
  - `summary.py`: Summary of the dataset used in the experiment.
  - `unique_values.py`: Exploration of unique values in key columns.
  - `stats.py`: Basic statistics of the experiment data.
  - `demographics.py`: Analysis of user demographics.
  - `duration.py`: Page dedicated to analyzing the duration of user interactions.
  - `hypothesis.py`: Displays results of hypothesis testing.
  - `completion.py`: Examines completion times for tasks.
  - `bounce_rate.py`: Visualizes and analyzes bounce rates.
  - `error_rate.py`: Presents error rates and analysis of issues encountered.

- **Utility Functions**:
  - `utils_`: A folder containing helper functions, such as `display.py`, for rendering data and visualizations across pages.

### **Interactive Features**
Despite the challenges, the final version of the app provides a dynamic and interactive interface. Users can explore different aspects of the A/B test, including key metrics, statistical results, and demographic insights, in real-time. The interactive visualizations help stakeholders make data-driven decisions by allowing them to engage directly with the results.

- [**Vanguard UI Experiment - Streamlit App**](#) *(Insert actual link to the deployed app)*

This app complements the presentation slides by offering a more hands-on, engaging experience for exploring the data and results.
