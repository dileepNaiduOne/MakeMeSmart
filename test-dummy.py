import streamlit as st
from PythonScipts.database_tasks import *
from PythonScipts.makemesmart_generater import make_me_smart

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------

qs = [
    {
        "question": "Is logistic regression primarily used for classification or regression tasks?",
        "check": "correct"
    },
    {
        "question": "Does logistic regression predict a continuous value between 0 and 1?",
        "check": "wrong"
    },
    {
        "question": "What is the link function in logistic regression?",
        "check": "correct"
     },
    {
        "question": "Can logistic regression handle non-linear relationships between features and the target variable?",
        "check":"wrong"
    },
     {
        "question": "Is the sigmoid function used in the computation of logistic regression?",
         "check":"correct"
     },
     {
       "question": "In logistic regression, does a higher coefficient value for a feature always imply more importance for prediction?",
        "check": "wrong"
     },
    {
      "question": "Does logistic regression assume that there is a linear relationship between the dependent and independent variables?",
      "check": "wrong"
    },
     {
        "question": "Is the output of a logistic regression model a probability?",
        "check": "correct"
     },
    {
        "question": "Is gradient descent commonly used to find the optimal parameters of a logistic regression model?",
        "check": "correct"
    },
     {
        "question": "Can multicollinearity significantly impact the performance of a logistic regression model?",
        "check":"correct"
    }
]

st.write(make_me_smart("Logistic Regression", qs))
        


st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

return_button = st.button("RETURN TO HOME", type="primary")

if return_button:
    st.switch_page("papers/home.py")
