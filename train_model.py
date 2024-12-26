import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import joblib

DATASOURCE = './data.csv'
TARGET_COLUMN = "LTE_DL_USER_THROUGHPUT_kbps"
MODEL_NAME = "./app/model.joblib"
COLUMNS = ['PRB_UTILIZATION', 'RRC_USER', 'PAYLOAD', 'LTE_DL_USER_THROUGHPUT_kbps']

# Load data
df = pd.read_csv(DATASOURCE, usecols=COLUMNS, encoding='latin-1')
print(df.head())
print(df.info())
print(df.describe())

# Clean Data
df = df.dropna()
q1 = df[TARGET_COLUMN].quantile(0.25)
q3 = df[TARGET_COLUMN].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
df = df[(df[TARGET_COLUMN] >= lower_bound) & (df[TARGET_COLUMN] <= upper_bound)]

# Separate Features and Targets
X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]


# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")

# Save trained model
joblib.dump(model, MODEL_NAME)
print("Model saved as model.joblib")

