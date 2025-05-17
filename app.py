import streamlit as st
import numpy as np
import pickle

# Load the saved model
with open('linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("House Price Predictor")

# Input fields (same as before)
squareMeters = st.number_input('Square Meters', min_value=10, max_value=100000, value=500)
numberOfRooms = st.number_input('Number of Rooms', min_value=1, max_value=100, value=3)
hasYard = st.selectbox('Has Yard', [0, 1])
hasPool = st.selectbox('Has Pool', [0, 1])
floors = st.number_input('Number of Floors', min_value=1, max_value=10, value=1)
cityCode = st.number_input('City Code', min_value=1000, max_value=100000, value=75000)
cityPartRange = st.number_input('City Part Range', min_value=1, max_value=10, value=5)
numPrevOwners = st.number_input('Number of Previous Owners', min_value=0, max_value=10, value=1)
made = st.number_input('Year Made', min_value=1800, max_value=2025, value=2000)
isNewBuilt = st.selectbox('Is New Built', [0, 1])
hasStormProtector = st.selectbox('Has Storm Protector', [0, 1])
basement = st.number_input('Basement Size (sqm)', min_value=0, max_value=5000, value=0)
attic = st.number_input('Attic Size (sqm)', min_value=0, max_value=5000, value=0)
garage = st.number_input('Garage Size', min_value=0, max_value=5000, value=0)
hasStorageRoom = st.selectbox('Has Storage Room', [0, 1])
hasGuestRoom = st.number_input('Number of Guest Rooms', min_value=0, max_value=10, value=0)

if st.button('Predict Price'):
    input_features = np.array([[squareMeters, numberOfRooms, hasYard, hasPool, floors, cityCode,
                                cityPartRange, numPrevOwners, made, isNewBuilt, hasStormProtector,
                                basement, attic, garage, hasStorageRoom, hasGuestRoom]])
    predicted_price = model.predict(input_features)[0]
    st.success(f'Estimated House Price: €{predicted_price:,.2f}')
