import streamlit as st
from streamlit_confetti import confetti
import time

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

try:

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

    i = 3

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
            
    if ("q4_clicked" not in st.session_state):
        st.session_state.q4_clicked = False

    def make_buttons_useless():
        if (option_chossen == None) or (option_chossen == []):
            st.session_state.q4_clicked = False
        else:
            st.session_state.q4_clicked = True

    option_chossen = st.pills(label="q4", options=["A", "B", "C", "D"], label_visibility="collapsed", disabled=st.session_state.q4_clicked)
    st.write("\n")
    st.write("\n")

    check_button = st.button(label="CHECK", type="primary", use_container_width=True, disabled=st.session_state.q4_clicked, key='q4', on_click=make_buttons_useless)
    if check_button:
        if (option_chossen != None) or (option_chossen != []):
            st.session_state["q4_check"] = True

    if check_button:
        if (option_chossen == None) or (option_chossen == []):
            st.error(body=f"{st.session_state.person["name"]}! :red[Choose a Option]", icon=":material/sentiment_very_dissatisfied:")
        else:
            if q["correct answer"] == ops[option_chossen]:
                confetti(emojis_correct)
                if st.session_state.quesion_bank[4] == None:
                    st.session_state.quesion_bank[4] = 1
                if st.session_state["check_list"][3]["check"] == None:
                    st.session_state["check_list"][3]["check"] = "correct"
                time.sleep(4)
                st.switch_page("papers/q5.py")
            else:
                if st.session_state.quesion_bank[4] == None:
                    st.session_state.quesion_bank[4] = 0
                if st.session_state["check_list"][3]["check"] == None:
                    st.session_state["check_list"][3]["check"] = "wrong"
                st.error(f":red[WRONG] - ✅{q["correct answer"]}")
                time.sleep(4)
                st.switch_page("papers/q5.py")
            
except KeyError:
    st.switch_page("papers/reload.py")

except AttributeError:
    st.switch_page("papers/reload.py")