import streamlit as st
import pandas as pd
import pickle

st.header('Car Price Prediction App')

#df=pd.read_csv('car_price.csv')
#st.dataframe(df)

#inputs from user

col1, col2= st.columns(2)

with col1:
    seats = st.selectbox(
        'Enter the number of seats: ',
        [4, 5, 7, 9, 11])

with col2:
    fuel_type_inp= st.selectbox(
        'Enter the Fuel Type: ',
        ('Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'))

col1, col2= st.columns(2)
with col1:
    transmission_inp= st.selectbox(
        'Enter the Transmission Type: ',
        ('Manual', 'Automatic'))
with col2:
    engine= st.slider('Engine CC', 500, 5000, 100)


encode_dict = {
    "fuel_type": {'Diesel': 1, 'Petrol': 2, 'CNG': 3, 'LPG': 4, 'Electric': 5},
    "transmission_type": {'Manual': 1, 'Automatic': 2}
}

#relation building is left
def model_pred(fuel_type_encoded,transmission_encoded, engine,seats ):
    with open("model_file", 'rb') as file:
        model = pickle.load(file)
        input_features = [[2014,2,130000,fuel_type_encoded,transmission_encoded,19.7,engine,46.3,seats]]
        return model.predict(input_features)


if st.button('Predict'):
    fuel_type_encoded= encode_dict['fuel_type'][fuel_type_inp]
    transmission_encoded= encode_dict['transmission_type'][transmission_inp]

    second_hand_price=model_pred(fuel_type_encoded,transmission_encoded, engine,seats)
    formatted_price = round(second_hand_price[0] * 1_000_000, 2)  # assuming normalized, scale appropriately

    st.markdown(
        f"""
        <div style="background-color:#f0f2f6;padding:20px;border-radius:10px">
            <h3 style="color:#0a9396;">💰 Estimated Second-hand Car Price</h3>
            <h1 style="color:#001219;">₹ {formatted_price:,.2f}</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
