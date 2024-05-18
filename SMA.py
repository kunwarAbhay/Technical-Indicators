def calculate_sma(data, column="Close", period=20):
    """
    Calculate the Simple Moving Average (SMA) for a given dataset.

    Parameters:
    data (DataFrame): 'OHLC' stock data.
    column (str): The name of the column containing the prices (Default is "Close").
    period (int): The number of periods to use for the moving average (default is 20).
    """
    # Calculate the Simple Moving Average (SMA)
    sma = data[column].rolling(window=period).mean()

    data[f'SMA_{period}'] = sma

    return data
