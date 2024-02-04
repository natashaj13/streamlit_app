import streamlit as st
import pandas as pd
from joblib import load

log_reg = load("log_reg.joblib")
#dec_tree = load("dec_tree.joblib")
#random_forest = load("random_forest.joblib")
ridge = load("ridge.joblib")
svc = load("svc.joblib")

st.title("hi")

mass = st.number_input("mass: ")
radius = st.number_input("radius: ")
insolation = st.number_input("insolation: ")
temp = st.number_input("temp: ")
eccentricity = st.number_input("eccentricity: ")
period = st.number_input("period: ")
metallicity = st.number_input("metallicity: ")
s_mass = st.number_input("s_mass: ")
axis = st.number_input("axis: ")
s_type = st.number_input("s_type: ")
s_temp = st.number_input("s_temp: ")
s_radius = st.number_input("s_radius: ")

input_features = [[mass, radius, temp, eccentricity, period, metallicity, s_mass, axis, insolation, s_type, s_temp, s_radius]]

pred = log_reg.predict(input_features)
st.write(pred)