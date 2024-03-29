from geopy.geocoders import Nominatim
import streamlit as st

locator = Nominatim(user_agent = 'geocoder-dev-2024')
st.header('Information Zone')

def dispatch_action(loc):
    global locator
    location = locator.geocode(loc)
    st.write(f"Address: { location.address }") 
    st.write(f"Altitude: { location.altitude }")
    st.write(f"Point: { location.point }") 
    st.write(f"Longitude: { location.longitude }, Latitude: { location.latitude }")    

def init_app_geocoder():
    with st.form("input-form", clear_on_submit=True, border=True):
        st.write('Input Form')
        loc = st.text_input(label = 'Location', placeholder = 'Type the Location here...')
        submitted =  st.form_submit_button('Search')
        if submitted: 
            dispatch_action(loc)

st.header('Search Result')
init_app_geocoder()