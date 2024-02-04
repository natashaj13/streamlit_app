import streamlit as st
import pandas as pd
from joblib import load

log_reg = load("log_reg.joblib")
#dec_tree = load("dec_tree.joblib")
#random_forest = load("random_forest.joblib")
ridge = load("ridge.joblib")
svc = load("svc.joblib")

st.title("Classifying Habitable Exoplanets")
st.write("This app detects if an exoplanet is potentially habitable.")
st.write("Enter the following values for the planet.")

mass = st.number_input("Planet Mass: ")
radius = st.number_input("Planet Radius: ")
temp = st.number_input("Planet Temperature: ")
eccentricity = st.number_input("Orbital Eccentricity: ")
period = st.number_input("Orbital Period: ")
axis = st.number_input("Planet Semi-Major Axis: ")
insolation = st.number_input("Insolation Flux: ")
metallicity = st.number_input("Star Metallicity: ")
s_mass = st.number_input("Star Mass: ")
star_type = st.text_input("Star Type (O, B, A, F, G, K, M)")
s_temp = st.number_input("Star Temperature: ")
s_radius = st.number_input("Star Radius: ")

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
