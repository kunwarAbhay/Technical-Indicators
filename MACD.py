def calculate_macd(data, column="Close", short_period=12, long_period=26, signal_period=9):
    """
    Calculate the MACD, Signal Line, and MACD Histogram.

    Parameters:
    data (DataFrame): 'OHLC' stock data.
    column (str): The name of the column containing the prices (default is "Close").
    short_period (int): The period for the short-term EMA (default is 12).
    long_period (int): The period for the long-term EMA (default is 26).
    signal_period (int): The period for the signal line EMA (default is 9).
    """
    # Calculate the short-term and long-term EMAs
    ema_short = data[column].ewm(span=short_period, adjust=False).mean()
    ema_long = data[column].ewm(span=long_period, adjust=False).mean()

    # Calculate the MACD Line
    macd_line = ema_short - ema_long

    # Calculate the Signal Line (EMA of MACD Line)
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()

    # Calculate the MACD Histogram
    macd_histogram = macd_line - signal_line

    data['MACD_Line'] = macd_line
    data['Signal_Line'] = signal_line
    data['MACD_Histogram'] = macd_histogram

    return data
