import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests
import pyperclip
import openai
import json


if 'pred' not in st.session_state:
    st.session_state.pred = None

st.markdown(''' # Recommended Job Postings 🧞‍♀️''')

api_output = st.session_state.prediction

job_recommendations = api_output['Job recommendations']

job_descriptions = []

with st.form(key='recommend'):

    for item in job_recommendations:
        with st.expander(f"{item['title']} - {item['company']}"):
            st.write(f"{item['description']}")
            st.write(f"{item['jobProviders']}")
            job_descriptions.append(item['description'])


    submitted = st.form_submit_button("Generate cover letters")


    if submitted:
        params = {
        'user_cv': st.session_state.user_cv,
        'job_descriptions': job_descriptions,
        }

        url = 'http://127.0.0.1:8000/generate'

        pred = requests.get(url, params=params)
        if pred.status_code == 200:
            st.session_state.pred = pred.json()
            st.write(pred)

        # switch_page("page_2_cover_letters" )
        # else:
        #     st.error(f"Failed to fetch cover letters: {response.status_code}")

    if st.session_state.pred:
        st.write("Cover letters generated!")
        for i, cover_letter in enumerate(st.session_state.pred['cover_letters']):
            with st.expander(f"Cover Letter {i+1}"):
                st.write(cover_letter)
            if st.button(f"Copy Cover Letter {i+1} to Clipboard"):
                pyperclip.copy(cover_letter)
                st.success(f"Cover Letter {i+1} copied to clipboard!")
