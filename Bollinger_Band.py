def calculate_bollinger_bands(data, column="Close", period=20, num_std_dev=2):
    """
    Calculate the Bollinger Bands for a given dataset.

    Parameters:
    data (DataFrame): 'OHLC' stock data.
    column (str): The name of the column containing the prices (default is "Close").
    period (int): The number of periods to use for the moving average and standard deviation (default is 20).
    num_std_dev (float): The number of standard deviations to use for the bands (default is 2).
    """
    # Calculate the Simple Moving Average (SMA)
    sma = data[column].rolling(window=period).mean()

    # Calculate the rolling standard deviation
    std_dev = data[column].rolling(window=period).std()

    # Calculate the Upper and Lower Bands
    upper_band = sma + (num_std_dev * std_dev)
    lower_band = sma - (num_std_dev * std_dev)

    data[f'upper_band_{period}'] = upper_band
    data[f'middle_band_{period}'] = sma
    data[f'lower_band_{period}'] = lower_band

    return data
