# pages/stats.py
import streamlit as st
import pandas as pd
from data_loader import load_data

def show_basic_statistics(df):
    # Select only numeric columns
    numeric_df = df.select_dtypes(include=['number'])

    # Check if there are numeric columns
    if numeric_df.empty:
        st.warning("No numeric columns found in the file.")
        return
    
    # Display basic statistics for numeric columns
    st.subheader("Basic Statistics for Numeric Columns:")
    statistics = numeric_df.describe().T  # Transpose for better readability
    st.write(statistics)