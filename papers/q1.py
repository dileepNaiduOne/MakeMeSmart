import streamlit as st
from streamlit_confetti import confetti
import time


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.image(r"./img/logo-light.svg", width=70)

questions = st.session_state["questions"]

emojis_correct = [
    {"emoji": "🫡", "score": 0.1},
    {"emoji": "🤘", "score": 0.1},
    {"emoji": "👍", "score": 0.1},
    {"emoji": "🙌", "score": 0.1},
    {"emoji": "😘", "score": 0.1},
    {"emoji": "😍", "score": 0.1},
    {"emoji": "🥰", "score": 0.1},
]


st.write("\n")
# print(questions)

i = 0

q = questions[i]
# print("==="*50)
# print(questions[i])
# print("==="*50)
ops = {
    "A" : q["options"][0],
    "B" : q["options"][1],
    "C" : q["options"][2],
    "D" : q["options"][3]
}
que = f"{i+1}. {q["question"]}"
st.write(f"<p style=\"font-weight: bold;\">{que}</p>", unsafe_allow_html=True)
st.write(f"A. {ops['A']}")
st.write(f"B. {ops['B']}")
st.write(f"C. {ops['C']}")
st.write(f"D. {ops['D']}")
st.write("\n")

def check_answer():
    if option_chossen != None:
        st.session_state["q1_check"] = True

if 'q1' in st.session_state and st.session_state.q1 == True and ('q1_check' in st.session_state):
    st.session_state.q1_clicked = True
else:
    st.session_state.q1_clicked = False

option_chossen = st.pills(label="q1", options=["A", "B", "C", "D"], label_visibility="collapsed", disabled=st.session_state.q1_clicked)
st.write("\n")
st.write("\n")


check_button = st.button(label="Check", type="primary", use_container_width=True, disabled=st.session_state.q1_clicked, key='q1', on_click=check_answer)

st.session_state["Score"] = 0

if check_button:
    if option_chossen == None:
        st.error(body=f"{st.session_state.person["name"]}! Choose a Option", icon=":material/sentiment_very_dissatisfied:")
    else:
        if q["correct answer"] == ops[option_chossen]:
            confetti(emojis_correct)
            st.session_state["Score"] += 1
            time.sleep(4)
            st.switch_page("papers/q2.py")
        else:
            st.error(f":red[WRONG] - ✅{q["correct answer"]}")
            time.sleep(4)
            st.switch_page("papers/q2.py")
        
