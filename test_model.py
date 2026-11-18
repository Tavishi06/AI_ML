import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Creating dataset

data = {
    "Age": [25, 30, 35, 40, 45, 50, 55, 60],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Separating features and target variable

X = df[["Age", "Salary"]]
y = df["Purchased"]

# Splitting the dataset into training and testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.25, random_state = 42)

# Feature scaling 

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

# Train the model 

model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions

y_pred = model.predict(X_test)

# Evaluate the model

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))