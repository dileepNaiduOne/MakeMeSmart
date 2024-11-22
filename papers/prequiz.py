from PythonScipts import questions_generater
import streamlit as st
import time
import random


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

with st.status(f"Getting 10 Questions for {st.session_state["user_name"]}", expanded=True):
    st.write("Searching Internet...")
    questions = questions_generater.ask_questions(st.session_state["input_topic"], st.session_state["input_difficulty"])
    st.session_state["questions"] = eval(questions[9:-4])
    st.write(f"Sorting data about '{st.session_state["input_topic"]}'...")
    time.sleep(2)
    st.write(f"Gathering 10 '{st.session_state["input_difficulty"]}' questions about '{st.session_state["input_topic"]}'")
    time.sleep(2)
    st.write("Done! Get Ready!!!")
    time.sleep(1)

for i in st.session_state["questions"]:
    random.shuffle(i["options"])

# st.session_state["questions"] = [
#   {
#     "question number": 1,
#     "question": "What is the name of Einstein's theory of gravity?",
#     "options": [
#       "Theory of General Relativity",
#       "Theory of Special Relativity",
#       "Theory of Quantum Gravity",
#       "Theory of Electromagnetism"
#     ],
#     "correct answer": "Theory of General Relativity",
#     "difficulty level": "Hard"
#   },
#   {
#     "question number": 2,
#     "question": "What is the famous equation associated with Einstein?",
#     "options": [
#       "E=mc^2",
#       "F=ma",
#       "PV=nRT",
#       "hc/λ=Φ"
#     ],
#     "correct answer": "E=mc^2",
#     "difficulty level": "Hard"
#   },
#   {
#     "question number": 3,
#     "question": "What was Einstein's nationality?",
#     "options": [
#       "German",
#       "Swiss",
#       "Austrian",
#       "American"
#     ],
#     "correct answer": "Swiss",
#     "difficulty level": "Hard"
#   },
#   {
#     "question number": 4,
#     "question": "What was Einstein's profession?",
#     "options": [
#       "Physicist",
#       "Mathematician",
#       "Engineer",
#       "Philosopher"
#     ],
#     "correct answer": "Physicist",
#     "difficulty level": "Hard"
#   },
#   {
#     "question number": 5,
#     "question": "What is the name of the thought experiment that led Einstein to develop the theory of special relativity?",
#     "options": [
#       "Michelson-Morley experiment",
#       "Double-slit experiment",
#       "Stern-Gerlach experiment",
#       "Millikan oil drop experiment"
#     ],
#     "correct answer": "Michelson-Morley experiment",
#     "difficulty level": "Hard"
#   },
#   {
#     "question number": 6,
#     "question": "What is the name of the phenomenon that Einstein predicted where light bends around massive objects?",
#     "options": [
#       "Gravitational lensing",
#       "Redshift",
#       "Doppler effect",
#       "Aberration of light"
#     ],
#     "correct answer": "Gravitational lensing",
#     "difficulty level": "Hard"
#   },
#   {
#     "question number": 7,
#     "question": "What is the name of the award that Einstein received in 1921?",
#     "options": [
#       "Nobel Prize in Physics",
#       "Nobel Prize in Chemistry",
#       "Nobel Prize in Medicine",
#       "Nobel Prize in Literature"
#     ],
#     "correct answer": "Nobel Prize in Physics",
#     "difficulty level": "Hard"
#   },
#   {
#     "question number": 8,
#     "question": "What is the name of the university where Einstein developed the theory of general relativity?",
#     "options": [
#       "University of Zurich",
#       "ETH Zurich",
#       "University of Berlin",
#       "University of Vienna"
#     ],
#     "correct answer": "ETH Zurich",
#     "difficulty level": "Hard"
#   },
#   {
#     "question number": 9,
#     "question": "What was Einstein's political affiliation?",
#     "options": [
#       "Socialist",
#       "Communist",
#       "Liberal",
#       "Conservative"
#     ],
#     "correct answer": "Socialist",
#     "difficulty level": "Hard"
#   },
#   {
#     "question number": 10,
#     "question": "What is the name of the institute that Einstein founded in Princeton, New Jersey?",
#     "options": [
#       "Institute for Advanced Study",
#       "Princeton University",
#       "Massachusetts Institute of Technology",
#       "California Institute of Technology"
#     ],
#     "correct answer": "Institute for Advanced Study",
#     "difficulty level": "Hard"
#   }
# ]

st.switch_page("papers/q1.py")