# 📊 AI Trading Risk & Prediction System

An end-to-end **Machine Learning + Data Science project** that predicts trade profitability and calculates a dynamic **risk score** using historical trading data and market sentiment.

---
## 🚀 Live Demo
👉 https://ai-trading-system-4255n5k8nfgsz4vfavcpp7.streamlit.app

---

## 🎯 Project Overview

This project builds an **AI-powered decision system** for traders.

It answers:
- Will this trade be profitable?
- How risky is this trade?
- Should I take this trade?

---

## 🧠 Key Features

✅ Profit Prediction using ML  
✅ Risk Score (0–100)  
✅ Market Sentiment Integration (Fear & Greed Index)  
✅ Feature Engineering (time, ratios, trade behavior)  
✅ Interactive Streamlit Web App  
✅ Visual Trade Analysis (charts)

---

## ⚙️ Tech Stack

- Python 🐍  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Matplotlib  
- Joblib  

---

## 📊 Machine Learning Pipeline

- Data Cleaning & Preprocessing  
- Feature Engineering  
- Handling categorical + numerical data  
- Model: Random Forest Classifier  
- Pipeline: ColumnTransformer + Encoding + Scaling  

---

## 📈 Features Used

- Trade Size & Price  
- Fee Ratio  
- Time Features (hour, day)  
- Previous Trade Performance  
- Rolling Profit Trends  
- Market Sentiment  

---

## ⚠️ Risk Scoring Logic

The system combines:

- Model prediction probability  
- Trade size impact  
- Fee impact  
- Market emotion (Fear vs Greed)  

Final output:

Risk Score (0–100)


---

## 🌐 Streamlit Web App

The app allows users to:

- Input trade details  
- Get instant prediction  
- View risk score  
- Visualize trade vs market  

---

## 📊 Sample Output

- Profit Probability: 64%  
- Risk Score: 52  
- Decision: Medium Risk  

---

## 📁 Project Structure


project/
│
├── src/
│ ├── preprocessing.py
│ ├── features.py
│ ├── model.py
│
├── data/
├── models/
│ └── model.pkl
│
├── app.py
├── risk.py
├── main.py
├── requirements.txt
└── README.md


---

## ▶️ How to Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Train model
python main.py
3. Run app
python -m streamlit run app.py
🚀 Deployment

This project is deployed using Streamlit Cloud.

💡 Future Improvements
Add real-time market data
Advanced models (XGBoost, Deep Learning)
Explainability (SHAP)
Portfolio-level risk analysis
Backtesting engine
🙋‍♂️ Author

Developed by KIRAN A N

⭐ If you like this project

Give it a ⭐ on GitHub and share!


---

# 🎯 HOW TO ADD

1. Go to your GitHub repo  
2. Click **Add file → Create new file**  
3. Name it:

```text
README.md
Paste above code
Commit
