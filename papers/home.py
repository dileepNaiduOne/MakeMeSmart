import streamlit as st
from PythonScipts.database_tasks import *

# st.set_page_config(page_title="Sign-Up Form", layout="centered")


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------



st.image(r"./img/logo-dark.svg", width=700)

st.write("\n")
st.write("\n")

col1, _1, col2, _2, col3 = st.columns([2, 0.1, 2, 0.1, 2])


with col1:
    st.button("PLAY QUIZ", use_container_width=True, type="primary", on_click=st.switch_page("papers/topic.py"))

with col2:
    st.button("MY STATS", use_container_width=True, type="primary")

with col3:
    st.button("LOG OUT", use_container_width=True, type="primary")