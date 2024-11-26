st.set_page_config(layout="wide")

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PythonScipts.database_tasks import add_user_data_to_charts
from plotly.graph_objs import *



with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>', unsafe_allow_html= True)

st.image(r"./img/logo-light.svg", width=70)

st.title("Charts will come here")


if "user_data" not in st.session_state:
    charts = {
        "date" : [],
        "topic" : [],
        "dificulty" : [],
        "score" : []
    }

    for i in add_user_data_to_charts(st.session_state.person["secret_sentence"]):
        charts["date"].append(i[0])
        charts["topic"].append(i[1])
        charts["dificulty"].append(i[2])
        charts["score"].append(i[3])

    st.session_state.user_data = pd.DataFrame(charts)

st.write(st.session_state.user_data)
## -----------------------------------------------------------------
## -----------------------------------------------------------------

one, two = st.columns([8, 2], vertical_alignment="center")
three, four = st.columns([7, 3], vertical_alignment="center")

with one:
    one_c = st.container(border=True)
    with one_c:
        st.write("One")

with two:
    two_c = st.container(border=True)
    with two_c:
        st.write("two")

with three:
    three_c = st.container(border=True)
    with three_c:
        three_1, three_2, three_3, three_4 = st.columns(4, vertical_alignment="center")
        with three_1:
            three_c_1 = st.container(border=True)
            with three_c_1:
                st.write("three 1")

        with three_2:
            three_c_2 = st.container(border=True)
            with three_c_2:
                st.write("three 2")

        with three_3:
            three_c_3 = st.container(border=True)
            with three_c_3:
                st.write("three 3")

        with three_4:
            three_c_4 = st.container(border=True)
            with three_c_4:
                st.write("three 4")
        

with four:
    four_c = st.container(border=True)
    with four_c:
        st.write("four")




return_button = st.button(label="BACK TO HOME", type="primary")

if return_button:
    st.switch_page("papers/home.py")