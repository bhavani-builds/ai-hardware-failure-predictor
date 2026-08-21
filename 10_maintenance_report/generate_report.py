import pandas as pd
from datetime import datetime


# ==========================================
# AI HARDWARE FAILURE PREDICTOR
# STAGE 10 — AUTOMATED MAINTENANCE REPORT
# ==========================================


# ------------------------------------------
# File paths
# ------------------------------------------

input_file = (
    "C:/ai-hardware-failure-predictor/"
    "08_predictive_maintenance/"
    "maintenance_recommendations.csv"
)

output_file = (
    "C:/ai-hardware-failure-predictor/"
    "10_maintenance_report/"
    "hardware_maintenance_report.txt"
)


# ------------------------------------------
# Load data
# ------------------------------------------

df = pd.read_csv(input_file)


print("=" * 70)
print("        AUTOMATED HARDWARE MAINTENANCE REPORT")
print("=" * 70)


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

average_voltage = (
    df["voltage"].mean()
)

average_current = (
    df["current"].mean()
)

average_vibration = (
    df["vibration"].mean()
)


# ------------------------------------------
# Overall status
# ------------------------------------------

if high_risk > 0:

    overall_status = (
        "ATTENTION REQUIRED"
    )

elif medium_risk > 0:

    overall_status = (
        "MAINTENANCE MONITORING"
    )

else:

    overall_status = (
        "NORMAL OPERATION"
    )


# ------------------------------------------
# Generate report
# ------------------------------------------

with open(
    output_file,
    "w",
    encoding="utf-8"
) as report:

    report.write(
        "=" * 70 + "\n"
    )

    report.write(
        "             AI HARDWARE HEALTH REPORT\n"
    )

    report.write(
        "=" * 70 + "\n\n"
    )


    # --------------------------------------
    # Report information
    # --------------------------------------

    report.write(
        "REPORT INFORMATION\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        "Generated: "
        + datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        + "\n"
    )

    report.write(
        "System: AI Hardware Failure Predictor\n\n"
    )


    # --------------------------------------
    # Overall status
    # --------------------------------------

    report.write(
        "OVERALL HARDWARE STATUS\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Status: {overall_status}\n"
    )

    report.write(
        f"Average Risk Score: "
        f"{average_risk:.2f}/100\n\n"
    )


    # --------------------------------------
    # Hardware summary
    # --------------------------------------

    report.write(
        "HARDWARE SUMMARY\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Total Hardware Units : "
        f"{total_units}\n"
    )

    report.write(
        f"Low Risk Units       : "
        f"{low_risk}\n"
    )

    report.write(
        f"Medium Risk Units    : "
        f"{medium_risk}\n"
    )

    report.write(
        f"High Risk Units      : "
        f"{high_risk}\n\n"
    )


    # --------------------------------------
    # Sensor summary
    # --------------------------------------

    report.write(
        "SENSOR SUMMARY\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        f"Average Temperature : "
        f"{average_temperature:.2f} °C\n"
    )

    report.write(
        f"Average Voltage     : "
        f"{average_voltage:.2f} V\n"
    )

    report.write(
        f"Average Current     : "
        f"{average_current:.2f} A\n"
    )

    report.write(
        f"Average Vibration   : "
        f"{average_vibration:.2f}\n\n"
    )


    # --------------------------------------
    # High-risk hardware
    # --------------------------------------

    report.write(
        "HIGH-RISK HARDWARE\n"
    )

    report.write(
        "-" * 70 + "\n"
    )


    high_risk_data = df[
        df["risk_level"] == "HIGH"
    ]


    if len(high_risk_data) > 0:

        for index, row in (
            high_risk_data.iterrows()
        ):

            report.write(
                f"\nHardware Unit "
                f"{index + 1}\n"
            )

            report.write(
                f"  Temperature: "
                f"{row['temperature']} °C\n"
            )

            report.write(
                f"  Voltage: "
                f"{row['voltage']} V\n"
            )

            report.write(
                f"  Current: "
                f"{row['current']} A\n"
            )

            report.write(
                f"  Vibration: "
                f"{row['vibration']}\n"
            )

            report.write(
                f"  Operating Hours: "
                f"{row['operating_hours']}\n"
            )

            report.write(
                f"  Risk Score: "
                f"{row['risk_score']}/100\n"
            )

            report.write(
                f"  Recommendation: "
                f"{row['maintenance_recommendation']}\n"
            )

    else:

        report.write(
            "No high-risk hardware units detected.\n"
        )


    report.write("\n")


    # --------------------------------------
    # Maintenance recommendations
    # --------------------------------------

    report.write(
        "MAINTENANCE RECOMMENDATIONS\n"
    )

    report.write(
        "-" * 70 + "\n"
    )


    recommendations = (
        df[
            "maintenance_recommendation"
        ]
        .value_counts()
    )


    for recommendation, count in (
        recommendations.items()
    ):

        report.write(
            f"{recommendation}: "
            f"{count} unit(s)\n"
        )


    report.write("\n")


    # --------------------------------------
    # Final recommendation
    # --------------------------------------

    report.write(
        "FINAL RECOMMENDATION\n"
    )

    report.write(
        "-" * 70 + "\n"
    )


    if high_risk > 0:

        report.write(
            "Immediate inspection is recommended "
            "for high-risk hardware units.\n"
        )

        report.write(
            "Review sensor conditions and investigate "
            "potential causes of abnormal behavior.\n"
        )

    elif medium_risk > 0:

        report.write(
            "Schedule maintenance for medium-risk "
            "hardware units and continue monitoring.\n"
        )

    else:

        report.write(
            "Hardware units are currently classified "
            "as low risk by this prototype.\n"
        )


    # --------------------------------------
    # Disclaimer
    # --------------------------------------

    report.write("\n")

    report.write(
        "IMPORTANT NOTE\n"
    )

    report.write(
        "-" * 70 + "\n"
    )

    report.write(
        "This is an educational predictive-maintenance "
        "prototype using a small synthetic dataset.\n"
    )

    report.write(
        "Risk scores and predictions require validation "
        "using real hardware sensor data before deployment.\n"
    )


# ------------------------------------------
# Console output
# ------------------------------------------

print(
    f"\nOverall Status: "
    f"{overall_status}"
)

print(
    f"Average Risk: "
    f"{average_risk:.2f}/100"
)

print(
    f"High-Risk Units: "
    f"{high_risk}"
)

print(
    "\n✅ Hardware maintenance report generated!"
)

print(
    "\nSaved to:"
)

print(
    output_file
)

print(
    "\n🎉 STAGE 10 COMPLETED!"
)
