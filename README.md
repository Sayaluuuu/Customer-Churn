# Customer-Churn
A end-to-end Machine Learning project that predicts whether a customer will churn (leave a service) based on demographic and account data. Includes data analysis, model training with hyperparameter tuning, and an interactive Streamlit web app for real-time predictions.

customer-churn-prediction/
│
├── Customer_Churn.ipynb      # Notebook: EDA, training, and model selection
├── App2.py                   # Streamlit web application
├── best_model.pkl            # Saved best model (Random Forest)
├── scaler-2.pkl              # Saved StandardScaler
├── customer_churn_data.csv   # Dataset (add your own)
└── README.md


Dataset
The dataset contains customer information with the following features used for prediction:
FeatureDescriptionAgeCustomer ageGenderMale / FemaleTenureNumber of months with the serviceMonthlyChargesMonthly billing amountChurnTarget variable — Yes / No

Exploratory Data Analysis
Key insights from the EDA in the notebook:

Churn distribution visualized via pie chart
Monthly charges are higher on average for churned customers
Tenure is lower on average for churned customers, suggesting newer customers churn more
Contract type influences average monthly charges significantly


Models Trained
Five models were trained and evaluated using accuracy_score. Hyperparameter tuning was applied using GridSearchCV (5-fold cross-validation):
ModelTuningLogistic RegressionDefault parametersK-Nearest Neighboursn_neighbors, weightsSupport Vector MachineC, kernelDecision Treecriterion, max_depth, min_samples_splitRandom Forest n_estimators, max_features, bootstrap

Best Model: Random Forest Classifier — saved as best_model.pkl



Tech Stack

Language: Python 3
ML: Scikit-learn, NumPy, Pandas
Visualization: Matplotlib, Seaborn
App: Streamlit
Model Persistence: Joblib

Notes

The scaler (scaler-2.pkl) was fit on training data — do not re-fit on new data
Gender encoding: Female = 1, Male = 0
Feature order for prediction: [Age, Gender, Tenure, MonthlyCharges]
