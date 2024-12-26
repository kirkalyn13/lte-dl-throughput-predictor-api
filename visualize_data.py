import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATASOURCE = './data.csv'
TARGET_COLUMN = "LTE_DL_USER_THROUGHPUT_kbps"
MODEL_NAME = "./app/model.joblib"
BAND_COLORS = {
    700 : 'blue',
    850: 'cyan',
    900: 'green',
    1800: 'yellow',
    2100: 'orange',
    2300: 'indigo',
    2600: 'purple',
    3500: 'grey'
}

# Load data
df = pd.read_csv(DATASOURCE, encoding='latin-1')
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

# Graph relationship of data
plt.figure(figsize=(12, 8))

for band, color in BAND_COLORS.items():
    subset = df[df['BAND'] == band]
    plt.scatter(subset['PRB_UTILIZATION'], subset[TARGET_COLUMN], 
                label=f'Band {band}', color=color, alpha=0.7)

m, b = np.polyfit(df['PRB_UTILIZATION'], df[TARGET_COLUMN], 1)
plt.plot(df['PRB_UTILIZATION'], m * df['PRB_UTILIZATION'] + b, 
         color='red', linewidth=2, label='Trend Line')

plt.title('PRB Utilization vs LTE DL User Throughput by Band', fontsize=14)
plt.xlabel('PRB Utilization', fontsize=12)
plt.ylabel('LTE DL User Throughput (kbps)', fontsize=12)
plt.legend(title='Band', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()