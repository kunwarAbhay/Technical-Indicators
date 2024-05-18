def calculate_rsi(data, column="Close", period=14):
    """
    Calculate the Relative Strength Index (RSI) for a given dataset.

    Parameters:
    data (DataFrame): 'OHLC' stock data.
    column (str): The name of the column containing the prices (default is "Close").
    period (int): The number of periods to use for the RSI calculation (default is 14).
    """

    # Calculate price changes
    delta = data[column].diff()

    # Calculate gains (positive changes) and losses (negative changes)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    # Calculate average gain and loss
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    # Calculate the Relative Strength (RS)
    rs = avg_gain / avg_loss

    # Calculate the RSI
    data['RSI'] = 100 - (100 / (1 + rs))

    return data
