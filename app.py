import streamlit as st
import pandas as pd
from joblib import load

log_reg = load("log_reg.joblib")
#dec_tree = load("dec_tree.joblib")
#random_forest = load("random_forest.joblib")
ridge = load("ridge.joblib")
svc = load("svc.joblib")

st.title("Classifying Habitable Exoplanets")
st.write("A planet’s habitability is determined by the planet’s composition, its location, and the properties of its host star. These properties can be detected using the planet’s emission spectrum, which is the frequencies of electromagnetic radiation a planet emits. Factors that influence a planet’s ability to sustain life include temperature, radius, mass, and orbit. These factors impact the presence of liquid water, an atmosphere, and the necessary chemical reactions for life. The host star determines the location of the habitable zone, which is where the temperature and radiation are sufficient to sustain life. Other properties of the host star, such as mass, radius, star type, and metallicity also affect the location of the habitable zone. Due to the multitude of factors affecting habitability, this problem is suited for machine learning algorithms.")
st.write("This app detects if an exoplanet is potentially habitable.")
st.write("Enter the following values for the planet.")

mass = st.number_input("Planet Mass (in terms of Earth mass)", value=4.155456)
radius = st.number_input("Planet Radius (in terms of Earth radius)", value=1.87)
temp = st.number_input("Planet temperature (K)", value=277.27227)
eccentricity = st.number_input("Orbital Eccentricity", value=0.0)
period = st.number_input("Orbital Period (days) ", value=28.1656)
axis = st.number_input("Planet Orbit Semi-Major Axis (au)", value=0.13456)
insolation = st.number_input("Insolation Flux (in terms of Earth flux) ", value=1.4029627)
metallicity = st.number_input("Star Metallicity (dex)", value=0.0)
s_mass = st.number_input("Star Mass (in terms of the sun's mass)", value=0.41)
star_type = st.text_input("Star Type (O, B, A, F, G, K, M)", value="M")
s_temp = st.number_input("Star Temperature (in terms of the sun's temperature)", value=3772.0)
s_radius = st.number_input("Star Radius (in terms of the sun's radius)", value=0.37424099)

if star_type == "B":
    s_type = 183
if star_type == "A":
    s_type = 180
if star_type == "F":
    s_type = 80
if star_type == "G":
    s_type = 30
if star_type == "K":
    s_type = 82
if star_type == "M":
    s_type = 185
else:
    s_type = 0

input_features = [[mass, radius, temp, eccentricity, period, metallicity, s_mass, axis, insolation, s_type, s_temp, s_radius]]

pred = log_reg.predict(input_features)

st.header("Result: ")
if pred == 0:
    st.write("This exoplanet is not habitable.")
else:
    st.write("This exoplanet is potentially habitable.")
