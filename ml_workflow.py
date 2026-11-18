import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# 1. Create dataset
data = {
    "age": [22, 25, 30, 35, 40, 45, 50, 55],
    "salary": [20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000],
    "city": ["Delhi", "Mumbai", "Delhi", "Pune",
             "Mumbai", "Pune", "Delhi", "Mumbai"],
    "purchased": [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# 2. Separate features and target
X = df.drop("purchased", axis=1)
y = df["purchased"]

# 3. Identify numerical and categorical columns
num_cols = ["age", "salary"]
cat_cols = ["city"]

# 4. Preprocessing
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), num_cols),
    ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols)
])

# 5. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# 6. Create pipeline
model = Pipeline([
    ("preprocessing", preprocessor),
    ("classifier", LogisticRegression())
])

# 7. Train
model.fit(X_train, y_train)

# 8. Predict
predictions = model.predict(X_test)

# 9. Evaluate
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))