# pages/unique_values.py
import streamlit as st
import pandas as pd
from data_loader import load_data

def show_unique_values_in_categorical_columns(df):
    st.title("Unique Values in Categorical Columns")
    
    # Get all categorical columns
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns.tolist()
    
    # Check if there are any categorical columns
    if not categorical_columns:
        st.warning("No categorical columns found in the file.")
        return

    st.subheader("Unique Values in Categorical Columns:")
    for column in categorical_columns:
        # Get unique values for each categorical column
        unique_values = df[column].unique()
        st.write(f"Column: {column}")
        st.write(f"Unique values: {unique_values}")