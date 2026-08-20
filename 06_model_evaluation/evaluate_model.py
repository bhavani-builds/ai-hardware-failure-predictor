import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)


# ==========================================
# AI HARDWARE FAILURE PREDICTOR
# STAGE 06 — MODEL EVALUATION
# ==========================================


# ------------------------------------------
# File path
# ------------------------------------------

input_file = (
    "C:/ai-hardware-failure-predictor/"
    "02_preprocessing/clean_sensor_data.csv"
)

output_folder = (
    "C:/ai-hardware-failure-predictor/"
    "06_model_evaluation/"
)


# ------------------------------------------
# Load dataset
# ------------------------------------------

df = pd.read_csv(
    input_file
)


print("=" * 60)
print("        HARDWARE FAILURE MODEL EVALUATION")
print("=" * 60)


# ------------------------------------------
# Select features
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


# ------------------------------------------
# Train model
# ------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)


# ------------------------------------------
# Make predictions
# ------------------------------------------

predictions = model.predict(
    X_test
)


# ------------------------------------------
# Calculate metrics
# ------------------------------------------

accuracy = accuracy_score(
    y_test,
    predictions
)

precision = precision_score(
    y_test,
    predictions,
    zero_division=0
)

recall = recall_score(
    y_test,
    predictions,
    zero_division=0
)

f1 = f1_score(
    y_test,
    predictions,
    zero_division=0
)


# ------------------------------------------
# Display metrics
# ------------------------------------------

print("\nModel Performance")
print("-" * 60)

print(
    f"Accuracy  : {accuracy:.2f}"
)

print(
    f"Precision : {precision:.2f}"
)

print(
    f"Recall    : {recall:.2f}"
)

print(
    f"F1 Score  : {f1:.2f}"
)


# ------------------------------------------
# Confusion Matrix
# ------------------------------------------

matrix = confusion_matrix(
    y_test,
    predictions
)


print("\nConfusion Matrix")
print("-" * 60)

print(
    matrix
)


# ------------------------------------------
# Plot confusion matrix
# ------------------------------------------

display = ConfusionMatrixDisplay(
    confusion_matrix=matrix,
    display_labels=[
        "HEALTHY",
        "FAILURE"
    ]
)

display.plot()


plt.title(
    "Hardware Failure Prediction\n"
    "Confusion Matrix",
    fontsize=16,
    fontweight="bold"
)

plt.tight_layout()


# ------------------------------------------
# Save figure
# ------------------------------------------

plt.savefig(
    output_folder +
    "Figure_6_confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ------------------------------------------
# Final message
# ------------------------------------------

print(
    "\n✅ Model evaluation completed!"
)

print(
    "\n🎉 STAGE 06 COMPLETED!"
)
