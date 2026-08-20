import pandas as pd


# ==========================================
# AI HARDWARE FAILURE PREDICTOR
# STAGE 02 — DATA PREPROCESSING
# ==========================================


# File paths

input_file = (
    "C:/ai-hardware-failure-predictor/"
    "01_dataset/hardware_sensor_data.csv"
)

output_file = (
    "C:/ai-hardware-failure-predictor/"
    "02_preprocessing/clean_sensor_data.csv"
)


# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv(input_file)


print("=" * 60)
print("HARDWARE SENSOR DATA PREPROCESSING")
print("=" * 60)


print("\nOriginal Dataset")
print("-" * 60)

print(df)


# ==========================================
# CHECK MISSING VALUES
# ==========================================

print("\nMissing Values")
print("-" * 60)

print(
    df.isnull().sum()
)


# ==========================================
# CHECK DUPLICATES
# ==========================================

duplicate_count = (
    df.duplicated().sum()
)

print("\nDuplicate Rows")
print("-" * 60)

print(
    f"Duplicates found: {duplicate_count}"
)


# Remove duplicates

df = df.drop_duplicates()


# ==========================================
# CHECK DATA TYPES
# ==========================================

print("\nData Types")
print("-" * 60)

print(
    df.dtypes
)


# ==========================================
# BASIC STATISTICS
# ==========================================

print("\nSensor Statistics")
print("-" * 60)

print(
    df.describe().round(2)
)


# ==========================================
# SAVE CLEAN DATASET
# ==========================================

df.to_csv(
    output_file,
    index=False
)


print(
    "\n✅ Clean sensor dataset saved!"
)

print(
    "\nLocation:"
)

print(
    output_file
)

print(
    "\n🎉 STAGE 02 COMPLETED!"
)
