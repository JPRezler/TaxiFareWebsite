import streamlit as st
import requests
'''
# TaxiFareModel in NY
'''

st.markdown('''
            You want to know what is the fare price of your drive in NY, you are on the right page
            ''')
'''
Enter below your pick time, pickup and drop off place, and number of passengers:
'''
pickup_datetime = st.text_input('Pick Up Time', '2013-07-06 17:18:00')
pickup_longitude = st.text_input('Pick Up Longitude', '-73.950655')
pickup_latitude = st.text_input('Pick Up Latitude', '40.783282')
dropoff_longitude = st.text_input('Dropoff Longitude', '-73.984365')
dropoff_latitude = st.text_input('Dropoff Latitude', '40.769802')
passenger_count = st.text_input('passenger_count', '1')

params = {
'pickup_datetime':pickup_datetime,
'pickup_longitude':pickup_longitude,
'pickup_latitude':pickup_latitude,
'dropoff_longitude':dropoff_longitude,
'dropoff_latitude':dropoff_latitude,
'passenger_count':passenger_count
}



url = ' https://taxifare-5vxhixo52q-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

req=requests.get(url, params=params).json()
price = round(req['pred'],2)

'''
## The estimated price is 
'''
price
'''USD'''