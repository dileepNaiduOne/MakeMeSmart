import streamlit as st
from streamlit_confetti import confetti
import time

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.image(r"./img/logo-light.svg", width=70)

st.title(f"{st.session_state["user_name"]}, You Scored", anchor=False)
st.title(f":red[{st.session_state["Score"]}]/10", anchor=False)
st.title(f"in '{st.session_state["input_topic"]}'", anchor=False)

return_button = st.button(label="Back to Home", type="primary")

if return_button:
    st.switch_page("papers/topic.py")

