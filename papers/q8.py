import streamlit as st
from streamlit_confetti import confetti
import time

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.image(".\img\logo-light.svg", width=70)

questions = st.session_state["questions"]

emojis_correct = [
    {"emoji": "🫡", "score": 0.1},
    {"emoji": "🤘", "score": 0.1},
    {"emoji": "👍", "score": 0.1},
    {"emoji": "🙌", "score": 0.1},
    {"emoji": "🤩", "score": 0.1},
    {"emoji": "😘", "score": 0.1},
    {"emoji": "😌", "score": 0.1},
    {"emoji": "🤑", "score": 0.1},
    {"emoji": "😍", "score": 0.1},
    {"emoji": "🥰", "score": 0.1},
]


st.write("\n")

i = 7

q = questions[i]
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
option_chossen = st.pills(label="", options=["A", "B", "C", "D"], label_visibility="collapsed")
st.write("\n")
st.write("\n")
check_button = st.button(label="Check", type="primary", use_container_width=True)

if check_button:
    if option_chossen == None:
        st.error(body=f"{st.session_state["user_name"]}! Choose a Option", icon=":material/sentiment_very_dissatisfied:")
    else:
        if q["correct answer"] == ops[option_chossen]:
            confetti(emojis_correct)
            st.session_state["Score"] += 1
            time.sleep(3)
            st.switch_page("papers/q9.py")
        else:
            st.error("Wrong")
            time.sleep(1)
            st.switch_page("papers/q9.py")
        
