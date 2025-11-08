# =========================================================
# ADVANCED SMART STOCK DASHBOARD APP (BY PRATHANMESH)
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(page_title="📊 Smart Stock Dashboard", layout="wide")
st.title("💹 Smart Stock Price Prediction & Trend Analyzer")
st.markdown("### 📈 Analyze 2-month stock trends, view predictions & investment suggestions instantly")

st.markdown("---")

# ======================
# LOAD SIMULATED DATASET
# ======================
@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range(end=pd.Timestamp.today(), periods=60)
    companies = ["TCS", "Infosys", "Reliance", "HDFC Bank", "Wipro",
                 "Adani Enterprises", "ICICI Bank", "HCL Tech"]

    data = []
    for company in companies:
        base = random.randint(500, 1500)
        high = np.round(base + np.random.randn(60).cumsum() * 2 + 20, 2)
        low = np.round(high - np.random.rand(60) * 30, 2)
        close = np.round((high + low) / 2 + np.random.rand(60) * 5, 2)
        volume = np.random.randint(1_00_000, 10_00_000, 60)
        for i in range(60):
            data.append([dates[i], company, high[i], low[i], close[i], volume[i]])

    df = pd.DataFrame(data, columns=["Date", "Company", "High", "Low", "Close", "Volume"])
    return df

df = load_data()

# ======================
# SIDEBAR USER INPUT
# ======================
st.sidebar.header("🧾 Select Stock Details")
companies = df["Company"].unique()
selected_company = st.sidebar.selectbox("Select Company", companies)
volume_held = st.sidebar.number_input("Enter Quantity (No. of Shares)", min_value=1, value=10)

analyze_btn = st.sidebar.button("🚀 Analyze Stock")

# ======================
# MAIN DASHBOARD
# ======================
if analyze_btn:
    company_data = df[df["Company"] == selected_company].reset_index(drop=True)

    # ---- Display Title
    st.markdown(f"## 📊 Last 2 Months Trend for **{selected_company}**")

    # ---- Line Chart
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(company_data["Date"], company_data["High"], label="High", color="green", linewidth=2)
    ax.plot(company_data["Date"], company_data["Low"], label="Low", color="red", linewidth=2)
    ax.plot(company_data["Date"], company_data["Close"], label="Close", color="blue", linestyle="--", linewidth=2)
    ax.fill_between(company_data["Date"], company_data["Low"], company_data["High"], color="lightblue", alpha=0.2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price (₹)")
    ax.set_title(f"{selected_company} - Stock Price Fluctuation (60 Days)")
    ax.legend()
    st.pyplot(fig)

    # ======================
    # PRICE PREDICTION & SUGGESTION
    # ======================
    st.markdown("### 💡 Price Prediction & Suggestion")

    latest_close = company_data["Close"].iloc[-1]
    trend_change = company_data["Close"].iloc[-5:].pct_change().mean() * 100
    predicted_price = latest_close * (1 + trend_change / 100)

    # Suggestion Logic
    if trend_change > 1.5:
        suggestion = "📈 **BUY** — Stock showing upward momentum"
        color = "green"
    elif trend_change < -1.5:
        suggestion = "📉 **SELL** — Stock trend declining"
        color = "red"
    else:
        suggestion = "⚖️ **HOLD** — Stable movement"
        color = "orange"

    st.markdown(f"**Current Price:** ₹{latest_close:.2f}")
    st.markdown(f"**Predicted Next Day Price:** ₹{predicted_price:.2f}")
    st.markdown(f"<h4 style='color:{color};'>{suggestion}</h4>", unsafe_allow_html=True)

    total_value = latest_close * volume_held
    st.success(f"💰 Your Holding Value: ₹{total_value:,.2f}")

    # ======================
    # SIMILAR STOCK PIE CHART
    # ======================
    st.markdown("### 🥧 Peer Stock Comparison")

    similar_df = df[df["Company"] != selected_company]
    similar_avg = similar_df.groupby("Company")["Close"].mean().sample(4)
    similar_avg[selected_company] = company_data["Close"].mean()

    fig2, ax2 = plt.subplots(figsize=(6, 6))
    colors = ["#1f77b4", "#2ca02c", "#ff7f0e", "#d62728", "#9467bd"]
    ax2.pie(similar_avg.values, labels=similar_avg.index, autopct="%1.1f%%",
            startangle=90, colors=colors)
    ax2.set_title("Average Stock Price Distribution (Peers)")
    st.pyplot(fig2)

    # ======================
    # ADVANCED INSIGHTS SECTION
    # ======================
    st.markdown("### 📊 Quick Insights")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📈 Highest Price", f"₹{company_data['High'].max():.2f}")
    col2.metric("📉 Lowest Price", f"₹{company_data['Low'].min():.2f}")
    col3.metric("🔁 Avg Volatility", f"{company_data['High'].std():.2f}")
    col4.metric("💵 Avg Volume", f"{company_data['Volume'].mean():,.0f}")

    # ======================
    # ADDITIONAL CHART (CANDLE-LIKE)
    # ======================
    st.markdown("### 🕯️ Price Range Visualization")

    fig3, ax3 = plt.subplots(figsize=(10, 5))
    ax3.bar(company_data["Date"], company_data["High"] - company_data["Low"],
            bottom=company_data["Low"], color="lightgreen", alpha=0.6, label="High-Low Range")
    ax3.plot(company_data["Date"], company_data["Close"], color="black", linewidth=1.5, label="Close Price")
    ax3.set_title(f"{selected_company} - Price Range & Close Line")
    ax3.set_ylabel("Price (₹)")
    ax3.legend()
    st.pyplot(fig3)

    # ======================
    # COMPANY OVERVIEW CARD
    # ======================
    st.markdown("### 🏢 Company Overview (Simulated Data)")
    st.info(f"""
    **Company:** {selected_company}  
    **Sector:** Technology / Finance / Manufacturing (Random Sim)  
    **Market Cap:** ₹{random.randint(10_000, 200_000)} Cr  
    **P/E Ratio:** {round(random.uniform(15, 35), 2)}  
    **52-Week Range:** ₹{round(company_data['Low'].min(), 2)} - ₹{round(company_data['High'].max(), 2)}  
    """)

    # ======================
    # FOOTER
    # ======================
    st.markdown("---")
    st.caption("Developed by **Prathanmesh Mandhane** | Powered by Machine Learning ⚡")

else:
    st.info("👈 Choose a company and click **Analyze Stock** to view detailed predictions & charts.")
