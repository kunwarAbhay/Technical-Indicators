def calculate_pivot_points(data):
    """
    Calculate pivot points and support/resistance levels.

    Parameters:
    data (DataFrame): 'OHLC' stock data.
    """

    # Calculate pivot point
    pivot = (data['High'] + data['Low'] + data['Close']) / 3

    # Calculate support and resistance levels
    R1 = 2 * pivot - data['Low']
    S1 = 2 * pivot - data['High']
    R2 = pivot + (data['High'] - data['Low'])
    S2 = pivot - (data['High'] - data['Low'])
    R3 = data['High'] + 2 * (pivot - data['Low'])
    S3 = data['Low'] - 2 * (data['High'] - pivot)

    data['pivot'] = pivot
    data['R1'] = R1
    data['S1'] = S1
    data['R2'] = R2
    data['S2'] = S2
    data['R3'] = R3
    data['S3'] = S3

    return data
