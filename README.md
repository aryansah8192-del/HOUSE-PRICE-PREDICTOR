# HOUSE-PRICE-PREDICTOR
<h1 align="center">🏠 House Price Prediction System</h1>

<p align="center">
A modular Machine Learning project that predicts house prices using <b>XGBoost Regression</b>.
</p>

---

## 🚀 Features

✔️ Data Cleaning Pipeline  
✔️ Feature Engineering  
✔️ Missing Value Handling  
✔️ Outlier Detection & Removal  
✔️ Data Visualization  
✔️ Correlation Heatmaps  
✔️ XGBoost Regression Model  
✔️ Model Evaluation Metrics  
✔️ Modular Project Architecture  

---

## 🛠️ Tech Stack

<p>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
<img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
<img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
<img src="https://img.shields.io/badge/XGBoost-AA0000?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge"/>
</p>

---

## 📂 Project Structure

```bash
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
```

---

## ⚙️ Workflow

```bash
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
```

---

## 📊 Model Used

### XGBoost Regressor

The model predicts house prices using multiple property-related features such as:

- Carpet Area
- Furnishing Status
- Floor Details
- Ownership Type
- Bathroom Count
- Balcony Count
- Location
- Transaction Type

---

## 📈 Evaluation Metrics

The model is evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## ▶️ How To Run

### 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Project

```bash
python main.py
```

---

## 🔮 Future Improvements

- Streamlit Web App Deployment
- Hyperparameter Tuning
- Random Forest Comparison
- Model Saving with Pickle
- Real-Time Prediction System
- Advanced Feature Engineering

---

## 👨‍💻 Author

<b>Aryan Sah</b>

---

<h3 align="center">⭐ If you like this project, consider starring the repository ⭐</h3>