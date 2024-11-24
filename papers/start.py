import streamlit as st
from PythonScipts.database_tasks import *

# st.set_page_config(page_title="Sign-Up Form", layout="centered")


with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------



st.image(r"./img/logo-dark.svg", width=700)

st.write("\n")
st.write("\n")

col1, _, col2 = st.columns([2, 0.1, 2])

@st.dialog("SIGN UP")
def sign_up():
    if "person" not in st.session_state:
        with st.form("signup_form"):
            secret_sentence = st.text_input("Secret Sentence :", placeholder="Type here. Remember this. Needed for Log In", type="password")
            st.divider()
            name = st.text_input("Name :", placeholder="Enter your name")
            age = st.text_input("Age :", placeholder="Enter your age")
            email = st.text_input("Email Address :", placeholder="Enter your email address")
            gender = st.selectbox(label="Gender", options=["Female", "Male", "Others"], index=None)

            submitted = st.form_submit_button("SIGN UP", type="primary")

            if submitted:
                if not secret_sentence or not name or not age or not email or not gender:
                    st.error("All fields are required.")
                else:
                    st.success(f"Welcome, {name}! Your account has been created.")
                    st.session_state.person = {
                            "secret_sentence" : secret_sentence,
                            "name" : name,
                            "age" : age,
                            "email" : email,
                            "gender" : gender
                    }

                    secret_sentence = secret_sentence.lower().replace(" ", "")
                    name = name.lower()
                    age = int(age)
                    gender = gender.lower()

                    add_people_data(secret_sentence, name, age, email, gender)

                    st.rerun()
    else:
        st.write(f"{st.session_state.person["name"]}, Don't try to cheat me😉.")
        st.write("You have already Signed Up. Do :red[Log In]")



@st.dialog("LOG IN")
def log_in():
    with st.form("login_form"):
        secret_sentence = st.text_input("Secret Sentence :", placeholder="Type here. Remember the Sign Up Sentence", type="password")

        submitted = st.form_submit_button("LOG IN", type="primary")

        if submitted:
            if not secret_sentence:
                st.error("All fields are required.")
            else:
                secret_sentence = secret_sentence.lower().replace(" ", "")
                if ckeck_if_ss_in_people(secret_sentence) == 1:
                    secret_sentence, name, age, email, gender = get_data_from_people_using_ss(secret_sentence)

                    st.session_state.person = {
                            "secret_sentence" : secret_sentence,
                            "name" : name.upper(),
                            "age" : age,
                            "email" : email,
                            "gender" : gender
                    }

                    st.switch_page("papers/home.py")


with col1:
    st.button("SIGN UP", use_container_width=True, type="primary", on_click=sign_up)

with col2:
    st.button("LOG IN", use_container_width=True, type="primary", on_click=log_in)