import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
from risk import calculate_risk

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(page_title="AI Trading System", layout="wide")

# -----------------------
# LOAD MODEL
# -----------------------
model = joblib.load("models/model.pkl")

# -----------------------
# TITLE
# -----------------------
st.title("📊 AI Trading Risk & Prediction System")
st.markdown("Analyze trade decisions using machine learning and market sentiment")

st.divider()

# -----------------------
# INPUT SECTION
# -----------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Trade Input")

    size = st.number_input("Trade Size (USD)", value=1000)
    price = st.number_input("Execution Price", value=30000)
    fee = st.number_input("Fee", value=10)

    side = st.selectbox("Side", ["BUY", "SELL"])
    direction = st.selectbox("Direction", ["LONG", "SHORT"])
    emotion = st.selectbox("Market Emotion", ["Fear", "Greed"])

with col2:
    st.subheader("📊 Instructions")
    st.info(
        "Enter trade details and click **Analyze Trade** to see prediction and risk."
    )

st.divider()

# -----------------------
# BUTTON
# -----------------------
if st.button("🚀 Analyze Trade"):

    # -----------------------
    # CREATE INPUT DATA
    # -----------------------
    df = pd.DataFrame([{
        'sizeusd': size,
        'executionprice': price,
        'fee': fee,
        'side': side,
        'direction': direction,
        'classification': emotion,
        'timestampist': pd.Timestamp.now()
    }])

    # -----------------------
    # FEATURE ENGINEERING
    # -----------------------
    df['size_price_ratio'] = df['sizeusd'] / (df['executionprice'] + 1)
    df['fee_ratio'] = df['fee'] / (df['sizeusd'] + 1)

    df['hour'] = pd.to_datetime(df['timestampist']).dt.hour
    df['day'] = pd.to_datetime(df['timestampist']).dt.dayofweek

    df['prev_pnl'] = 0
    df['rolling_pnl'] = 0

    # -----------------------
    # PREDICT
    # -----------------------
    risk_score, prob = calculate_risk(df, model)

    # -----------------------
    # RESULTS
    # -----------------------
    st.divider()
    st.subheader("🔮 Analysis Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Profit Probability", f"{round(prob[0]*100, 2)}%")

    with col2:
        st.metric("Risk Score", f"{round(risk_score[0], 2)} / 100")

    # Risk bar
    st.progress(min(int(risk_score[0]) / 100, 1.0))

    # Decision
    if risk_score[0] < 30:
        st.success("✅ Low Risk → Good Trade")
    elif risk_score[0] < 60:
        st.warning("⚠️ Medium Risk → Be Careful")
    else:
        st.error("❌ High Risk → Avoid Trade")

    # -----------------------
    # CHART SECTION
    # -----------------------
    st.subheader("📊 Trade Position vs Market")

    # Simulated historical data
    sample_size = 200
    historical_prob = np.random.uniform(0.2, 0.9, sample_size)
    historical_risk = (1 - historical_prob) * 100 + np.random.normal(0, 5, sample_size)

    fig, ax = plt.subplots()

    # Historical points
    ax.scatter(historical_prob, historical_risk)

    # Current trade point
    ax.scatter(prob[0], risk_score[0], marker='X')

    ax.set_xlabel("Profit Probability")
    ax.set_ylabel("Risk Score")
    ax.set_title("Your Trade vs Market Trades")

    st.pyplot(fig)

    # -----------------------
    # INSIGHT
    # -----------------------
    st.subheader("💡 Insight")

    if prob[0] > 0.6 and risk_score[0] < 50:
        st.success("📈 Strong position — good probability with controlled risk")
    elif prob[0] < 0.5 and risk_score[0] > 60:
        st.error("📉 Weak trade — low probability and high risk")
    else:
        st.warning("⚖️ Balanced trade — moderate outcome expected")

    if emotion == "Greed":
        st.write("⚠️ Market shows **Greed** — higher chance of risky trades.")
    else:
        st.write("😨 Market shows **Fear** — safer but slower growth.")