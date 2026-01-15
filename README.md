# medical-data-analysis
# Medical Data Analysis – Cardiovascular Disease Risk

This project analyzes medical examination data to explore how health indicators and lifestyle factors relate to cardiovascular disease.

Using Python data analysis and visualization tools, the project investigates relationships between variables such as blood pressure, cholesterol, glucose levels, BMI, smoking, alcohol intake, and physical activity, and how they correlate with heart disease risk.

## Objectives
- Engineer meaningful health indicators (e.g., overweight using BMI)
- Normalize categorical health measurements
- Visualize categorical health trends by cardiovascular status
- Identify correlations between medical features using a heatmap

## Dataset
The analysis is performed on a medical examination dataset (`medical_examination.csv`) containing patient health and lifestyle records.
You can download it from here; https://github.com/chapamchivi/cardiovascular-disease-dataset

## Key Features
- BMI-based overweight classification
- Normalization of cholesterol and glucose levels
- Categorical bar plots comparing health factors by cardiovascular condition
- Correlation heatmap for numerical health measurements
- Data cleaning to remove implausible or extreme values

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Visualizations
- **Categorical Plot:** Displays counts of health and lifestyle indicators split by cardiovascular disease status.
- **Heatmap:** Shows correlations between medical measurements after data cleaning.

## How to Run
1. Ensure required libraries are installed:
   ```bash
   pip install pandas numpy matplotlib seaborn
