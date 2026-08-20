import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# AI HARDWARE FAILURE PREDICTOR
# STAGE 03 — SENSOR VISUALIZATION
# ==========================================


# ------------------------------------------
# File paths
# ------------------------------------------

input_file = (
    "C:/ai-hardware-failure-predictor/"
    "02_preprocessing/clean_sensor_data.csv"
)

output_folder = (
    "C:/ai-hardware-failure-predictor/"
    "03_visualization/"
)


# ------------------------------------------
# Load dataset
# ------------------------------------------

df = pd.read_csv(input_file)


print("=" * 60)
print("HARDWARE SENSOR VISUALIZATION")
print("=" * 60)


# ==========================================
# 1. TEMPERATURE VS FAILURE
# ==========================================

plt.figure(figsize=(9, 6))

plt.scatter(
    df["temperature"],
    df["failure"],
    s=100
)

plt.title(
    "Temperature vs Hardware Failure",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Temperature (°C)"
)

plt.ylabel(
    "Failure (0 = Healthy, 1 = Failure)"
)

plt.yticks(
    [0, 1],
    ["Healthy", "Failure"]
)

plt.grid(
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()

plt.savefig(
    output_folder +
    "Figure_3_1_temperature_failure.png",
    dpi=300
)

plt.show()


# ==========================================
# 2. VOLTAGE VS FAILURE
# ==========================================

plt.figure(figsize=(9, 6))

plt.scatter(
    df["voltage"],
    df["failure"],
    s=100
)

plt.title(
    "Voltage vs Hardware Failure",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Voltage (V)"
)

plt.ylabel(
    "Failure (0 = Healthy, 1 = Failure)"
)

plt.yticks(
    [0, 1],
    ["Healthy", "Failure"]
)

plt.grid(
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()

plt.savefig(
    output_folder +
    "Figure_3_2_voltage_failure.png",
    dpi=300
)

plt.show()


# ==========================================
# 3. CURRENT VS FAILURE
# ==========================================

plt.figure(figsize=(9, 6))

plt.scatter(
    df["current"],
    df["failure"],
    s=100
)

plt.title(
    "Current vs Hardware Failure",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Current (A)"
)

plt.ylabel(
    "Failure (0 = Healthy, 1 = Failure)"
)

plt.yticks(
    [0, 1],
    ["Healthy", "Failure"]
)

plt.grid(
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()

plt.savefig(
    output_folder +
    "Figure_3_3_current_failure.png",
    dpi=300
)

plt.show()


# ==========================================
# 4. VIBRATION VS FAILURE
# ==========================================

plt.figure(figsize=(9, 6))

plt.scatter(
    df["vibration"],
    df["failure"],
    s=100
)

plt.title(
    "Vibration vs Hardware Failure",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Vibration Level"
)

plt.ylabel(
    "Failure (0 = Healthy, 1 = Failure)"
)

plt.yticks(
    [0, 1],
    ["Healthy", "Failure"]
)

plt.grid(
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()

plt.savefig(
    output_folder +
    "Figure_3_4_vibration_failure.png",
    dpi=300
)

plt.show()


# ==========================================
# 5. OPERATING HOURS VS FAILURE
# ==========================================

plt.figure(figsize=(9, 6))

plt.scatter(
    df["operating_hours"],
    df["failure"],
    s=100
)

plt.title(
    "Operating Hours vs Hardware Failure",
    fontsize=18,
    fontweight="bold"
)

plt.xlabel(
    "Operating Hours"
)

plt.ylabel(
    "Failure (0 = Healthy, 1 = Failure)"
)

plt.yticks(
    [0, 1],
    ["Healthy", "Failure"]
)

plt.grid(
    linestyle="--",
    alpha=0.4
)

plt.tight_layout()

plt.savefig(
    output_folder +
    "Figure_3_5_hours_failure.png",
    dpi=300
)

plt.show()


# ==========================================
# SUMMARY
# ==========================================

print("\nSensor Summary")
print("-" * 60)

print(
    f"Average Temperature : "
    f"{df['temperature'].mean():.2f} °C"
)

print(
    f"Average Voltage     : "
    f"{df['voltage'].mean():.2f} V"
)

print(
    f"Average Current     : "
    f"{df['current'].mean():.2f} A"
)

print(
    f"Average Vibration   : "
    f"{df['vibration'].mean():.2f}"
)

print(
    f"Average Operating Hours: "
    f"{df['operating_hours'].mean():.2f}"
)


print(
    "\n✅ Sensor graphs created!"
)

print(
    "\n🎉 STAGE 03 COMPLETED!"
)
