# Stock_Price_Predictions
📈 Stock Price Prediction Using Machine Learning

This project is a Machine Learning-based Stock Price Predictor that estimates the future trend of stock prices for various companies. It includes a Streamlit web interface where users can input a company name and view predicted stock prices with clear and attractive visualizations.

🚀 Project Overview

This project predicts the future stock prices of selected companies based on their historical data using Machine Learning algorithms such as Linear Regression.
It preprocesses the dataset, trains an ML model, and displays:

Historical stock price trends

Predicted future prices

Suggested companies and insights through a simple and clean UI

🧠 Features

📊 Data Loading — Reads cleaned stock data from an Excel/CSV file

🧹 Data Preprocessing — Handles missing values, scales features, and prepares data for training

🤖 Model Training — Uses Linear Regression for predicting stock trends

💡 Interactive UI — Built using Streamlit for smooth user interaction

📈 Visual Insights — Displays line plots comparing past and predicted prices

🧭 Company Suggestions — Provides company options to guide the user

🛠️ Technologies Used
Category	Tools & Libraries
Programming Language	Python
Libraries	pandas, numpy, matplotlib, scikit-learn
Framework	Streamlit
Model	Linear Regression
Environment	Jupyter Notebook / VS Code
📁 Project Structure
├── app.py                       # Streamlit UI for prediction and visualization
├── stock_price_prediction.ipynb  # Jupyter Notebook for model training
├── model.pkl                    # Saved ML model
├── stock_market_dataset_Cleaned.xlsx  # Cleaned dataset
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation

🧩 Machine Learning Explanation

The model uses Linear Regression, a simple supervised learning algorithm that predicts continuous values like stock prices.

Input Features: Date, Open, High, Low, Close, Volume

Target Variable: Future Closing Price

Process:

Load and preprocess the dataset

Split data into training and testing sets

Train the Linear Regression model on historical stock data

Predict future stock prices

Display results and visualizations using Streamlit

This approach provides a clear understanding of how stock price prediction works with basic ML techniques.

💻 Streamlit UI Overview

The Streamlit interface allows users to:

Select or input a company name

Click a button to predict its future stock price

View stock price visualizations (past vs predicted trends)

See clear and interactive plots in a clean layout

🧭 Future Scope

🔮 Use Random Forest or LSTM models for more accurate predictions

📊 Add multi-company comparison charts

🎨 Improve visualization with more interactive elements

🧠 Integrate model retraining for updated predictions

👨‍💻 Author

Prathamesh Mandhane
🎓 B.Tech in Artificial Intelligence & Data Science
💡 Machine Learning & Data Analytics Enthusiast
📍 Yeshwantrao Chavan College of Engineering, Nagpur
