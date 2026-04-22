import pandas as pd
import joblib
from risk import calculate_risk

# ================================
# 1. LOAD MODEL
# ================================
model = joblib.load("models/model.pkl")

print("✅ Model loaded successfully")

# ================================
# 2. CREATE NEW TRADE INPUT
# ================================
new_trade = pd.DataFrame([{
    'size usd': 1000,
    'execution price': 30000,
    'fee': 10,
    'side': 'BUY',
    'direction': 'LONG',
    'classification': 'Greed',
    'timestamp ist': pd.Timestamp.now()
}])

# ================================
# 3. FEATURE ENGINEERING (IMPORTANT)
# ================================

# Ratios
new_trade['size_price_ratio'] = new_trade['size usd'] / (new_trade['execution price'] + 1)
new_trade['fee_ratio'] = new_trade['fee'] / (new_trade['size usd'] + 1)

# Time features
new_trade['hour'] = pd.to_datetime(new_trade['timestamp ist']).dt.hour
new_trade['day'] = pd.to_datetime(new_trade['timestamp ist']).dt.dayofweek

# Lag features (dummy values for now)
new_trade['prev_pnl'] = 0
new_trade['rolling_pnl'] = 0

# ================================
# 4. PREDICT + RISK
# ================================
risk_score, prob = calculate_risk(new_trade, model)

# ================================
# 5. OUTPUT RESULT
# ================================
print("\n🔮 Trade Analysis")
print("-----------------------------")
print("Profit Probability:", round(prob[0], 2))
print("Risk Score:", round(risk_score[0], 2))

# Decision logic
if risk_score[0] < 30:
    print("✅ Low Risk → Good Trade")
elif risk_score[0] < 60:
    print("⚠️ Medium Risk → Be Careful")
else:
    print("❌ High Risk → Avoid Trade")