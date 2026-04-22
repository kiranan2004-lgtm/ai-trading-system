def backtest(df, model, threshold=0.6):

    probs = model.predict_proba(df)[:, 1]

    df['prob'] = probs
    df['take_trade'] = df['prob'] > threshold

    strategy = df[df['take_trade']]

    total_profit = strategy['closed pnl'].sum()
    win_rate = (strategy['closed pnl'] > 0).mean()

    return total_profit, win_rate