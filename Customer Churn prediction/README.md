# Customer Churn Prediction

An end-to-end customer churn prediction and business insight system developed using Python, Exploratory Data Analysis (EDA), and Machine Learning.

## Project Overview

Customer churn is an important business problem for subscription-based companies. Predicting which customers are likely to leave can help businesses take proactive retention measures.

This project analyses customer information from a telecommunications dataset and develops a machine learning model to predict customer churn.

The project also extends the analysis with Linear Regression and customer risk segmentation to generate actionable business insights.

## Objectives

- Understand the structure and quality of the customer dataset.
- Identify and handle missing values and data-quality issues.
- Perform exploratory data analysis and visualisation.
- Analyse relationships between customer characteristics and churn.
- Build a Logistic Regression model for churn prediction.
- Evaluate the classification model using multiple performance metrics.
- Use Linear Regression to predict a continuous customer variable.
- Interpret important features associated with churn.
- Segment customers into low, medium, and high churn-risk categories.
- Provide business recommendations based on the analysis.

## Dataset

The project uses a Telco Customer Churn dataset containing customer demographic information, service subscriptions, contract details, billing information, tenure, and churn status.

The dataset contains:

- **7,043 customers**
- **21 columns**
- Numerical and categorical customer attributes
- `Churn` as the target variable

The dataset is stored in:

```text
data/telco_data.csv

____________________________________________________________________________________________________________________________________________________________________________________________________

Project Structure

Customer_churn_prediction/
│
├── data/
│   └── telco_data.csv
│
├── notebooks/
│   └── Customer_Churn_Prediction.ipynb
│
├── visualizations/
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt

____________________________________________________________________________________________________________________________________________________________________________________________________

Technologies Used:

1. Python
2. Pandas
3. NumPy
4. Matplotlib
5. Seaborn
6. Scikit-learn
7. Jupyter Notebook
8. GitHub Codespaces

____________________________________________________________________________________________________________________________________________________________________________________________________

Project Workflow

The project follows the following workflow:

1.  Python environment and project setup
2.  Dataset loading and exploration
3.  Data quality assessment
4.  Missing-value analysis and cleaning
5.  Exploratory Data Analysis
6.  Data visualisation
7.  Statistical analysis
8.  Data preprocessing
9.  Train-test splitting
10. Logistic Regression
11. Classification evaluation
12. Linear Regression
13. Feature interpretation
14. Customer risk segmentation
15. Business recommendations
16. Final conclusions

____________________________________________________________________________________________________________________________________________________________________________________________________

Data Cleaning

The dataset was checked for:

1. Missing values
2. Duplicate rows
3. Incorrect data types
4. Numerical and categorical variables
5. Invalid or inconsistent values

Missing numerical values were handled using appropriate statistical imputation, while categorical values were handled using the most appropriate categorical treatment.

TotalCharges was converted to a numerical data type before modelling.

The cleaned dataset contains 7,043 rows and 21 columns with no remaining missing values.

____________________________________________________________________________________________________________________________________________________________________________________________________

Exploratory Data Analysis

The analysis examines customer churn in relation to:

1. Contract type
2. Internet service
3. Payment method
4. Tenure
5. Monthly charges
6. Total charges
7. Customer services and subscriptions

The analysis found that contract type is particularly important. Month-to-month customers show substantially higher churn compared with customers on one-year and two-year contracts.

____________________________________________________________________________________________________________________________________________________________________________________________________

Logistic Regression

Logistic Regression was used to predict whether a customer would churn.

Test Performance
Metric	    Score
Accuracy	79.06%
Precision	62.95%
Recall	    51.34%
F1-Score	56.55%

The model provides a useful baseline for identifying customers who may be at risk of churn.

____________________________________________________________________________________________________________________________________________________________________________________________________

Linear Regression

Linear Regression was used as a regression extension to predict the continuous variable TotalCharges.

Performance
Metric	    Score
MAE	        1118.64
MSE	        2422185.89
RMSE	    1556.34
R²	        0.5341

The model explains approximately 53.4% of the variation in TotalCharges.

____________________________________________________________________________________________________________________________________________________________________________________________________

Feature Insights

The Logistic Regression coefficients identified several important associations with churn predictions.

Some of the strongest positive associations included:

1. Fiber optic internet service
2. Internet Service = No
3. Electronic check payment
4. Streaming Movies
5. Paperless Billing

Strong negative associations included:

1. Two-year contracts
2. One-year contracts
3. Online Security
4. Phone Service
5. Higher Total Charges

These relationships represent model associations and should not be interpreted as proof of causation.

____________________________________________________________________________________________________________________________________________________________________________________________________

Customer Risk Segmentation

Customers in the test dataset were divided into three risk categories based on predicted churn probability.

Risk Category	Customers	Percentage	Observed Churn Rate
Low Risk	    862	        61.18%	    11.14%
Medium Risk	    348	        24.70%	    39.94%
High Risk	    199	        14.12%	    69.85%

The increasing observed churn rate across the three risk categories demonstrates that the model's predicted probabilities provide useful customer prioritisation.

____________________________________________________________________________________________________________________________________________________________________________________________________

Business Recommendations

Based on the analysis, the following strategies are recommended:

1. Prioritise high-risk customers for retention campaigns.
2. Encourage month-to-month customers to move toward longer-term contracts.
3. Investigate churn among fiber optic customers.
4. Examine retention opportunities among electronic-check customers.
5. Promote useful support and security services.
6. Use risk-based retention strategies rather than treating all customers identically.

____________________________________________________________________________________________________________________________________________________________________________________________________

How to Run

Clone the repository and install the required Python packages:

</> Bash
pip install -r requirements.txt

Open the project in GitHub Codespaces or a local VS Code environment.

Run:

notebooks/Customer_Churn_Prediction.ipynb

Make sure the dataset remains at:

data/telco_data.csv


Disclaimer

The predictions generated by the model should be treated as risk indicators rather than definitive predictions that a specific customer will leave.

The analysis is intended for educational and analytical purposes.


Author

M Sanjay Lakshman Reddy