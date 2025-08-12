import streamlit as st
from PythonScipts.database_tasks import *

# st.set_page_config(page_title="Sign-Up Form", layout="centered")


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

try:

    st.title(f":gray[Hi,] :red[{st.session_state.person["name"]}!]", anchor=False)
    st.image(r"./img/logo-dark.svg", width=700)


    st.write("\n")
    st.write("\n")

    col1, a1, col2, a2, col3 = st.columns([2, 0.1, 2, 0.1, 2])


    with col1:
        b1 = st.button("PLAY QUIZ", use_container_width=True, type="primary")
        if b1:
            st.switch_page("papers/topic.py")

    with col2:
        b2 = st.button("MY STATS", use_container_width=True, type="primary")
        if b2:
            st.switch_page("papers/charts.py")

    with col3:
        b3 = st.button("LOG OUT", use_container_width=True, type="primary")
        if b3:
            for key in st.session_state.keys():
                del st.session_state[key]
            st.switch_page("papers/start.py")

    st.write("\n")
    st.write("\n")
    
    st.caption(":red[Caution] : :gray[This app is using Gemini 2.5 Pro. The odds of an LLM slip-up are super low, but hey, always stay sharp!!!]")

except KeyError:
    st.switch_page("papers/reload.py")

except AttributeError:
    st.switch_page("papers/reload.py")
