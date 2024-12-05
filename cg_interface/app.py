import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from io import StringIO
import requests
from open_ai.pdf_preproc import pdf_to_text



# User input page

st.markdown(''' # Cover Genie 🧞‍♀️''')

st.markdown(''' Please enter the following information to generate relevant job postings:''')

job_title_1 = st.text_input('Enter a first desired job title: ')
job_title_2 = st.text_input('Enter a second desired job title: ')
job_title_3 = st.text_input('Enter a third desired job title: ')

st.write('Select the relevant industries for your job search: ')

industries = ['Healthcare and Biotechnology',
            'Technology',
            'Manufacturing',
            'Consumer Goods and Retail',
            'Finance, Banking, Insurance and Accounting',
            'Staffing and Recruiting',
            'Financial Services',
            'Hospitality, Travel, and Food Service',
            'Education and Research',
            'Construction and Real Estate Development',
            'Legal and Consulting Services',
            'Transportation and Logistics',
            'Real Estate, Property Management, and Construction',
            'Government and Public Administration',
            'Entertainment and Media',
            'Advertising Services',
            'Wellness and Fitness Services',
            'Environmental and Renewable Energy',
            'Utilities']

selected_industries = []
for industry in industries:
    if st.checkbox(industry):
        selected_industries.append(industry)

location = st.multiselect(
     'Enter the desired work location: ',
     ['Montreal', 'Toronto'])

with st.form("my_form"):
    upload = st.file_uploader('Upload your CV in PDF format: ', type=['pdf'], accept_multiple_files=False),
    submitted = st.form_submit_button("Upload")

if submitted:
    user_cv = pdf_to_text(upload[0])

query_params = {
    'job_title_1': job_title_1,
    'job_title_2': job_title_2,
    'job_title_3': job_title_3,
    'location': location,
    'industries': selected_industries,
}

if query_params not in st.session_state:
    st.session_state.query_params = query_params

if st.button("Recommend jobs"):
    switch_page("job_postings")  # Match the file name of Page1.py (case-sensitive)
