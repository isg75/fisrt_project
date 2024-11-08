import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yaml

from functions import cleaning_productivity_data, describe_work_type_stats, plot_work_type_distribution, plot_stacked_work_and_overtime_hours, calculate_avg_median_scores_by_work_type, plot_average_scores_by_work_type, plot_scores_by_work_type, heat_map, df_mentalhealth_cleaning, satisfaction_mentalhealth, work_type_productivity, stress_worktype_rel, stress_jobrole_rel, descriptive_statistics_hours_worked

#opens yaml file
try:
    with open("../config.yaml") as file:
        config = yaml.safe_load(file)
except:
    print("Sorry, configuration file not found!")

#loads csv from yaml file directory
df = pd.read_csv(config['input_data']['productivity_file'])
df2 = pd.read_csv(config['input_data']['mental_health_file'])
df_cleaned = cleaning_productivity_data(df)
df2_cleaned = df_mentalhealth_cleaning(df2)
#saves csv to yaml file directory
df_cleaned.to_csv(config['output_data']['productivity_file'], index=False)
df2_cleaned.to_csv(config['output_data']['mental_health_file'], index=False)

describe_stats = describe_work_type_stats(df_cleaned)

'''
Interpretation of descriptive stats:
1)Age: mean age is very similar, between 40-41 years, the std is also similar aross the work types of 11 years. The interquartile range indicates employees fall between 30 to 50 years old which could suggest the data is based on more experienced IT professionals rather than junior or entry level.
2)Years at company: the average tenure across all work types ranges 4.38 - 4.48 years, the interquartile range is between 2 to 7 years, can be considered as relatively low turnover within the IT industry
3)Performance Score: The mean shows very similar variability across the work types with a very slight lower score for onsite workers. This can suggest that the work type doesn't impact employee productivity or performance.
4)Monthly salary: the mean salary is 6400 with similar ranges. This can be used to consider there is pay equality amongst the different work types.
5)Work hours per week: weekly average work hours are 45 across all groups which can indicate that the workloads are similar. We can assume all work types are just as productive.
6)Projects handled: are also very similar at 24 projects across all work types, this shows that the work type does not impact the employees to handle projects.
7)Overtime hours: we are asumming this is a monthly figure, the average is 14-15 hours across the work types with a wide spread of 0 to about 29 hours. Which can indicate a flexible work approach in the IT industry.
8)Sick days: the assumption is this is a yearly figure, the average number of sick days taken are 7. This can indicate that the work type does not influence health or attendance.
9)Training hours: shows an average of 48-50 across the work types with a high variablity from 0 to 99. We assume here that all work types have the same about of opportunity to training resources.
10)Promotions: are just under 1 across work types which might indicate that promotions are not frequent, however, with the remote work type having slightly less that 1 promotion might indicate less chance for promotion for remote workers.
11)Employee satisfaction score: the average score is approximately 3 out of 5 with the same std for all work types which indicate that work type does not impact job satisfaction.
12)Motivation score: average is around 3 out of 5 among all work types which suggests the different work environments have similar motivation
Conclusion:
Work type doesn’t show significant differences in productivity, satisfaction or motivation. We can infer if a company has a strong digital infrastructure and if they can provide equal access to resources, work environments do not matter.
'''

plot_work_type_distribution(df_cleaned, 'work_type')

plot_stacked_work_and_overtime_hours(df_cleaned)

pivot_avg_scores = calculate_avg_median_scores_by_work_type(df_cleaned)

plot_average_scores_by_work_type(df_cleaned, 'work_type')

plot_scores_by_work_type(df_cleaned)

heat_map(df_cleaned)


# Mental Health Dataset


df2_cleaned = df_mentalhealth_cleaning(df2)

satisfaction_mentalhealth(df2_cleaned)

work_type_productivity(df2_cleaned)

stress_worktype_rel(df2_cleaned)

stress_jobrole_rel(df2_cleaned)

descriptive_statistics_hours_worked(df2_cleaned)