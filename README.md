# 🏠 Bengaluru House Price Prediction App

This is a machine learning web app built with **Streamlit** that predicts house prices in **Bengaluru** based on user inputs like location, area (sqft), number of bedrooms (BHK), and number of bathrooms.

🔗 **Live App:**  
[Predict Price of the House](https://housepriceprediction-ausj9u22hwtiek458mpzor.streamlit.app/)

---

## 📌 About the Project

This project is based on the Bengaluru housing dataset and follows the end-to-end ML workflow:

- Data cleaning and preprocessing
- Feature engineering (e.g., one-hot encoding for location)
- Model training with different regressors
- Building a pipeline using `scikit-learn`
- Exporting the trained model using `joblib`
- Creating an interactive web interface using Streamlit

---

## 🛠 Features

✅ User-friendly UI with dropdowns and number inputs  
✅ Predicts price in Lakhs based on BHK, bathrooms, location, and sqft  
✅ Fast and efficient prediction using a trained `RandomForestRegressor` pipeline  
✅ Hosted for free on Streamlit Cloud  
✅ Easily shareable public link  

---



## 📂 Files in This Repository

| File                  | Purpose                                           |
|-----------------------|---------------------------------------------------|
| `app.py`              | Streamlit app code                                |
| `requirements.txt`    | Lists all Python dependencies                     |
| `house_price_model.pkl` | Serialized machine learning pipeline            |
| `location_list.pkl`   | List of all unique locations used for dropdown UI |


