import pandas as pd

def load_data():
    sentiment = pd.read_csv("data/fear_greed_index (1).csv")
    trades = pd.read_csv("data/historical_data (1).csv")

    # Clean column names
    sentiment.columns = sentiment.columns.str.strip().str.lower().str.replace(" ", "")
    trades.columns = trades.columns.str.strip().str.lower().str.replace(" ", "")

    # Convert dates
    sentiment['date'] = pd.to_datetime(sentiment['date'], errors='coerce').dt.date

    trades['timestampist'] = pd.to_datetime(
        trades['timestampist'], dayfirst=True, errors='coerce'
    )
    trades['date'] = trades['timestampist'].dt.date

    # Merge
    df = pd.merge(trades, sentiment, on='date', how='left')

    # Drop nulls
    df = df.dropna().reset_index(drop=True)

    return df