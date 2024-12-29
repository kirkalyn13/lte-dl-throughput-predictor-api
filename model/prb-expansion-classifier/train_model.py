import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

DATASOURCE = './data.csv'
TARGET_COLUMN = "PRB_FOR_EXPANSION"
MODEL_NAME = "../../app/prb_expansion_classifier_model.joblib"
COLUMNS = ['PRB_UTILIZATION', 'RRC_USER', 'PAYLOAD', 'PRB_FOR_EXPANSION']

# Load data
df = pd.read_csv(DATASOURCE, usecols=COLUMNS, encoding='latin-1')
print(df.head())
print(df.info())
print(df.describe())

# Clean Data
df = df.dropna()

# Separate Features and Targets
X = df.drop(TARGET_COLUMN, axis=1)
y = df[TARGET_COLUMN]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save trained model
joblib.dump(model, MODEL_NAME)
print("Model saved as model.joblib")

