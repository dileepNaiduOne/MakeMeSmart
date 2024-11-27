import streamlit as st
from streamlit_confetti import confetti
import time


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)



st.image(r"./img/logo-light.svg", width=70)

st.title("Uh-oh 😟", anchor=False)
st.markdown("### You should not have reloaded the page. :red[Don't Reload Next Time]")
st.write("\n")
st.write("\n")
st.write("\n")

a = st.empty()

for i in range(10, 0, -1):
    a.write(f"Redirecting to start page...   :red[{i} Seconds left]")
    time.sleep(1)

for key in st.session_state.keys():
    del st.session_state[key]

st.switch_page("papers/start.py")