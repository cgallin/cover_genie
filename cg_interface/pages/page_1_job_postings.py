import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests
import pyperclip

st.markdown(''' # Recommended Job Postings 🧞‍♀️''')

api_output = st.session_state.prediction

job_recommendations = api_output['Job recommendations']

job_descriptions = []


for item in job_recommendations:
    with st.expander(f"{item['title']} - {item['company']}"):
        st.write(f"{item['description']}")
        st.write(f"{item['jobProviders']}")
        job_descriptions.append(item['description'])

params = {
    'user_cv': st.session_state.user_cv,
    'job_descriptions': job_descriptions,
}

if st.button("Generate cover letters"):
        url = 'http://127.0.0.1:8000/generate'
        response = requests.get(url, params=params).json()
        if 'response' not in st.session_state:
            st.session_state.response = response
        switch_page("page_2_cover_letters" )
