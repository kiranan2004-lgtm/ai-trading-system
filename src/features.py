import pandas as pd

def create_features(df):

    # Target (only for training)
    df['target'] = (df['closedpnl'] > 0).astype(int)

    # Features
    df['size_price_ratio'] = df['sizeusd'] / (df['executionprice'] + 1)
    df['fee_ratio'] = df['fee'] / (df['sizeusd'] + 1)

    df['hour'] = pd.to_datetime(df['timestampist']).dt.hour
    df['day'] = pd.to_datetime(df['timestampist']).dt.dayofweek

    df['prev_pnl'] = df['closedpnl'].shift(1)
    df['rolling_pnl'] = df['closedpnl'].rolling(5).mean()

    df = df.dropna().reset_index(drop=True)

    return df