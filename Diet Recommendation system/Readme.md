# 🥗 Diet Recommendation System

A personalized diet recommendation system that predicts ideal body weight and daily calorie needs based on user input such as age, height, and weight. It provides food suggestions and weight management goals tailored to vegetarian or non-vegetarian preferences.

---

## 📌 Overview

This system uses a machine learning approach with **Random Forest Regression** to estimate:

- ✅ Ideal Weight (in kg)
- 🔥 Daily Calorie Requirement (in kcal)
- 🥗 Recommended Foods
- 🚫 Foods to Avoid
- 🎯 Personalized Weight Goals (Gain / Maintain / Lose)

---

## 🔧 Technologies Used

- **Python**
- **Streamlit** for web UI
- **Pandas** for data handling
- **Scikit-learn** for modeling and preprocessing

---

## 🧠 ML Workflow

- **Model**: RandomForestRegressor
- **Features Used**:
  - Weight (kg)
  - Height (cm)
  - Age
- **Targets Predicted**:
  - Ideal Weight
  - Daily Calorie Intake
- **Scaling**: StandardScaler used to normalize input features

---

## 📁 Dataset Description

- **File**: `diet_recommendation_corrected_calories.csv`
- **Columns**:
  - `Weight (kg)`
  - `Height (cm)`
  - `Age`
  - `Ideal Weight (kg)`
  - `Calories`

## OUTPUT
![OUTPUT](https://github.com/AnanyaS-03/ML/blob/main/Diet%20Recommendation%20system/Screenshot%202025-05-08%20000345.png?raw=true)

