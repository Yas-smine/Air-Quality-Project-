import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load("rf_air_quality_model.pkl")
scaler = joblib.load("scaler.pkl")
le = joblib.load("label_encoder.pkl")
# Feature list

features = [
    "PT08.S1(CO)",
    "C6H6(GT)",
    "PT08.S2(NMHC)",
    "NOx(GT)",
    "PT08.S3(NOx)",
    "NO2(GT)",
    "PT08.S4(NO2)",
    "PT08.S5(O3)",
    "T",
    "RH",
    "AH"
]

# Map predicted classes to readable levels
level_map = {
    "Low": "Good",
    "Medium": "Moderate",
    "High": "Bad "
}
st.title("Air Quality Level Prediction 🌫️")

st.write("""
This app predicts the **air quality level** (Low, Medium, High) based on sensor readings and weather conditions.
""")

# Input fields for each feature
input_data = {}
for feature in features:
    value = st.number_input(f"{feature}", value=0.0)
    input_data[feature] = value

# Convert input to DataFrame
input_df = pd.DataFrame([input_data])

# Scale the features
input_scaled = scaler.transform(input_df)

# Prediction button
if st.button("Predict Air Quality Level"):
    prediction = model.predict(input_scaled)
    predicted_class = le.inverse_transform(prediction)[0]  # Convert 0/1/2 → Low/Medium/High
    st.success(f"Predicted Air Quality Level: {predicted_class} → {level_map[predicted_class]}")

