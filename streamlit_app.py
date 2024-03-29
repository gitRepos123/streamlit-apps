from geopy.geocoders import Nominatim
import streamlit as st
import pandas as pd

st.title("GeoPin")
locator = Nominatim(user_agent = 'geocoder-dev-2024')

def dispatch_action(loc):
    global locator
    st.header('Search Result')
    location = locator.geocode(loc)
    if location != None:
        st.write(f"Address: { location.address }") 
        st.write(f"Altitude: { location.altitude }")
        st.write(f"Point: { location.point }") 
        st.write(f"Longitude: { location.longitude }, Latitude: { location.latitude }")  
        st.header("See Map")
        st.map(data = pd.DataFrame({ 'lat': [ location.latitude ], 'lon': [ location.longitude ] }), size = 20.0, color =  "#0000ff", zoom = 0.1)

def init_app_geocoder():
    with st.form("input-form", clear_on_submit=True, border=True):
        st.write('Input Form')
        loc = st.text_input(label = 'Location', placeholder = 'Type the Location here...')
        submitted =  st.form_submit_button('Search')
        if submitted: 
            dispatch_action(loc)

init_app_geocoder()
