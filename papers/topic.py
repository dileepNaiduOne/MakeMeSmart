import streamlit as st

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------



# if "user_name" not in st.session_state:
#     st.session_state["user_name"] = user_name

st.image(r"./img/logo-light.svg", width=100)
st.title(f":gray[Hi,] :red[{st.session_state.person["name"]}!]", anchor=False)
st.divider()

st.text("\n")
input_topic = st.text_input(label="Topic :", placeholder="Type in the topic")
st.text("\n")
input_difficulty = st.pills(label="Difficulty :", options=["Mixed", "Easy", "Medium", "Hard"])

st.divider()

st.session_state["input_topic"] = input_topic.strip()
st.session_state["input_difficulty"] = input_difficulty

quiz_button = st.button(label="Start Quiz", type="primary", use_container_width=True)

if quiz_button:
    if (len(input_topic) == 0) and (input_difficulty == None):
        st.error(body=f"{st.session_state.person["name"]}! You did not type Topic & Difficulty Level", icon=":material/sentiment_very_dissatisfied:")
    elif (len(input_topic) == 0):
        st.error(body=f"{st.session_state.person["name"]}! You did not type Topic", icon=":material/sentiment_sad:")
    elif (input_difficulty == None):
        st.error(body=f"{st.session_state.person["name"]}! You did not type Difficulty Level", icon=":material/sentiment_dissatisfied:")
    else:
        st.switch_page("papers/prequiz.py")

