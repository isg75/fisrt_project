import pandas as pd
import seaborn as sns
import yfinance as yf

def normalize(df):
    """
    Normalizes a DataFrame by adjusting index and column naming conventions.
    
    The function performs the following transformations:
      - Converts the index name to lowercase.
      - Drops the second level of the column MultiIndex, if present.
      - Strips whitespace from column names.
      - Converts column names to lowercase.
      - Replaces spaces in column names with underscores.
      
    Parameters:
        df (pd.DataFrame): The DataFrame to normalize.
        
    Returns:
        pd.DataFrame: A new DataFrame with normalized column and index names.
    """

    result_df = df.copy()

    # Normalize index name
    if result_df.index.name is not None:
        result_df.index.name = result_df.index.name.lower()

    # Drop the second level in the column MultiIndex if it exists
    if isinstance(result_df.columns, pd.MultiIndex) and result_df.columns.nlevels > 1:
        result_df.columns = result_df.columns.droplevel(1)

    # Normalize column names
    result_df.columns = result_df.columns.str.strip()
    result_df.columns = result_df.columns.str.lower()
    result_df.columns = result_df.columns.str.replace(' ', '_', regex=False)

    # Normalize column index name, if it exists
    if result_df.columns.name is not None:
        result_df.columns.name = result_df.columns.name.lower()

    return result_df

def plot(data, labels, events=[], export_path=None):
    """
    Plots a time series data with optional event markers and export functionality.
    
    Parameters:
        data (pd.Series): The time series data to plot (e.g., closing prices).
        labels (tuple): A tuple containing two strings: 
                        - labels[0]: The label for the x-axis (typically "Date").
                        - labels[1]: The label for the y-axis (e.g., "Closing Price ($)").
        events (list of dicts, optional): List of events to mark on the plot. 
                                           Each event should be a dictionary with:
                                           - "name" (str): Event label (e.g., "COVID").
                                           - "date" (datetime): Date of the event.
        export_path (str, optional): File path to save the plot as an image. If provided,
                                     the plot will be saved at this location.
                                     
    Returns:
        None. Displays the plot and optionally saves it if export_path is provided.
    """

    # Plot graph from input data and labels
    ax = data.plot(figsize=(12, 6), label=labels[1])
    
    # Draw event markers
    for event in events:
        ax.axvline(event["date"], color="red", linestyle="--", linewidth=0.8)
        ax.text(event["date"] + pd.Timedelta(days=10), data.max(), event["name"], color="red", ha="left", va="top")

    # Set additional plot information
    ax.set_title(labels[1])
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.legend()

    # Save plot to file, if provided
    if export_path:
        ax.get_figure().savefig(export_path)

def plot_ticker(ticker, series, date_range, events=[]):
    """
    Fetches historical stock data for a specified ticker and date range, normalizes the data,
    and plots a specified series with optional event markers.
    
    Parameters:
        ticker (str): The stock ticker symbol (e.g., "AAPL" for Apple).
        series (str): The name of the data series to plot, must be one of the following:
                      - "adj_close": Adjusted closing price
                      - "close": Closing price
                      - "high": Highest price during the day
                      - "low": Lowest price during the day
                      - "open": Opening price
                      - "volume": Trading volume
        date_range (tuple of datetime): A tuple with two datetime objects representing 
                                        the start and end dates (start, end) for the data.
        events (list of dicts, optional): List of events to mark on the plot. 
                                          Each event should be a dictionary with:
                                          - "name" (str): Event label (e.g., "COVID").
                                          - "date" (datetime): Date of the event.
                                          
    Returns:
        None. Calls the `plot` function to display the specified series from the historical
        stock data with event markers.
    """

    # Download ticker data from Yahoo! Finance
    start, end = date_range
    df = yf.download(ticker, start=date_range[0], end=date_range[1], progress=False)

    # Normalize fetched DataFrame
    df = normalize(df)

    # Plot specific series or list of series from DataFrame
    plot(df[series], (df.index.name, series), events)
