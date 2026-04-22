def calculate_risk(df, model):

    prob = model.predict_proba(df)[:, 1]

    model_risk = (1 - prob) * 100
    size_risk = df['sizeusd'] / 10000 * 100
    fee_risk = df['fee'] / (df['sizeusd'] + 1) * 100

    emotion_risk = df['classification'].apply(
        lambda x: 70 if str(x).lower() == 'greed' else 40
    )

    risk_score = (
        0.5 * model_risk +
        0.2 * size_risk +
        0.2 * fee_risk +
        0.1 * emotion_risk
    )

    return risk_score, prob