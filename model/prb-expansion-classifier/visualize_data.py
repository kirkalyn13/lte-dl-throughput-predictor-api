import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATASOURCE = './data.csv'
REFERENCE_COLUMN = 'PRB_UTILIZATION'
TARGET_COLUMN = "PRB_FOR_EXPANSION"
MODEL_NAME = "./app/model.joblib"

# Load data
df = pd.read_csv(DATASOURCE, encoding="latin-1")
print(df.head())
print(df.info())
print(df.describe())

# Clean Data
df = df.dropna()

# Graph relationship of data
plt.figure(figsize=(12, 8))
plt.scatter(df[REFERENCE_COLUMN], df[TARGET_COLUMN], color='blue', alpha=0.7)
plt.title('PRB Utilization vs PRB for Expansion', fontsize=14)
plt.xlabel('PRB Utilization', fontsize=12)
plt.ylabel('PRB for Expansion', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()