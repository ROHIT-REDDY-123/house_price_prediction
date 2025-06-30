import streamlit as st
import pandas as pd
import joblib

# Load model and location list
pipe = joblib.load("house_price_model.pkl")
locations = joblib.load("location_list.pkl")

st.title("🏠 Bengaluru House Price Predictor")

st.write("Enter the details below to estimate the house price.")

# UI inputs
location = st.selectbox("📍 Location", sorted(locations))
bhk = st.selectbox("🛏️ Bedrooms (BHK)", [1, 2, 3, 4, 5])
bath = st.selectbox("🛁 Bathrooms", [1, 2, 3, 4])
sqft = st.number_input("📐 Total Square Feet", min_value=300.0, max_value=10000.0, step=50.0)

if st.button("💰 Predict Price"):
    input_df = pd.DataFrame([[location, sqft, bath, bhk]], columns=["location", "total_sqft", "bath", "bhk"])
    result = pipe.predict(input_df)[0]
    st.success(f"🏷️ Estimated Price: ₹ {result:.2f} Lakhs")
