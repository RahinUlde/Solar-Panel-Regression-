# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 16:49:32 2025

@author: DELL
"""
import streamlit as st
import joblib
import pandas as pd

# Load trained RandomForest model with preprocessing pipeline
model = joblib.load("solarPanel_pipeline.pkl")

st.title("⚡ Solar Power Prediction App")
st.write("Enter the conditions to predict solar power generation.")

# Input fields for each feature
distance_to_solar_noon = st.number_input("Distance to Solar Noon (hours)", value=1.0)
temperature = st.number_input("Temperature (°C)", value=25.0)
wind_direction = st.number_input("Wind Direction (degrees)", value=180.0)
wind_speed = st.number_input("Wind Speed (m/s)", value=5.0)
sky_cover = st.number_input("Sky Cover (%)", value=50.0)
humidity = st.number_input("Humidity (%)", value=50.0)
avg_wind_speed_period = st.number_input("Average Wind Speed (period) (m/s)", value=5.0)
avg_pressure_period = st.number_input("Average Pressure (period) (hPa)", value=1013.0)

# Collect input into DataFrame
input_data = pd.DataFrame(
    [[distance_to_solar_noon, temperature, wind_direction, wind_speed,
      sky_cover, humidity, avg_wind_speed_period, avg_pressure_period]],
    columns=[
        "distance-to-solar-noon",
        "temperature",
        "wind-direction",
        "wind-speed",
        "sky-cover",
        "humidity",
        "average-wind-speed-(period)",
        "average-pressure-(period)"
    ]
)

# Predict button
if st.button("🔮 Predict Power Generated"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Power Generated: **{prediction[0]:.2f} kW**")
