import streamlit as st
from io import StringIO
import requests
import pandas as pd
import numpy as np

# User input page

st.markdown(''' # Cover Genie 🧞‍♀️''')
st.markdown(''' # Automate your job search: Generate Cover letters with ease!''')

st.markdown(''' Please enter the following information to generate relevant job postings:''')

url = 'https://X.X.X/recommend'

if st.button('Recommend jobs'):
    pred = requests.get(url, params=query_params).json()
    # pred["fare"] = pred["fare"]
    # st.markdown(f'This ride will cost you: ${pred["fare"]}')

# Get input function
def input():
    job_title_1 = st.text_input('Enter a desired job title: '),
    job_title_2 = st.text_input('Enter a desired job title: '),
    job_title_3 = st.text_input('Enter a desired job title: '),

    location = st.text_input('Enter the desired work location: '),

    user_cv = st.file_uploader('Upload your CV in PDF format: ', type=['pdf'], accept_multiple_files=False),

    if user_cv is not None:
        # To read file as bytes:
        bytes_data = user_cv.getvalue() # not sure about this bit, how to make it work with the pdf text extractor
        st.write('filename:', user_cv.name)

    industries = get_select_industries()

    # Getting params to generate job recommendations,
    query_params = {
        'job_title_1': job_title_1,
        'job_title_2': job_title_2,
        'job_title_3': job_title_3,
        'location': location,
        'user_cv': bytes_data,
        'industries': industries,
    }
    return query_params

# Selecting Job industry

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


def get_select_industries():
    st.write('Select the relevant industries for your job search: ')

    selected_industries = []

    for industry in industries:
        st.checkbox(industry)
        if industry:
            selected_industries.append(industry)

    st.write('You selected:', selected_industries)
    return selected_industries

# Output from recommendation system: displaying job recommendations in a dataframe.

def get_dataframe_data():

    return pd.DataFrame(
# data frame with job recommendations: Job title, company, job description, apply button
        )

df = get_dataframe_data()

# Generate cover letter page
