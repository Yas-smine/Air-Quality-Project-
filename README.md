# Air Quality Level Prediction

## Project Overview
This project predicts the **air quality level** (Low, Medium, High) using sensor readings, pollutant concentrations, and meteorological variables from the **Air Quality UCI Dataset**.  
The goal is to build a machine learning model capable of identifying air pollution levels in real-time and deploy it via an interactive **Streamlit app**.

---

## Dataset
- **Features:**
  - Gas sensors: PT08.S1(CO), PT08.S2(NMHC), PT08.S3(NOx), PT08.S4(NO2), PT08.S5(O3)
  - Pollutants: CO(GT), NMHC(GT), C6H6(GT), NOx(GT), NO2(GT)
  - Meteorology: Temperature (T), Relative Humidity (RH), Absolute Humidity (AH)
  - Date: Day, Month, Year
- **Target variable:**
  - `Air_Quality_Level` derived from CO(GT) values: Low, Medium, High

---

## Methodology

### Data Preprocessing
- Replace missing values (`-200`) with NaN and impute using median.
- Convert numeric columns with commas to proper floats.
- Generate the `Air_Quality_Level` target from CO(GT).
- Exclude CO(GT) from features to avoid leakage.

### Feature Selection
- Used all sensor readings, other pollutant concentrations, and meteorological variables as predictors.

### Model Selection
- Tested **Random Forest Classifier**, **Logistic Regression**, and **Decision Tree**.
- **Random Forest** chosen for its **high accuracy**, robustness to feature scaling, and ability to handle non-linear relationships.

---

## Model Evaluation
- Split: 80% training, 20% testing.
- Metrics:
  - **Accuracy:** 92%
  - **Weighted F1-score:** 0.92
  - **Precision & Recall:**
    - Low: High precision & recall (~95–96%)
    - Medium: Balanced (~88%)
    - High: Lower recall (~65%) due to class imbalance
- **Confusion Matrix:** Most errors occur between Medium and High pollution levels.

---

## Challenges & Solutions
- **Class imbalance:** High pollution cases are few, causing lower recall.  
  **Solution:** Acknowledge limitation; could use SMOTE or class weighting in future work.
- **Missing values (-200) and inconsistent formatting:**  
  **Solution:** Replaced with median and standardized numeric columns.
- **Feature mismatch in Streamlit deployment:**  
  **Solution:** Ensure exact feature names and order match training, save and load LabelEncoder for predictions.

---

## Streamlit Application
- Interactive input of sensor and meteorological variables.
- Predicts **Air Quality Level** and converts it to a friendly description:
  - Low → Good 😊
  - Medium → Moderate 😐
  - High → Bad ⚠️
- Automatically scales inputs and predicts with the trained Random Forest model.

---

## Conclusion
- The Random Forest model achieves **high accuracy** in predicting air quality levels using independent sensor measurements.
- Predictions are **very reliable** for Low and Medium pollution, slightly less for High pollution due to data imbalance.
- The Streamlit app demonstrates a practical deployment, allowing **real-time predictions** from new measurements.
- Future improvements include official AQI calculations, balancing classes, and enhanced visualizations.

---



