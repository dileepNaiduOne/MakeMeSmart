import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs import *
from dotenv import load_dotenv 
import pymysql
import os

st.set_page_config(layout="wide")

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>', unsafe_allow_html= True)

st.image(r"./img/logo-light.svg", width=70)

def add_user_data_to_charts(ss):
    load_dotenv()

    db = pymysql.connect(
        host = os.getenv("MYSQL_ADDON_HOST"),
        user = os.getenv("MYSQL_ADDON_USER"),
        password = os.getenv("MYSQL_ADDON_PASSWORD"),
        database=os.getenv("MYSQL_ADDON_DB")
    )

    mycursor = db.cursor()

    mycursor.execute(f"truncate table charts")
    db.commit()
    mycursor.execute(f"insert into charts select date, topic, dificulty, score from scores where secret_sentence like '{ss}';")
    db.commit()

    mycursor.execute(f"select * from charts;")
    return mycursor


if "user_data" not in st.session_state:
    charts = {
        "date" : [],
        "topic" : [],
        "dificulty" : [],
        "score" : []
    }

    for i in add_user_data_to_charts("iam"):
        charts["date"].append(i[0])
        charts["topic"].append(i[1])
        charts["dificulty"].append(i[2])
        charts["score"].append(i[3])

    user_data = pd.DataFrame(charts)
    st.write(user_data)

def draw_line_plot(d):
    fig = px.line(
        d,
        x="date",
        y="score",
        markers=True,
        text="score",
        title="Performance Over Time",
    )
    fig.update_traces(textposition="top center")
    st.plotly_chart(fig, use_container_width=True)


# draw_line_plot(user_data[["date", "score"]])

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