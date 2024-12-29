import pandas as pd

DATASOURCE = './raw.csv'
MODEL_NAME = "./app/model.joblib"
OUTPUT_FILE = "data.csv"
COLUMNS = ['PRB_UTILIZATION', 'RRC_USER', 'PAYLOAD', 'PRB_FOR_EXPANSION']

# Load data
df = pd.read_csv(DATASOURCE, usecols=COLUMNS, encoding='latin-1')
print(df.head())
print(df.info())
print(df.describe())

# Save file to new CSV file
df.to_csv(OUTPUT_FILE, mode='a', header=not pd.io.common.file_exists(OUTPUT_FILE), index=False)