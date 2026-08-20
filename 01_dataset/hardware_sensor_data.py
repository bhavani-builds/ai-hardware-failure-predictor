import pandas as pd


# ==========================================
# AI HARDWARE FAILURE PREDICTOR
# STAGE 01 — HARDWARE SENSOR DATASET
# ==========================================


# Create sample hardware sensor data

data = {

    "temperature": [
        35, 38, 42, 45,
        50, 55, 60, 65,
        70, 75, 80, 85,
        40, 48, 58, 68
    ],

    "voltage": [
        3.30, 3.31, 3.29, 3.30,
        3.28, 3.27, 3.25, 3.24,
        3.22, 3.20, 3.18, 3.15,
        3.30, 3.28, 3.26, 3.23
    ],

    "current": [
        0.80, 0.82, 0.85, 0.88,
        0.92, 0.98, 1.05, 1.10,
        1.18, 1.25, 1.35, 1.45,
        0.84, 0.90, 1.02, 1.15
    ],

    "vibration": [
        0.10, 0.12, 0.15, 0.18,
        0.20, 0.25, 0.30, 0.38,
        0.45, 0.55, 0.70, 0.85,
        0.13, 0.22, 0.32, 0.42
    ],

    "operating_hours": [
        500, 800, 1200, 1600,
        2200, 3000, 3800, 4500,
        5200, 6000, 7000, 8000,
        1000, 2500, 4000, 5500
    ],

    "failure": [
        0, 0, 0, 0,
        0, 0, 0, 0,
        1, 1, 1, 1,
        0, 0, 0, 1
    ]
}


# Create DataFrame

df = pd.DataFrame(data)


# ==========================================
# DISPLAY DATASET
# ==========================================

print("=" * 60)

print(
    "AI HARDWARE FAILURE PREDICTOR"
)

print("=" * 60)


print("\nHardware Sensor Dataset")

print("-" * 60)

print(
    df.to_string(index=False)
)


# ==========================================
# DATASET INFORMATION
# ==========================================

print("\nDataset Information")

print("-" * 60)

print(
    f"Total samples : {len(df)}"
)

print(
    f"Healthy units : "
    f"{(df['failure'] == 0).sum()}"
)

print(
    f"Failure cases : "
    f"{(df['failure'] == 1).sum()}"
)


# ==========================================
# SAVE DATASET
# ==========================================

df.to_csv(
    "hardware_sensor_data.csv",
    index=False
)


print(
    "\n✅ hardware_sensor_data.csv created!"
)

print(
    "\n🎉 STAGE 01 COMPLETED!"
)
