import pymysql
import os
from dotenv import load_dotenv
import streamlit as st



@st.cache_data
def add_people_data(ss, name, age, email, gender):
    load_dotenv()

    db = pymysql.connect(
        host = os.getenv("MYSQL_ADDON_HOST"),
        user = os.getenv("MYSQL_ADDON_USER"),
        password = os.getenv("MYSQL_ADDON_PASSWORD"),
        database=os.getenv("MYSQL_ADDON_DB")
    )

    mycursor = db.cursor()

    mycursor.execute(f"insert into people (secret_sentence, name, age, email, gender) values ('{ss}', '{name}', {age}, '{email}', '{gender}')")
    db.commit()



@st.cache_data
def ckeck_if_ss_in_people(ss):
    load_dotenv()

    db = pymysql.connect(
        host = os.getenv("MYSQL_ADDON_HOST"),
        user = os.getenv("MYSQL_ADDON_USER"),
        password = os.getenv("MYSQL_ADDON_PASSWORD"),
        database=os.getenv("MYSQL_ADDON_DB")
    )

    mycursor = db.cursor()

    mycursor.execute(f"select * from people where secret_sentence like '{ss}'")

    return len([i for i in mycursor])



@st.cache_data
def get_data_from_people_using_ss(ss):
    load_dotenv()

    db = pymysql.connect(
        host = os.getenv("MYSQL_ADDON_HOST"),
        user = os.getenv("MYSQL_ADDON_USER"),
        password = os.getenv("MYSQL_ADDON_PASSWORD"),
        database=os.getenv("MYSQL_ADDON_DB")
    )

    mycursor = db.cursor()

    mycursor.execute(f"select * from people where secret_sentence like '{ss}'")

    return list(mycursor)[0]



@st.cache_data
def add_score_data(ss, topic, dificulty, score):
    load_dotenv()

    db = pymysql.connect(
        host = os.getenv("MYSQL_ADDON_HOST"),
        user = os.getenv("MYSQL_ADDON_USER"),
        password = os.getenv("MYSQL_ADDON_PASSWORD"),
        database=os.getenv("MYSQL_ADDON_DB")
    )

    mycursor = db.cursor()

    mycursor.execute(f"insert into scores (secret_sentence, date, topic, dificulty, score) values ('{ss}', now(), '{topic}', '{dificulty}', {score})")
    db.commit()



@st.cache_data
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