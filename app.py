import streamlit as st
import pandas as pd
import numpy as np
import joblib
# Load pre-trained models and encoders
scaler = joblib.load("scaler.pkl")
best_model = joblib.load("best_model.pkl")
# Define the prediction function
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_data = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                              columns=["N", "P", "K", "temperature", "humidity", "ph", "rainfall"])
    input_data = scaler.transform(input_data)  # Standardize input
    prediction = best_model.predict(input_data)[0]
    return prediction
# Streamlit UI
st.title("🌱 Crop Recommendation System")

st.sidebar.header("Enter Soil and Weather Parameters")

# User input fields
N = st.sidebar.number_input("Nitrogen (N)", min_value=0, max_value=200, value=50)
P = st.sidebar.number_input("Phosphorus (P)", min_value=0, max_value=200, value=50)
K = st.sidebar.number_input("Potassium (K)", min_value=0, max_value=200, value=50)
temperature = st.sidebar.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=25.0)
humidity = st.sidebar.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=70.0)
ph = st.sidebar.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.sidebar.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=200.0)

# Prediction button
if st.sidebar.button("Predict Crop"):
    recommended_crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
    st.success(f"🌾 Recommended Crop: *{recommended_crop}*")

if recommended_crop.lower() == "rice":
        st.image("rice.jpg", caption="Recommended Crop: Rice", use_container_width=True)
elif recommended_crop.lower() == "apple":
        st.image("apple.jpeg", caption="Recommended Crop: Apple", use_container_width=True)
elif recommended_crop.lower() == "papaya":
        st.image("papaya.webp", caption="Recommended Crop:Papaya", use_container_width=True)
elif recommended_crop.lower() == "maize":
        st.image("maize.jpeg", caption="Recommended Crop:Banana", use_container_width=True)
elif recommended_crop.lower() == "orange":
        st.image("orange.jpg", caption="Recommended Crop:Orange", use_container_width=True)
elif recommended_crop.lower() == "coconuts":
        st.image("coconuts.jpg", caption="Recommended Crop:Coconut", use_container_width=True)
elif recommended_crop.lower() == "cotton":
        st.image("cotton.jpg", caption="Recommended Crop:Cotton", use_container_width=True)
elif recommended_crop.lower() == "coffee":
        st.image("coffee.jpg", caption="Recommended Crop:Coffee", use_container_width=True)

elif recommended_crop.lower() == "grapes":
    st.image("grapes.jpg", caption="Recommended Crop:Grapes", use_container_width=True)
elif recommended_crop.lower() == "chickpea":
    st.image("chickpea.jpg", caption="Recommended Crop:Chickpea", use_container_width=True)
elif recommended_crop.lower() == "blackgram":
    st.image("blackgram.jpg", caption="Recommended Crop:Blackgram", use_container_width=True)
elif recommended_crop.lower() == "jute":
    st.image("jute.jpg", caption="Recommended Crop:Jute", use_container_width=True)
elif recommended_crop.lower() == "kidneybeans":
    st.image("kidneybeans.jpg", caption="Recommended Crop:Kidneybeans", use_container_width=True)
elif recommended_crop.lower() == "lentil":
    st.image("lentil.jpg", caption="Recommended Crop:Lentil", use_container_width=True)
elif recommended_crop.lower() == "maize":
    st.image("maize.jpg", caption="Recommended Crop:Maize", use_container_width=True)
elif recommended_crop.lower() == "mango":
    st.image("mango.jpg", caption="Recommended Crop:Mango", use_container_width=True)
elif recommended_crop.lower() == "moskmelon":
    st.image("moskmelon.jpg", caption="Recommended Crop:Moskmelon", use_container_width=True)
elif recommended_crop.lower() == "mothbeans":
    st.image("mothbeans.jpg", caption="Recommended Crop:Mothbeans", use_container_width=True)
elif recommended_crop.lower() == "mungbean":
    st.image("mungbean.jpg", caption="Recommended Crop:Mungbean", use_container_width=True)
elif recommended_crop.lower() == "pigeonpeas":
    st.image("pigeonpeas.jpg", caption="Recommended Crop:Pigeonpeas", use_container_width=True)
elif recommended_crop.lower() == "pomegranate":
    st.image("pomegranate.jpg", caption="Recommended Crop:Pomegranate", use_container_width=True)
elif recommended_crop.lower() == "watermelon":
    st.image("watermelon.jpg", caption="Recommended Crop:Watermelon", use_container_width=True)
