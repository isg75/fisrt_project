#Neccessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# clean df_final_demo
def clean_df_final_demo():
    #key fields client_id, clnt_age, gender, num_accts, balance, clnt_tenure_yr
    df_copy = pd.read_csv("df_final_demo.txt")
    df_copy = df_copy.dropna()
    corrected_columns = {"gendr" : "gender", "bal" : "balance"}
    df_copy.rename(columns=corrected_columns, inplace = True)
    df_copy = df_copy[df_copy['gender'] != 'X']    
    gender_mapping = {
    'M': 'Male',
    'F': 'Female',
    'U': 'Unknown',
    }
    df_copy['gender'] = df_copy['gender'].map(gender_mapping)
    return df_copy

#df_1 = clean_df_final_demo()

# clean df_experiment_clients
def clean_df_experiment_clients():
    df_copy = pd.read_csv("df_final_experiment_clients.txt")
    df_copy = df_copy.dropna() # dropping the NaN values
    df_copy.rename(columns={'Variation': 'variation'}, inplace=True)
    return df_copy
