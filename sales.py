import numpy as np
import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder


# Load the model,
try:
    with open('rf_model.sav', 'rb') as file:
        loaded_model = pickle.load(file)
except FileNotFoundError as e:
    st.error(f"Model file not found: {e}")
    loaded_model = None

# Load LabelEncoders (Crucial!)
try:
    with open('label_encoders.pkl', 'rb') as file:
        label_encoders = pickle.load(file)
except FileNotFoundError:
    st.error("LabelEncoders file not found.  Make sure 'label_encoders.pkl' is in the correct location.")
    label_encoders = None
    
def main():
    st.title('Pa John Supper market Sales Prediction')

    col1, col2 = st.columns(2)
    # Input fields
    with col1:
        # Input for categorical feature
        customer = st.selectbox("Customer Type", ["Member", "Normal"])
        city_type = st.selectbox("City", ["Yangon", "Mandalay", "Naypyitaw"])
        branch = st.selectbox("Branch", ["A", "B", "C"])
        tax = st.number_input("Tax(5%)", min_value=0.0, value=300.0)

    with col2:
        product_line = st.selectbox("Product Type", ["Electronic accessories", "Fashion accessories", "Food and beverages", "Health and beauty", "Home and lifestyle", "Sports and travel"])
        gender = st.selectbox("Gender", ["Male", "Female"])
        quantity = st.number_input("Quantity", min_value=0.0, value=50.0)
       

    # --- Process Input Data and Make Prediction ---
    if st.button("Predict Sales"):
        if loaded_model is not None:  # Only check for the model

            input_data = pd.DataFrame({
                'Gender':[gender],
                'Branch': [branch],
                'Customer type': [customer],
                'Product line': [product_line],
                'City': [city_type],
                'Quantity': [quantity],
                'Tax 5%': [tax]
            })

            #Transform columns before passing to prediction
            for col in ['Gender','Branch', 'Customer type', 'Product line', 'City']:
                input_data[col] = label_encoders[col].transform(input_data[col])
            try:
                prediction = loaded_model.predict(input_data)
                st.success(f"Predicted Sales: {prediction[0]:.2f}")
            except Exception as e:
                st.error(f"Prediction failed: {e}")

        else:
            st.error("Model not loaded.  Please check the file path.")  # Simplified message


if __name__ == '__main__':
    main()