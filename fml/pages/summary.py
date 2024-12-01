# pages/summary.py
import streamlit as st
import pandas as pd
from data_loader import load_data

def show_data_summary(df):
    st.subheader("CSV Data Overview")
    st.write(f"Number of rows: {df.shape[0]}")
    st.write(f"Number of columns: {df.shape[1]}")
    st.write("First 5 rows of the dataset:")
    st.dataframe(df.head())

# Assuming you're loading your data in the main part of the app or another script
if __name__ == "__main__":
    # Example: loading a CSV file
    # Change the path below to your actual file location
    df = pd.read_csv("path_to_your_data.csv")  # Load data from CSV

    # Now call the function and pass the DataFrame `df`
    show_data_summary(df)