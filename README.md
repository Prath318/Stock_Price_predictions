# 📈 Indian Stock Price Predictor

A machine learning-based stock price predictor with an interactive web interface. The project predicts future stock prices for Indian companies using historical data and regression models, providing visualizations and investment insights through a clean Streamlit dashboard.

---

## ✨ Features

- **Model training pipeline** — engineers 13 features (lags, moving averages, returns) from historical stock data and trains Linear Regression and Random Forest models
- **Interactive dashboard** — Streamlit UI to explore price trends for 8 major Indian companies
- **Buy/Sell/Hold recommendations** — generated from price momentum signals
- **Visualizations** — trend charts and comparative views for quick analysis

---

## 🧱 Tech Stack

| Layer | Tools |
|---|---|
| Language | Python |
| Web UI | Streamlit |
| Model training | Jupyter Notebook |
| ML | scikit-learn (Linear Regression, Random Forest) |
| Data handling | pandas, numpy |
| Visualization | matplotlib |

---

## 📂 Project Structure

```
├── README.md                        # Project documentation
├── app.py                           # Streamlit dashboard with simulated data
├── STOCK_price_prediction.ipynb     # Jupyter notebook with model training pipeline
├── stock_market_dataset.xlsx        # Historical stock market data (20,000 rows)
```

---

## ⚙️ How It Works

The project follows a two-phase workflow:

1. **Training Phase** (`STOCK_price_prediction.ipynb`)
   Loads historical stock data from Excel, engineers 13 features (lags, moving averages, returns), trains both Linear Regression and Random Forest models, and selects the best-performing model — **Random Forest** (RMSE: **18.88**).

2. **Application Phase** (`app.py`)
   A Streamlit dashboard that generates simulated stock data for 8 Indian companies — **TCS, Infosys, Reliance, HDFC Bank, Wipro, Adani Enterprises, ICICI Bank, HCL Tech** — over a 60-day window, letting users select a company, view price trends, and see Buy/Sell/Hold recommendations based on momentum.

---

## 🚀 Getting Started

### 1. Install dependencies
```bash
pip install streamlit pandas numpy scikit-learn matplotlib openpyxl
```

### 2. Run the dashboard
```bash
streamlit run app.py
```
Then open **http://localhost:8501** and select a company to analyze.

### 3. (Optional) Train the model
Open `STOCK_price_prediction.ipynb` in Jupyter and run all cells.
> Requires `stock_market_dataset.xlsx` to be present in the working directory.

---

## 🔮 Future Improvements

- Replace simulated dashboard data with live/real-time market feeds
- Integrate the trained Random Forest model directly into `app.py` (currently the dashboard uses simulated data independent of the notebook's model)
- Add more technical indicators (RSI, MACD, Bollinger Bands)
- Deploy the dashboard (Streamlit Community Cloud / Docker)

---

## ⚠️ Disclaimer

This project is for **educational purposes only**. Predictions and recommendations are based on historical/simulated data and simple statistical models — they should **not** be used as financial advice for real investment decisions.

---

