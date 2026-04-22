def calculate_metrics(df):

    returns = df['closed pnl']

    sharpe = returns.mean() / returns.std()

    cum = returns.cumsum()
    drawdown = cum - cum.cummax()

    return sharpe, drawdown.min()