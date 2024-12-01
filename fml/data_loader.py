# data_loader.py
import pandas as pd
import streamlit as st

def load_data(file_path):
    """
    Load and return the data from the given file path.
    Also, calculate any derived columns like `completion` and `age_group`.
    """
    try:
        # Load data from the specified CSV file
        df = pd.read_csv('https://raw.githubusercontent.com/simovaeliska/second_project/refs/heads/main/data/clean/combined_cleaned_data1.csv')
        
        # Ensure 'completion' column is calculated if not present
        if 'completion' not in df.columns:
            df['completion'] = df['process_step'].apply(lambda x: 1 if x in ['confirm', 'completed'] else 0)
        
        # Age categorization (if not already done)
        if 'age_group' not in df.columns:
            bins = [0, 30, 40, 50, 100] 
            labels = ['Under 30', '30-39', '40-49', '50 and above']
            df['age_group'] = pd.cut(df['clnt_age'], bins=bins, labels=labels)

        return df
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None