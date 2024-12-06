import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from io import StringIO
import requests
from open_ai.pdf_preproc import pdf_to_text
import json
import pdfplumber
import io

def pdf_bytes_to_string(pdf_bytes: bytes) -> str:
    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text


# User input page
st.markdown(''' # Cover Genie 🧞‍♀️''')

st.markdown(''' Please enter the following information to generate relevant job postings:''')

job_title = st.text_input('Enter a desired job title: ')

industries = st.multiselect('Select the relevant industries for your job search: ',
            ['Healthcare and Biotechnology',
            'Technology',
            'Manufacturing',
            'Consumer Goods and Retail',
            'Finance, Banking, Insurance and Accounting',
            'Staffing and Recruiting',
            'Hospitality, Travel, and Food Service',
            'Education and Research',
            'Construction and Real Estate Development',
            'Legal and Consulting Services',
            'Transportation and Logistics'],
            key='industries')

location = st.multiselect(
     'Enter the desired work location: ',
     ['Montreal', 'Toronto', 'Vancouver',
      'Calgary', 'Ottawa', 'Edmonton', 'Winnipeg'],
     key='location')

user_cv = None

with st.form(key='upload_cv'):
    upload = st.file_uploader('Upload your CV in PDF format: ', type=['pdf'], accept_multiple_files=False)
    submitted = st.form_submit_button("Upload")
    if submitted:
        if upload is not None:
            byte_pdf = upload.read()
            # user_cv = pdf_to_text(byte_pdf)
            user_cv = pdf_bytes_to_string(byte_pdf)

query_params = {
    'job_title': job_title,
    'location': location,
    'industries': industries,
    'user_cv': user_cv
}

params = json.dumps(query_params)

if 'user_cv' not in st.session_state:
    st.session_state.user_cv = user_cv

if st.button("Recommend jobs"):
    url = 'http://127.0.0.1:8000/recommend'
    prediction = requests.get(url, params=params).json()
    st.write(prediction)
    # if 'prediction' not in st.session_state:
    #     st.session_state.prediction = prediction
    # switch_page("page_1_job_postings")
