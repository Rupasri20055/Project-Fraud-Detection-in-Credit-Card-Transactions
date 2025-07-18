# Project - Fraud Detection in Credit Card Transactions

This project uses machine learning techniques to detect fraudulent credit card transactions. It handles imbalanced data using SMOTE and builds a powerful classifier using XGBoost. Multiple visualizations and evaluation metrics ensure high interpretability and performance.

## Dataset Information

- **Source**: [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Total Records**: 284,807 transactions  
- **Fraudulent Transactions**: 492  
- **Features**: 30 (Time, Amount, and anonymized V1–V28)

## Project Objectives

- Perform data cleaning and preprocessing  
- Visualize patterns using EDA  
- Address class imbalance with SMOTE  
- Train a model using XGBoost  
- Evaluate the model using metrics like ROC-AUC  
- Save and reuse the trained model  
- (Optional) Deploy via Streamlit app

## Workflow Overview

### 1. Data Preprocessing
- Checked and removed null values  
- Scaled `Time` and `Amount` features  
- Created `scaled_time` and `scaled_amount` columns

### 2. Exploratory Data Analysis (EDA)
- Count plot, pie chart, and bar chart for class balance  
- Correlation heatmap for feature relationships  
- Histogram for amount distribution

### 3. Handling Class Imbalance
- Applied SMOTE to oversample the minority class in training data

### 4. Model Training
- Used XGBoost Classifier with default tuning  
- Trained on a balanced dataset

### 5. Model Evaluation
- Confusion matrix and classification report  
- ROC-AUC score  
- ROC Curve for performance visualization

### 6. Model Saving
- Saved trained model as `xgboost_model.pkl` using `joblib`

### 7. Optional Streamlit App
- Simple app (`app.py`) to load model and make real-time predictions



## How to Run

1. Clone the repository  
2. Upload `creditcard.csv` into the working directory  
3. Open `fraud_detection.ipynb` in Jupyter Notebook or Google Colab  
4. Run all cells sequentially  
5. *(Optional)* To run the Streamlit app:  
   Open your terminal and run the following command:
   ```bash
streamlit run app.py
```

## Tools & Libraries Used

- Python  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  
- XGBoost  
- imbalanced-learn (SMOTE)  
- Joblib (for saving model)  
- Streamlit (optional)

## Extra Highlights

- Clean, insightful data visualizations  
- Balanced training set using SMOTE  
- High-performance model using XGBoost  
- Deployable web app via Streamlit  
- Saved model for reuse

## Author

Name: Rupa Sri Rudroju  
Project Type: Internship Showcase 
