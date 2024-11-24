import streamlit as st
from streamlit_confetti import confetti
import time


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.image(r"./img/logo-light.svg", width=70)

st.title("Tableau Charts will come here 😉")