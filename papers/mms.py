import streamlit as st
from PythonScipts.database_tasks import *
from PythonScipts.makemesmart_generater import make_me_smart

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

try:

    st.image(r"./img/logo-light.svg", width=100)
    if "text_shown" not in st.session_state:
        st.write(make_me_smart(st.session_state["input_topic"], st.session_state["check_list"]))
        st.session_state["text_shown"] = True


    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    return_button = st.button("RETURN TO HOME", type="primary")

    if return_button:
        st.switch_page("papers/home.py")

except KeyError:
    st.switch_page("papers/reload.py")

except AttributeError:
    st.switch_page("papers/reload.py")
