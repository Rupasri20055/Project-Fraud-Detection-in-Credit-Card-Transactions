# Project-Fraud-Detection-in-Credit-Card-Transactions
 Fraud Detection in Credit Card Transactions

Project Type: Internship Project (Phase-1 Progress)  
Objective: Detect fraudulent credit card transactions using classification techniques.

Project Overview:

This project aims to identify fraudulent transactions from a credit card dataset using machine learning.  
The initial phase involves exploratory data analysis, data preprocessing, and preparing the dataset for model building.

Dataset Information:

- Source: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- Description: Contains anonymized transaction details and a 'Class' label (1 = Fraud, 0 = Not Fraud).
- Note: The dataset is not included in this repository due to file size and licensing.
        It can be downloaded directly from the Kaggle link above.
  
Work Completed So Far:

- Imported all required Python libraries.  
- Loaded the credit card transaction dataset and displayed its basic structure.  
- Checked for missing values in the dataset and confirmed that there were none (or removed them if present).  
- Analyzed the distribution of fraudulent vs non-fraudulent transactions.  
- Created clear visualizations for class distribution:
  - Count Plot  
  - Clean and resized Pie Chart  
  - Simple Bar Chart  
- Generated a correlation heatmap to identify relationships between features.  
- Plotted the distribution of transaction amounts using a histogram.  
- Applied standard scaling to the `Amount` and `Time` columns.  
- Dropped the original `Amount` and `Time` columns after scaling.  
- Split the data into features (`X`) and target (`y`).  
- Verified that the target variable had no missing values.  
- Performed a train-test split (80-20) with class stratification to preserve class balance in both sets.  
- Checked class distribution in the training dataset.

Libraries and Tools Used:  

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  


Status Update:  

 Exploratory Data Analysis and data preprocessing are completed.  
 The next phase will include class imbalance handling, model building, evaluation, and model saving.

