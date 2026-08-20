import pandas as pd

from sklearn.ensemble import RandomForestClassifier


# ==========================================
# AI HARDWARE FAILURE PREDICTOR
# STAGE 07 — FAILURE RISK SCORE
# ==========================================


# ------------------------------------------
# File paths
# ------------------------------------------

input_file = (
    "C:/ai-hardware-failure-predictor/"
    "02_preprocessing/clean_sensor_data.csv"
)

output_file = (
    "C:/ai-hardware-failure-predictor/"
    "07_risk_score/"
    "hardware_risk_results.csv"
)


# ------------------------------------------
# Load dataset
# ------------------------------------------

df = pd.read_csv(input_file)


print("=" * 65)
print("             HARDWARE FAILURE RISK")
print("=" * 65)


# ------------------------------------------
# Features
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
# Train prototype model
# ------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X,
    y
)


# ------------------------------------------
# Get failure probability
# ------------------------------------------

probabilities = model.predict_proba(X)

classes = list(model.classes_)


if 1 in classes:

    failure_index = classes.index(1)

    failure_probability = (
        probabilities[:, failure_index]
    )

else:

    failure_probability = (
        [0] * len(df)
    )


# ------------------------------------------
# Convert probability to risk score
# ------------------------------------------

df["failure_probability"] = (
    failure_probability
)

df["risk_score"] = (
    df["failure_probability"] * 100
).round(2)


# ------------------------------------------
# Determine risk level
# ------------------------------------------

def get_risk_level(score):

    if score >= 70:
        return "HIGH"

    elif score >= 40:
        return "MEDIUM"

    else:
        return "LOW"


df["risk_level"] = (
    df["risk_score"]
    .apply(get_risk_level)
)


# ------------------------------------------
# Display results
# ------------------------------------------

print("\nHardware Risk Analysis")
print("-" * 65)


for index, row in df.iterrows():

    print(
        f"\nHardware Unit {index + 1}"
    )

    print(
        f"  Temperature : "
        f"{row['temperature']} °C"
    )

    print(
        f"  Voltage     : "
        f"{row['voltage']} V"
    )

    print(
        f"  Current     : "
        f"{row['current']} A"
    )

    print(
        f"  Vibration   : "
        f"{row['vibration']}"
    )

    print(
        f"  Operating   : "
        f"{row['operating_hours']} hours"
    )

    print(
        f"  Risk Score  : "
        f"{row['risk_score']}/100"
    )

    print(
        f"  Risk Level  : "
        f"{row['risk_level']}"
    )


# ------------------------------------------
# Summary
# ------------------------------------------

print("\n" + "=" * 65)

print("RISK SUMMARY")

print("=" * 65)


print(
    "\nAverage Risk Score:",
    round(
        df["risk_score"].mean(),
        2
    )
)


print(
    "\nRisk Level Counts:"
)

print(
    df["risk_level"].value_counts()
)


# ------------------------------------------
# Save results
# ------------------------------------------

df.to_csv(
    output_file,
    index=False
)


print(
    "\n✅ Hardware risk results saved!"
)

print(
    "\nLocation:"
)

print(
    output_file
)

print(
    "\n🎉 STAGE 07 COMPLETED!"
)
