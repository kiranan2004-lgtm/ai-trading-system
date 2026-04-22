# 📊 AI-Powered Trading Risk & Decision System

## 🚀 Overview

This project builds an end-to-end **machine learning system** to analyze trader behavior using market sentiment (Fear vs Greed) and predict the **probability of trade profitability**.

It goes beyond simple prediction by providing a **risk scoring system and decision support tool** that helps traders evaluate whether to take or avoid a trade.

---

## 🎯 Problem Statement

Financial markets are highly influenced by **human emotions**, especially fear and greed. Traders often make irrational decisions during extreme market conditions, leading to losses.

This project aims to:

* Understand how **market sentiment impacts trading outcomes**
* Predict whether a trade will result in **profit or loss**
* Provide a **risk score** for better decision-making

---

## 🧠 Solution Approach

### 1. Data Processing

* Cleaned and standardized multiple datasets
* Merged **trading data** with **market sentiment data**
* Handled missing values and inconsistencies

---

### 2. Feature Engineering

Created meaningful features such as:

* Trade size ratios
* Fee impact ratios
* Time-based features (hour, day)
* Behavioral indicators (large trade, high fee)

---

### 3. Machine Learning Model

* Model: **Random Forest Classifier**
* Predicts: **Probability of profit (not just yes/no)**
* Handles both numerical and categorical features using pipelines

---

### 4. Risk Scoring System 🔥

A custom **risk score (0–100)** is calculated using:

* Model prediction (most important)
* Trade size (risk exposure)
* Transaction fee impact
* Market sentiment (fear/greed)

---

### 5. Backtesting Strategy

Simulated trading strategy:

* Take trades only when probability > threshold
* Evaluated:

  * Total profit
  * Win rate
  * Trade frequency

---

### 6. Interactive Web App

Built using **Streamlit**:

* Input trade parameters
* Get:

  * Profit probability
  * Risk score
  * Trade recommendation (Low/Medium/High Risk)

---

## 🏗️ Project Structure

```
AI-Trading-System/
│
├── data/                # Raw datasets
├── notebooks/           # Analysis & exploration
├── src/                 # Core logic
│   ├── preprocessing.py
│   ├── features.py
│   ├── model.py
│   ├── risk.py
│   ├── backtest.py
│
├── models/              # Saved ML model
├── app.py               # Streamlit app
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Streamlit
* Joblib

---

## 📊 Key Features

* 📈 Profit prediction model
* ⚠️ Risk scoring system
* 🧪 Backtesting engine
* 🧠 Behavior analysis (Fear vs Greed)
* 🌐 Interactive UI (Streamlit app)

---

## 📈 Results & Insights

* Market sentiment significantly impacts trading outcomes
* Higher trade sizes and fees increase risk
* Traders tend to take riskier decisions during **greed phases**
* Model enables **probability-based decision making**, improving trade selection

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Train model

```
python src/model.py
```

### 3. Run app

```
streamlit run app.py
```

---

## 🔮 Future Improvements

* Add advanced models (XGBoost, LightGBM)
* Deploy as a web application
* Integrate real-time market data
* Add explainability using SHAP
* Improve backtesting with realistic trading strategies

---

## 💡 Key Learning Outcomes

* End-to-end ML pipeline development
* Feature engineering for financial data
* Risk modeling and decision systems
* Building deployable data science applications

---

## 👨‍💻 Author

**Kiran**

---

## ⭐ If you like this project

Give it a star on GitHub and feel free to connect!
