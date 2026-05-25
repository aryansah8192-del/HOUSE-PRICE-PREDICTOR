# HOUSE-PRICE-PREDICTOR
A modular Machine Learning-based House Price Prediction System using XGBoost Regression with separate pipelines for data cleaning, feature engineering, visualization, model training, and evaluation.

Features
Data preprocessing and cleaning
Missing value handling
Feature engineering and encoding
Outlier handling
Correlation heatmap visualization
XGBoost Regression model
Model evaluation using:
R² Score
MAE
MSE
RMSE
Modular project structure for scalability and maintainability
Project Structure
HOUSE-PRICE-PREDICTOR/
│
├── data/
│   └── house_prices.csv
│
├── src/
│   ├── __init__.py
│   ├── data_cleaning.py
│   ├── feature_engineering.py
│   ├── visualization.py
│   ├── model_training.py
│   └── evaluation.py
│
├── main.py
└── README.md
Workflow
main.py
   ↓
data_cleaning.py
   ↓
feature_engineering.py
   ↓
visualization.py
   ↓
model_training.py
   ↓
evaluation.py
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
XGBoost
Model Used
XGBoost Regressor

The project uses the XGBoost Regression algorithm for predicting house prices based on multiple property-related features.

Evaluation Metrics

The model performance is evaluated using:

R² Score
Mean Absolute Error (MAE)
Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
How to Run
Clone the Repository
git clone <repository-url>
Install Dependencies
pip install -r requirements.txt
Run the Project
python main.py
Future Improvements
Hyperparameter tuning
Streamlit web deployment
Random Forest comparison
Model saving using Pickle
Advanced feature engineering
Real-time prediction interface
Author

Aryan Sah

Project Goal

The goal of this project is to build a scalable and professional Machine Learning pipeline while understanding real-world data preprocessing, feature engineering, and regression modeling techniques.
