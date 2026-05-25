import pandas as pd

from src.data_cleaning import clean_data
from src.feature_engineering import feature_engineering
from src.visualization import visualize_data
from src.model_training import train_model
from src.evaluation import evaluate_model

# Load dataset
filepath = r"data/house_prices.csv"

df = pd.read_csv(filepath)

# Step 1 → Data Cleaning
df = clean_data(df)

# Step 2 → Feature Engineering
df = feature_engineering(df)

# Step 3 → Visualization
visualize_data(df)

# Step 4 → Model Training
model, x_test, y_test, y_pred = train_model(df)

# Step 5 → Evaluation
evaluate_model(y_test, y_pred)