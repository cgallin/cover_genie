import streamlit as st
import requests
# from open_ai.pdf_preproc import pdf_to_text
import json
# import pdfplumber
import io

# def pdf_bytes_to_string(pdf_bytes: bytes) -> str:
#     with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
#         text = ""
#         for page in pdf.pages:
#             text += page.extract_text()
#     return text


# User input page
st.markdown('''# Cover Genie 🧞‍♀️''')
st.markdown('''Please enter the following information to generate relevant job postings:''')

# # Initialize variables
# job_title = ""
# industries = []
# location = []
# user_cv = None

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
        ]
    )

    location = st.multiselect(
        'Enter the desired work location:',
        ['Montreal', 'Toronto', 'Vancouver', 'Calgary', 'Ottawa', 'Edmonton', 'Winnipeg'],
    )
    # upload = st.file_uploader('Upload your CV in PDF format:', type=['pdf'], accept_multiple_files=False)

    user_cv = st.text_area("Paste your CV here:")
    # Ensure variables are not empty
    # if not job_title:
    #     st.warning("Please enter a job title.")
    # if not industries:
    #     st.warning("Please select at least one industry.")
    # if not location:
    #     st.warning("Please select at least one location.")


    submitted = st.form_submit_button("Recommend jobs")

    if submitted:
        query_params = {
        'job_title': job_title,
        'location': location if location else "",
        'industries': industries if industries else "",
        'user_cv': user_cv,
        }
        st.write("Query Parameters:", query_params)

        url = 'http://127.0.0.1:8000/recommend'

        response = requests.get(url, params=query_params)
        if response.status_code == 200:
            prediction = response.json()
            st.write("Job Recommendations:", prediction)
        else:
            st.error(f"Failed to fetch recommendations: {response.status_code}")

        # else:
        #     st.info("Please upload your CV and fill in the required fields before recommending jobs.")

        # if upload is not None:
        #     # with open(upload.name, mode='wb') as w:
        #     #     w.write(upload.getvalue())
        #     # byte_pdf = upload.read()
        #     # user_cv = pdf_bytes_to_string(byte_pdf)
        #     st.success("CV uploaded successfully!")
        # else:
        #     st.error("Please upload a valid PDF file.")
        #     byte_pdf = upload.read()
        #     # user_cv = pdf_to_text(byte_pdf)
        #     user_cv = pdf_bytes_to_string(byte_pdf)


        # Build query parameters


    # # Display query parameters for debugging
    # st.write("Query Parameters:", query_params)

    # Recommend jobs button
# params = json.dumps(query_params)

# if 'user_cv' not in st.session_state:
#     st.session_state.user_cv = user_cv
