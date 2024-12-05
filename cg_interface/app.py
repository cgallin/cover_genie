import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from io import StringIO
import requests
from open_ai.pdf_preproc import pdf_to_text

# User input page
st.markdown(''' # Cover Genie 🧞‍♀️''')

st.markdown(''' Please enter the following information to generate relevant job postings:''')

job_title_1 = st.text_input('Enter a first desired job title: ', key='job_title_1')
job_title_2 = st.text_input('Enter a second desired job title: ', key='job_title_2')
job_title_3 = st.text_input('Enter a third desired job title: ', key='job_title_3')

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
     ['Montreal', 'Toronto'],
     key='location')

with st.form("my_form"):
    upload = st.file_uploader('Upload your CV in PDF format: ', type=['pdf'], accept_multiple_files=False),
    submitted = st.form_submit_button("Upload")

if submitted:
    user_cv = pdf_to_text(upload[0])

query_params = {
    'job_title_1':job_title_1,
    'job_title_2':job_title_2,
    'job_title_3':job_title_3,
    'location':location,
    'industries':industries
}

if st.button("Recommend jobs"):
    # url = ''
    # prediction = requests.get(url, params=query_params).json()
    # save prediction to session state
    switch_page("1_job_postings")
