import streamlit as st
import requests



st.set_page_config(
    page_title="NY Taxi Fare ", # => Quick reference - Streamlit
    page_icon="🚕") # collapsed

# page_bg_img = '''
# <style>
# h1 {
#     color: red;
# }
# body {
# background-image: url("https://as1.ftcdn.net/jpg/00/44/84/68/500_F_44846834_q8DqmWHbHvodkWvYjZvZzA1esHPsBUBr.jpg");
# background-size: cover;
# }
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)

CSS = """
h1 {
    color: red;
}
body {
    body-image: url(https://as1.ftcdn.net/jpg/00/44/84/68/500_F_44846834_q8DqmWHbHvodkWvYjZvZzA1esHPsBUBr.jpg);
    body-size: cover;
}
"""
st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)

'''
# TaxiFareModel in NY
'''

st.markdown('''
            ## You want to know what is the fare price of your drive in NY, you are on the right page
            ''')
'''
Enter below your pick time, pickup and drop off place, and number of passengers:
'''
pickup_datetime = st.text_input('Pick Up Time', '2013-07-06 17:18:00')
pickup_longitude = st.text_input('Pick Up Longitude', '-73.950655')
pickup_latitude = st.text_input('Pick Up Latitude', '40.783282')
dropoff_longitude = st.text_input('Dropoff Longitude', '-73.984365')
dropoff_latitude = st.text_input('Dropoff Latitude', '40.769802')
# passenger_count = st.text_input('passenger_count', '1')
passenger_count = st.number_input(label='passenger_count',
min_value=1,
max_value=6,
value=1,
step=1
)

params = {
'pickup_datetime':pickup_datetime,
'pickup_longitude':pickup_longitude,
'pickup_latitude':pickup_latitude,
'dropoff_longitude':dropoff_longitude,
'dropoff_latitude':dropoff_latitude,
'passenger_count':passenger_count
}



url_api = ' https://taxifare-5vxhixo52q-ew.a.run.app/predict'

if url_api == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

req=requests.get(url_api, params=params).json()
price = round(req['pred'],2) + 2*int(passenger_count/4)
st.markdown(f'# The estimated price is {price} USD')

