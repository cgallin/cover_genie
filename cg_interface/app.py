import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests
import json
import io
import pyperclip
import pdfplumber

# User input page
st.markdown('''# Cover Genie 🧞‍♀️''')
st.markdown('''Please enter the following information to generate relevant job postings:''')

# Form for user input
with st.form(key='upload_cv'):
    # Input fields
    job_title = st.text_input('Enter a desired job title: ', value='Data Scientist')
    industries = st.multiselect(
        'Select the relevant industries for your job search:',
        [
            'Healthcare and Biotechnology',
            'Technology',
            'Manufacturing',
            'Consumer Goods and Retail',
            'Finance, Banking, Insurance and Accounting',
            'Sales, Marketing, and Recruitement',
            'Hospitality, Travel, and Food Service',
            'Education and Research',
            'Construction and Real Estate Development',
            'Legal and Consulting Services',
            'Transportation and Logistics',
        ],
        default=['Technology'],
    )

    location = st.multiselect(
        'Enter the desired work location:',
        ['Montreal', 'Toronto', 'Vancouver', 'Calgary', 'Ottawa', 'Edmonton', 'Winnipeg'],
        default= ['Montreal'],
    )

    user_cv = st.text_area("Paste your CV here:",
                           value= 'A naturally creative, critical, and analytical thinker, I am a resourceful, organized, and above all dedicated to my work.  Passionate about my starting career in the market research industry, I will greatly contribute to your team.')

    submitted = st.form_submit_button("Recommend jobs")

    if submitted:
        query_params = {
        'job_title': job_title,
        'location': location[0] if location else "",
        'industries': industries[0] if industries else "",
        'user_cv': user_cv,
        }
        st.write("Query Parameters:", query_params)

        # Ensure session state variables exist
        if 'job_title' not in st.session_state:
            st.session_state.job_title = job_title
        if 'industries' not in st.session_state:
            st.session_state.industries = industries
        if 'location' not in st.session_state:
            st.session_state.location = location
        if 'user_cv' not in st.session_state:
            st.session_state.user_cv = user_cv

        url = 'http://127.0.0.1:8000/recommend'

        response = requests.get(url, params=query_params)
        if response.status_code == 200:
            prediction = response.json()
            st.write("Job Recommendations:", prediction)
            if 'prediction' not in st.session_state:
                st.session_state.prediction = prediction
            switch_page("page_1_job_postings")
        else:
            st.error(f"Failed to fetch recommendations: {response.status_code}")
