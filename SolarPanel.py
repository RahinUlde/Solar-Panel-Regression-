# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 16:49:32 2025

@author: DELL
"""

import streamlit as st
import joblib
import numpy as np

# Load the saved Random Forest pipeline model
with open("solarPanel_pipeline.pkl", "rb") as f:
    model = joblib.load(f)

# -------------------
# Streamlit UI
# -------------------
st.set_page_config(page_title="Solar Power Prediction", page_icon="⚡", layout="centered")

# Title & description
st.title("⚡ Solar Power Prediction App")
st.markdown(
    """
    This app predicts **solar power generation** based on weather conditions.  
    Adjust the inputs in the sidebar and click **Predict** to see the results.  
    """
)

# Sidebar inputs
st.sidebar.header("🔧 Input Weather Features")

distance_to_noon = st.sidebar.slider("Distance to Solar Noon (hrs)", min_value=0.0, max_value=4.0, step=0.1)
temperature = st.sidebar.slider("Temperature (°C)", min_value=20.0, max_value=80.0, step=0.5)
wind_direction = st.sidebar.slider("Wind Direction (°)", min_value=0, max_value=100, step=5)
wind_speed = st.sidebar.slider("Wind Speed (m/s)", min_value=0.0, max_value=30.0, step=0.1)
sky_cover = st.sidebar.slider("Sky Cover (%)", min_value=0, max_value=40, step=1)
humidity = st.sidebar.slider("Humidity (%)", min_value=0, max_value=100, step=1)
avg_wind_speed = st.sidebar.slider("Average Wind Speed (period, m/s)", min_value=0.0, max_value=40.0, step=0.1)
avg_pressure = st.sidebar.slider("Average Pressure (hPa)", min_value=25.0, max_value=250.0, step=0.5)

# Collect input features
features = np.array([[distance_to_noon, temperature, wind_direction, wind_speed,
                      sky_cover, humidity, avg_wind_speed, avg_pressure]])

# Predict button
if st.sidebar.button("⚡ Predict Power Generation"):
    prediction = model.predict(features)
    st.success(f"🔋 Estimated Power Generated: **{prediction[0]:.2f} kW**")
    # Show PNG image at the top
    st.image("solar.png", caption="Solar Energy Prediction", use_container_width=True)
    st.snow()  # 🎈 nice animation effect
