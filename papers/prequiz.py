from PythonScipts import questions_generater
import streamlit as st
import time
import random


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

try:

    with st.status(f"Getting 10 Questions for {st.session_state.person["name"]}", expanded=True):
        st.write("Searching Internet...")
        questions = questions_generater.ask_questions(st.session_state["input_topic"], st.session_state["input_difficulty"])
        print(questions)
        st.session_state["questions"] = eval(questions[questions.find("["): questions.rfind("]")+1])

        st.session_state["check_list"] = []
        for i in st.session_state["questions"]:
            st.session_state["check_list"].append({
                'question' : i["question"],
                'check' : None
            })
            
        st.write(f"Sorting data about '{st.session_state["input_topic"]}'...")
        time.sleep(2)
        st.write(f"Gathering 10 '{st.session_state["input_difficulty"]}' questions about '{st.session_state["input_topic"]}'")
        time.sleep(2)
        st.write("Done! Get Ready!!!")
        time.sleep(1)

    for i in st.session_state["questions"]:
        random.shuffle(i["options"])

    st.session_state["Score"] = 0

    st.session_state.quesion_bank = {
        1 : None,
        2 : None,
        3 : None,
        4 : None,
        5 : None,
        6 : None,
        7 : None,
        8 : None,
        9 : None,
        10 : None
    }

    print(st.session_state["questions"])
    st.switch_page("papers/q1.py")

except KeyError:
    st.switch_page("papers/reload.py")

except AttributeError:
    st.switch_page("papers/reload.py")