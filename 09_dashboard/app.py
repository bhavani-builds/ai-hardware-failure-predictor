import streamlit as st
import pandas as pd


# ==========================================
# AI HARDWARE FAILURE PREDICTOR
# STAGE 09 — HARDWARE HEALTH DASHBOARD
# ==========================================


# ------------------------------------------
# Page configuration
# ------------------------------------------

st.set_page_config(
    page_title="AI Hardware Health Monitor",
    page_icon="🔧",
    layout="wide"
)


# ------------------------------------------
# Title
# ------------------------------------------

st.title(
    "🔧 AI Hardware Health Monitor"
)

st.write(
    "Machine-learning based hardware "
    "failure prediction and predictive "
    "maintenance prototype."
)

st.divider()


# ------------------------------------------
# Load maintenance results
# ------------------------------------------

input_file = (
    "C:/ai-hardware-failure-predictor/"
    "08_predictive_maintenance/"
    "maintenance_recommendations.csv"
)


try:

    df = pd.read_csv(
        input_file
    )

except FileNotFoundError:

    st.error(
        "maintenance_recommendations.csv "
        "was not found. Run Stage 08 first."
    )

    st.stop()


# ------------------------------------------
# Calculate statistics
# ------------------------------------------

total_units = len(df)

high_risk = (
    df["risk_level"] == "HIGH"
).sum()

medium_risk = (
    df["risk_level"] == "MEDIUM"
).sum()

low_risk = (
    df["risk_level"] == "LOW"
).sum()

average_risk = (
    df["risk_score"].mean()
)

average_temperature = (
    df["temperature"].mean()
)

average_vibration = (
    df["vibration"].mean()
)


# ------------------------------------------
# Dashboard overview
# ------------------------------------------

st.subheader(
    "📊 Hardware Health Overview"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Hardware Units",
        total_units
    )


with col2:

    st.metric(
        "High Risk",
        high_risk
    )


with col3:

    st.metric(
        "Medium Risk",
        medium_risk
    )


with col4:

    st.metric(
        "Average Risk",
        f"{average_risk:.1f}/100"
    )


st.divider()


# ------------------------------------------
# Overall health status
# ------------------------------------------

st.subheader(
    "⚠️ Overall Hardware Health"
)


if average_risk >= 70:

    st.error(
        "🔴 HIGH RISK — Immediate inspection recommended."
    )

elif average_risk >= 40:

    st.warning(
        "🟡 MEDIUM RISK — Maintenance should be scheduled."
    )

else:

    st.success(
        "🟢 LOW RISK — Hardware operating normally."
    )


# ------------------------------------------
# Sensor statistics
# ------------------------------------------

st.divider()

st.subheader(
    "🌡️ Sensor Statistics"
)


sensor_col1, sensor_col2, sensor_col3 = (
    st.columns(3)
)


with sensor_col1:

    st.metric(
        "Average Temperature",
        f"{average_temperature:.1f} °C"
    )


with sensor_col2:

    st.metric(
        "Average Vibration",
        f"{average_vibration:.2f}"
    )


with sensor_col3:

    st.metric(
        "Maximum Temperature",
        f"{df['temperature'].max():.1f} °C"
    )


# ------------------------------------------
# Risk distribution
# ------------------------------------------

st.divider()

st.subheader(
    "📈 Risk Distribution"
)


risk_counts = (
    df["risk_level"]
    .value_counts()
)


st.bar_chart(
    risk_counts
)


# ------------------------------------------
# Sensor activity
# ------------------------------------------

st.subheader(
    "📡 Sensor Measurements"
)


sensor_data = df[
    [
        "temperature",
        "voltage",
        "current",
        "vibration"
    ]
]


st.line_chart(
    sensor_data
)


# ------------------------------------------
# Hardware table
# ------------------------------------------

st.divider()

st.subheader(
    "📋 Hardware Health Details"
)


display_columns = [
    "temperature",
    "voltage",
    "current",
    "vibration",
    "operating_hours",
    "failure_probability",
    "risk_score",
    "risk_level",
    "maintenance_recommendation"
]


st.dataframe(
    df[display_columns],
    width="stretch"
)


# ------------------------------------------
# Maintenance recommendations
# ------------------------------------------

st.divider()

st.subheader(
    "🔧 Maintenance Recommendations"
)


recommendation_counts = (
    df[
        "maintenance_recommendation"
    ]
    .value_counts()
)


st.bar_chart(
    recommendation_counts
)


# ------------------------------------------
# High-risk hardware
# ------------------------------------------

st.divider()

st.subheader(
    "🔴 High-Risk Hardware"
)


high_risk_data = df[
    df["risk_level"] == "HIGH"
]


if len(high_risk_data) > 0:

    st.dataframe(
        high_risk_data[
            display_columns
        ],
        width="stretch"
    )

else:

    st.success(
        "No high-risk hardware units detected."
    )


# ------------------------------------------
# Footer
# ------------------------------------------

st.divider()

st.caption(
    "Educational predictive-maintenance "
    "prototype. Risk scores and predictions "
    "require validation with real hardware "
    "data before deployment."
)
