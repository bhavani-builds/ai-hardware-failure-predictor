import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


# ==========================================
# AI HARDWARE FAILURE PREDICTOR
# STAGE 05 — FAILURE PREDICTION
# ==========================================


# ------------------------------------------
# File path
# ------------------------------------------

input_file = (
    "C:/ai-hardware-failure-predictor/"
    "02_preprocessing/clean_sensor_data.csv"
)


# ------------------------------------------
# Load dataset
# ------------------------------------------

df = pd.read_csv(input_file)


print("=" * 60)
print("        AI HARDWARE FAILURE PREDICTOR")
print("=" * 60)


print(
    f"\nTotal samples: {len(df)}"
)


# ------------------------------------------
# Select sensor features
# ------------------------------------------

features = [
    "temperature",
    "voltage",
    "current",
    "vibration",
    "operating_hours"
]


X = df[features]

y = df["failure"]


# ------------------------------------------
# Split dataset
# ------------------------------------------

X_train, X_test, y_train, y_test = (
    train_test_split(
        X,
        y,
        test_size=0.25,
        random_state=42,
        stratify=y
    )
)


print(
    f"Training samples: {len(X_train)}"
)

print(
    f"Testing samples : {len(X_test)}"
)


# ------------------------------------------
# Create model
# ------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ------------------------------------------
# Train model
# ------------------------------------------

model.fit(
    X_train,
    y_train
)


print(
    "\n✅ Model training completed!"
)


# ------------------------------------------
# Predict
# ------------------------------------------

predictions = model.predict(
    X_test
)


# ------------------------------------------
# Accuracy
# ------------------------------------------

accuracy = accuracy_score(
    y_test,
    predictions
)


print(
    f"\nAccuracy: "
    f"{accuracy * 100:.2f}%"
)


# ------------------------------------------
# Classification report
# ------------------------------------------

print(
    "\nClassification Report"
)

print(
    "-" * 60
)

print(
    classification_report(
        y_test,
        predictions,
        target_names=[
            "HEALTHY",
            "FAILURE"
        ],
        zero_division=0
    )
)


# ------------------------------------------
# Feature importance
# ------------------------------------------

importance = (
    model.feature_importances_
)


feature_importance = pd.DataFrame({

    "feature": features,

    "importance": importance

})


feature_importance = (
    feature_importance
    .sort_values(
        "importance",
        ascending=False
    )
)


print(
    "\nFeature Importance"
)

print(
    "-" * 60
)

print(
    feature_importance.to_string(
        index=False
    )
)


print(
    "\n🎉 STAGE 05 COMPLETED!"
)
