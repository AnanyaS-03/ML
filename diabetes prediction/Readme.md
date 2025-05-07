# 🩺 Diabetes Prediction System

A machine learning-based system to predict the likelihood of diabetes in individuals based on personal and medical history data. Built using **Python**, **Pandas**, **Scikit-learn**, and the **Random Forest Classifier**.

---

## 📌 Project Overview

This project uses a dataset containing various health-related features to predict whether an individual is likely to be diabetic. The system preprocesses the data, encodes categorical variables, applies feature scaling, and uses a Random Forest model for classification.

---

## 🧠 Machine Learning Pipeline

- **Model**: Random Forest Classifier (n_estimators = 100, max_depth = 8)
- **Encoding**: Label Encoding for categorical features like gender and smoking history
- **Scaling**: StandardScaler used to normalize numerical features
- **Split Ratio**: 80% training, 20% testing
- **Evaluation**: Accuracy Score and Classification Report

---

## 🗃️ Dataset Description

- **Filename**: `diabetes_prediction_dataset.csv`
- **Size**: ~1000+ records (based on assumption)
- **Target Column**: `diabetes` (Binary: 1 = Yes, 0 = No)

### 🎯 Features:

- `gender`
- `age`
- `hypertension`
- `heart_disease`
- `smoking_history`
- `bmi`
- `HbA1c_level`
- `blood_glucose_level`

---


