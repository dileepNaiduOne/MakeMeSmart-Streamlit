import streamlit as st
from streamlit_confetti import confetti
import time
from PythonScipts.database_tasks import *

with open( "style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.image(r"./img/logo-light.svg", width=70)

st.title(f":gray[{st.session_state.person["name"]}, You Scored]", anchor=False)
st.title(f":red[{st.session_state["Score"]}]:gray[/10]", anchor=False)
st.title(f":gray[in '{st.session_state["input_topic"]}']", anchor=False)

if "score_data" not in st.session_state:
    add_score_data(st.session_state.person["secret_sentence"], st.session_state["input_topic"], st.session_state["input_difficulty"], st.session_state["Score"])
    st.session_state["score_data"] = True

return_button = st.button(label="BACK TO HOME", type="primary")

if return_button:
    st.switch_page("papers/home.py")

