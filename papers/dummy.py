import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objs import *
from dotenv import load_dotenv 
import pymysql
import os

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

    for i in add_user_data_to_charts("walking"):
        charts["date"].append(i[0])
        charts["topic"].append(i[1])
        charts["dificulty"].append(i[2])
        charts["score"].append(i[3])

    user_data = pd.DataFrame(charts)
    st.write(user_data)

def draw_line_plot(d, key_value):
    fig = px.line(
        d,
        x="date",
        y="score",
        markers=True,
        text="score",
        title="Performance Over Time",
        labels=False,
    )
    fig.update_traces(textposition="top center", line=dict(color='#f25270'))
    fig.update_xaxes(tickvals=[d["date"].iloc[0], d["date"].iloc[-1]], ticktext=["Oldest", "Most Recent"], title_text="")
    fig.update_yaxes(showticklabels=False, title_text="SCORE")
    st.plotly_chart(fig, use_container_width=True, key=key_value)


def plot_gauge(indicator_number, indicator_title, key_value, indicator_suffix="", indicator_color="#f25270", max_bound=10):
    fig = go.Figure(
        go.Indicator(
            value=indicator_number,
            mode="gauge+number",
            domain={"x": [0, 1], "y": [0, 1]},
            number={
                "suffix": indicator_suffix,
                "font.size": 30,
            },
            gauge={
                "axis": {"range": [0, max_bound], "tickwidth": 1, 'visible': False},
                "bar": {"color": indicator_color}
            },
            title={
                "text": f"{indicator_title}<br><span style='font-size:0.7em;color:gray'>Highest Score</span><br>",
                "font": {"size": 18},
            },
        )
    )
    fig.update_layout(
        height=200,
        margin=dict(l=10, r=10, t=10, b=10, pad=8)
    )
    st.plotly_chart(fig, use_container_width=True, key=key_value)



def draw_pie_plot(d, key_value):
    fig = px.pie(d, values='Count', names=list(map(str.capitalize, list(d.index))),
             title='Attempts based on Dificulty',
             hover_data=["Mean"])
    fig.update_traces(textposition='inside', textinfo='percent+label',  marker=dict(colors=['#f25270', "#AFB1C0", '#cacbd5', '#F3F3F6']))
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig, use_container_width=True, key=key_value)


def draw_bar_chart(d, key_value):
    fig = px.bar(
        d,
        x="Topic",
        y="MeanScore",
        title="Topics wise Mean Score",
    )
    st.plotly_chart(fig, use_container_width=True, key=key_value)


##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################
##############################################################################################################

one_c = st.container(border=True)
with one_c:
    draw_line_plot(
        d=user_data[["date", "score"]],
        key_value="line1"
    )

two_c = st.container(border=True)
with two_c:
    two_1, two_2, two_3, two_4 = st.columns(4, vertical_alignment="center")
    with two_1:
        two_c_1 = st.container(border=False)
        with two_c_1:
            plot_gauge(
                indicator_number=0 if pd.isna(user_data[user_data['dificulty'] == "mixed"]['score'].max()) else int(user_data[user_data['dificulty'] == "mixed"]['score'].max()),
                indicator_title="Mixed",
                key_value="gauge1"
            )

    with two_2:
        two_c_2 = st.container(border=False)
        with two_c_2:
            plot_gauge(
                indicator_number=0 if pd.isna(user_data[user_data['dificulty'] == "easy"]['score'].max()) else int(user_data[user_data['dificulty'] == "easy"]['score'].max()),
                indicator_title="Easy",
                key_value="gauge2"
            )

    with two_3:
        two_c_3 = st.container(border=False)
        with two_c_3:
            plot_gauge(
                indicator_number=0 if pd.isna(user_data[user_data['dificulty'] == "medium"]['score'].max()) else int(user_data[user_data['dificulty'] == "medium"]['score'].max()),
                indicator_title="Medium",
                key_value="gauge3"
            )

    with two_4:
        two_c_4 = st.container(border=False)
        with two_c_4:
            plot_gauge(
                indicator_number=0 if pd.isna(user_data[user_data['dificulty'] == "hard"]['score'].max()) else int(user_data[user_data['dificulty'] == "hard"]['score'].max()),
                indicator_title="Hard",
                key_value="gauge4"
            )

three, four = st.columns([5, 5], vertical_alignment="center")

with three:
    three_c = st.container(border=True)
    with three_c:
        a = pd.pivot_table(data=user_data, index="dificulty", values="score", aggfunc="count")['score']
        b = pd.pivot_table(data=user_data, index="dificulty", values="score", aggfunc="mean")['score']

        c = pd.DataFrame({"Count" : a, "Mean" : list(map(lambda x : round(x, 2), list(b)))}).sort_values("Count", ascending=False)
        draw_pie_plot(
            d=c,
            key_value="pie1"
        )

with four:
    four_c = st.container(border=True)
    with four_c:
        a = user_data.groupby("topic")["score"].agg("mean")
        b = user_data.groupby("topic")["score"].agg("count")

        c = pd.DataFrame({"Topic" : a.index, "MeanScore" : list(a), "Count" : list(b)})
        
        draw_bar_chart(c.sort_values("MeanScore", ascending=False).iloc[:3], "bar1")