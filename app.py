import streamlit as st

start_page = st.Page(
    page="papers/start.py", 
    title="Start Page"
)

home_page = st.Page(
    page="papers/home.py", 
    title="Home Page"
)

topic_page = st.Page(
    page="papers/topic.py", 
    title="Topic Page"
)

pre_quiz_page = st.Page(
    page="papers/prequiz.py", 
    title="Pre Quiz Page"
)

q1 = st.Page(
    page="papers/q1.py", 
    title="Q1"
)

q2 = st.Page(
    page="papers/q2.py", 
    title="Q2"
)

q3 = st.Page(
    page="papers/q3.py", 
    title="Q3"
)

q4 = st.Page(
    page="papers/q4.py", 
    title="Q4"
)

q5 = st.Page(
    page="papers/q5.py", 
    title="Q5"
)

q6 = st.Page(
    page="papers/q6.py", 
    title="Q6"
)

q7 = st.Page(
    page="papers/q7.py", 
    title="Q7"
)

q8 = st.Page(
    page="papers/q8.py", 
    title="Q8"
)

q9 = st.Page(
    page="papers/q9.py", 
    title="Q9"
)

q10 = st.Page(
    page="papers/q10.py", 
    title="Q10"
)

score_page = st.Page(
    page="papers/score.py", 
    title="Score"
)

charts_page = st.Page(
    page="papers/charts.py", 
    title="Tableau Charts"
)

mms_page = st.Page(
    page="papers/mms.py", 
    title="MMS Charts"
)

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

pg = st.navigation(pages=[start_page, home_page, topic_page, pre_quiz_page, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, score_page, charts_page, mms_page], position="hidden")

pg.run()
