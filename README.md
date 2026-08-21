# 🔧 AI Hardware Failure Predictor

Predictive maintenance prototype that analyzes hardware sensor data, estimates failure risk with machine learning, and recommends maintenance actions through an interactive dashboard.

---

## 🚀 Overview

This project demonstrates an end-to-end workflow for **predictive maintenance** using Python and machine learning.

It includes:

* 📊 Sensor data analysis
* 🧹 Data preprocessing
* 📈 Visualizations
* 🤖 Failure prediction
* 📉 Model evaluation
* ⚠️ Risk scoring
* 🔧 Maintenance recommendations
* 🖥️ Streamlit dashboard
* 📄 Automated maintenance report

> **Educational prototype:** The current version uses a small synthetic dataset.

---

## 🧠 Pipeline

```text
Sensor Data
      ↓
Data Cleaning
      ↓
Feature Analysis
      ↓
ML Failure Prediction
      ↓
Risk Score
      ↓
Maintenance Recommendation
      ↓
Dashboard
      ↓
Report
```

---

## 📂 Project Structure

```text
ai-hardware-failure-predictor/
│
├── 01_dataset/
├── 02_preprocessing/
├── 03_visualization/
├── 04_feature_engineering/
├── 05_failure_prediction/
├── 06_model_evaluation/
├── 07_risk_score/
├── 08_predictive_maintenance/
├── 09_dashboard/
├── 10_maintenance_report/
└── README.md
```

---

## 🛠️ Tech Stack

* Python
* Pandas
* Matplotlib
* Scikit-learn
* Streamlit

---

## ▶️ Run

```bash
# Install dependencies
pip install pandas matplotlib scikit-learn streamlit

# Launch dashboard
python -m streamlit run 09_dashboard/app.py
```

---

## 📊 What the dashboard shows

* Hardware health overview
* Average risk score
* Sensor statistics
* Risk distribution
* Maintenance recommendations
* High-risk hardware list

---

## 📄 Report

Generate the maintenance report with:

```bash
python 10_maintenance_report/generate_report.py
```

Output:

```text
hardware_maintenance_report.txt
```

---

## ⚠️ Limitations

* Small synthetic dataset
* Prototype risk scoring
* No live sensor ingestion
* Requires validation with real hardware data

---

## 🚀 Future Improvements

* Real IoT sensor integration
* Time-series failure prediction
* Deep learning models
* Real-time alerts
* Cloud deployment

---

## 🎯 Learning Outcomes

* Data preprocessing
* Feature engineering
* Machine learning classification
* Model evaluation
* Predictive maintenance concepts
* Dashboard development

---

## ⭐ Project Status

| Stage               | Status |
| ------------------- | ------ |
| Dataset             | ✅      |
| Preprocessing       | ✅      |
| Visualization       | ✅      |
| Feature Engineering | ✅      |
| Failure Prediction  | ✅      |
| Model Evaluation    | ✅      |
| Risk Scoring        | ✅      |
| Maintenance Engine  | ✅      |
| Dashboard           | ✅      |
| Report              | ✅      |
| Documentation       | ✅      |

**Project complete.**
