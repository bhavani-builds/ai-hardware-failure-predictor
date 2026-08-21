import pandas as pd


# ==========================================
# AI HARDWARE FAILURE PREDICTOR
# STAGE 08 — PREDICTIVE MAINTENANCE
# ==========================================


# ------------------------------------------
# File paths
# ------------------------------------------

input_file = (
    "C:/ai-hardware-failure-predictor/"
    "07_risk_score/hardware_risk_results.csv"
)

output_file = (
    "C:/ai-hardware-failure-predictor/"
    "08_predictive_maintenance/"
    "maintenance_recommendations.csv"
)


# ------------------------------------------
# Load risk results
# ------------------------------------------

df = pd.read_csv(input_file)


print("=" * 70)
print("             PREDICTIVE MAINTENANCE ENGINE")
print("=" * 70)


# ------------------------------------------
# Maintenance recommendation function
# ------------------------------------------

def get_recommendation(row):

    score = row["risk_score"]

    temperature = row["temperature"]

    vibration = row["vibration"]

    operating_hours = row["operating_hours"]


    # HIGH RISK

    if score >= 70:

        return "IMMEDIATE INSPECTION"


    # MEDIUM RISK

    elif score >= 40:

        return "SCHEDULE MAINTENANCE"


    # Additional warning conditions

    elif temperature >= 75:

        return "CHECK TEMPERATURE"


    elif vibration >= 0.60:

        return "CHECK VIBRATION"


    elif operating_hours >= 7000:

        return "SCHEDULE ROUTINE INSPECTION"


    # LOW RISK

    else:

        return "NORMAL OPERATION"


# ------------------------------------------
# Generate recommendations
# ------------------------------------------

df["maintenance_recommendation"] = (
    df.apply(
        get_recommendation,
        axis=1
    )
)


# ------------------------------------------
# Display results
# ------------------------------------------

print("\nMaintenance Recommendations")
print("-" * 70)


for index, row in df.iterrows():

    print(
        f"\nHardware Unit {index + 1}"
    )

    print(
        f"  Risk Score : "
        f"{row['risk_score']}/100"
    )

    print(
        f"  Risk Level : "
        f"{row['risk_level']}"
    )

    print(
        f"  Temperature: "
        f"{row['temperature']} °C"
    )

    print(
        f"  Vibration  : "
        f"{row['vibration']}"
    )

    print(
        f"  Recommendation:"
    )

    print(
        f"  → {row['maintenance_recommendation']}"
    )


# ------------------------------------------
# Recommendation summary
# ------------------------------------------

print("\n" + "=" * 70)

print(
    "MAINTENANCE SUMMARY"
)

print("=" * 70)


recommendation_counts = (
    df["maintenance_recommendation"]
    .value_counts()
)


print(
    recommendation_counts
)


# ------------------------------------------
# Save results
# ------------------------------------------

df.to_csv(
    output_file,
    index=False
)


print(
    "\n✅ Maintenance recommendations saved!"
)

print(
    "\nLocation:"
)

print(
    output_file
)


print(
    "\n🎉 STAGE 08 COMPLETED!"
)
