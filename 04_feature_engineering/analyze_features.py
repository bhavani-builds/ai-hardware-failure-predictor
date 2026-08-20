import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# AI HARDWARE FAILURE PREDICTOR
# STAGE 04 — FEATURE ENGINEERING
# ==========================================


input_file = (
    "C:/ai-hardware-failure-predictor/"
    "02_preprocessing/clean_sensor_data.csv"
)

output_folder = (
    "C:/ai-hardware-failure-predictor/"
    "04_feature_engineering/"
)


# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(input_file)


print("=" * 60)
print("HARDWARE FEATURE ANALYSIS")
print("=" * 60)


# ==========================================
# SELECT SENSOR FEATURES
# ==========================================

features = [
    "temperature",
    "voltage",
    "current",
    "vibration",
    "operating_hours"
]


# ==========================================
# CORRELATION WITH FAILURE
# ==========================================

correlation = (
    df[features + ["failure"]]
    .corr()["failure"]
    .drop("failure")
    .sort_values(
        ascending=False
    )
)


print("\nCorrelation with Hardware Failure")
print("-" * 60)

print(
    correlation.round(3)
)


# ==========================================
# COMPLETE CORRELATION MATRIX
# ==========================================

correlation_matrix = (
    df[features + ["failure"]]
    .corr()
)


print("\nComplete Correlation Matrix")
print("-" * 60)

print(
    correlation_matrix.round(2)
)


# ==========================================
# CORRELATION HEATMAP
# ==========================================

plt.figure(
    figsize=(10, 7)
)

plt.imshow(
    correlation_matrix,
    interpolation="nearest"
)

plt.colorbar(
    label="Correlation"
)


labels = (
    features + ["failure"]
)


plt.xticks(
    range(len(labels)),
    labels,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(labels)),
    labels
)


# Add correlation values

for row in range(len(labels)):

    for column in range(len(labels)):

        value = (
            correlation_matrix
            .iloc[row, column]
        )

        plt.text(
            column,
            row,
            f"{value:.2f}",
            ha="center",
            va="center"
        )


plt.title(
    "Hardware Sensor Correlation Matrix",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()


plt.savefig(
    output_folder +
    "Figure_4_correlation.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================
# FAILURE GROUP COMPARISON
# ==========================================

summary = (
    df.groupby("failure")[features]
    .mean()
    .round(2)
)


print("\nAverage Sensor Values")
print("-" * 60)

print(
    summary
)


# ==========================================
# SAVE RESULTS
# ==========================================

correlation.to_csv(
    output_folder +
    "failure_correlation.csv"
)

summary.to_csv(
    output_folder +
    "failure_feature_summary.csv"
)


print(
    "\n✅ Correlation analysis completed!"
)

print(
    "✅ Feature summary created!"
)

print(
    "\n🎉 STAGE 04 COMPLETED!"
)
