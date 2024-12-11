import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests
import pdfplumber
from io import BytesIO



# User input page
st.markdown('''# Cover Genie 🧞‍♀️''')
st.markdown('''Please enter the following information to generate relevant job postings:''')

# Form for user input
with st.form(key='upload_cv'):
    # Input fields
    job_title = st.text_input('Enter a desired job title: ')

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
        ])

    location = st.multiselect(
        'Enter the desired work location:',
        ['Montreal', 'Toronto', 'Vancouver', 'Calgary', 'Ottawa', 'Edmonton', 'Winnipeg']
    )

    # Upload CV as PDF
    uploaded_file = st.file_uploader("Upload your CV (PDF format):", type=["pdf"])


    user_cv = ""
    if uploaded_file is not None:
        try:
            with pdfplumber.open(BytesIO(uploaded_file.read())) as pdf:
                # Extract text from all pages of the PDF
                user_cv = "".join([page.extract_text() for page in pdf.pages])
            st.success("CV uploaded and processed successfully!")
        except Exception as e:
            st.error(f"Failed to process the PDF. Error: {e}")

    # Form submission
    submitted = st.form_submit_button("Recommend jobs")

    if submitted and user_cv:
        query_params = {
            'job_title': str(job_title),
            'location': list(location) if location else "",
            'industries': list(industries) if industries else "",
            'user_cv': str(user_cv),
        }

        # Ensure session state variables exist
        if 'job_title' not in st.session_state:
            st.session_state.job_title = job_title
        if 'industries' not in st.session_state:
            st.session_state.industries = industries
        if 'location' not in st.session_state:
            st.session_state.location = location
        if 'user_cv' not in st.session_state:
            st.session_state.user_cv = user_cv

        url = 'https://cover-genie-696845380208.us-east1.run.app/recommend'

        response = requests.get(url, params=query_params)
        if response.status_code == 200:
            prediction = response.json()
            if 'prediction' not in st.session_state:
                st.session_state.prediction = prediction
            switch_page("page_1_job_postings")
        else:
            st.error(f"Failed to fetch recommendations: {response.status_code}")
    elif submitted and not user_cv:
        st.error("Please upload a valid CV PDF to proceed.")
