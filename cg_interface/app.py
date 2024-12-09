import streamlit as st
import requests
<<<<<<< HEAD
import json
# import pdfplumber
import io
# from open_ai.pdf_preproc import pdf_to_text


# def pdf_bytes_to_string(pdf_bytes: bytes) -> str:
#     """Convert PDF bytes to a string."""
#     with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
#         text = ""
#         for page in pdf.pages:
#             text += page.extract_text()
#     return text
=======
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
>>>>>>> 1c6c900f50e419ae9e68d2fb91aeb6a1238da7df


# User input page
st.markdown('''# Cover Genie 🧞‍♀️''')
st.markdown('''Please enter the following information to generate relevant job postings:''')

# Initialize variables
job_title = ""
industries = []
location = []
user_cv = None

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
            'Staffing and Recruiting',
            'Hospitality, Travel, and Food Service',
            'Education and Research',
            'Construction and Real Estate Development',
            'Legal and Consulting Services',
            'Transportation and Logistics',
        ]
    )
    location = st.multiselect(
        'Enter the desired work location:',
        ['Montreal', 'Toronto', 'Vancouver', 'Calgary', 'Ottawa', 'Edmonton', 'Winnipeg']
    )
    upload = st.file_uploader('Upload your CV in PDF format:', type=['pdf'], accept_multiple_files=False)
    submitted = st.form_submit_button("Recommend jobs")

    if submitted:
        if upload is not None:
<<<<<<< HEAD
            # with open(upload.name, mode='wb') as w:
            #     w.write(upload.getvalue())
            # byte_pdf = upload.read()
            # user_cv = pdf_bytes_to_string(byte_pdf)
            st.success("CV uploaded successfully!")
        else:
            st.error("Please upload a valid PDF file.")
=======
            byte_pdf = upload.read()
            # user_cv = pdf_to_text(byte_pdf)
            user_cv = pdf_bytes_to_string(byte_pdf)
>>>>>>> 1c6c900f50e419ae9e68d2fb91aeb6a1238da7df

# Ensure variables are not empty
if not job_title:
    st.warning("Please enter a job title.")
if not industries:
    st.warning("Please select at least one industry.")
if not location:
    st.warning("Please select at least one location.")

<<<<<<< HEAD
# Build query parameters
if user_cv:
    query_params = {
        'job_title': job_title,
        'location': location[0] if location else "",
        'industries': industries[0] if industries else "",
        'user_cv': user_cv,
    }

    # # Display query parameters for debugging
    # st.write("Query Parameters:", query_params)

    # Recommend jobs button
=======
params = json.dumps(query_params)

if 'user_cv' not in st.session_state:
    st.session_state.user_cv = user_cv
>>>>>>> 1c6c900f50e419ae9e68d2fb91aeb6a1238da7df

    url = 'http://127.0.0.1:8000/recommend'
<<<<<<< HEAD
    try:
        response = requests.post(url, params=json.dumps(query_params))
        if response.status_code == 200:
            prediction = response.json()
            st.write("Job Recommendations:", prediction)
        else:
            st.error(f"Failed to fetch recommendations: {response.status_code}")
    except Exception as e:
        st.error(f"Error fetching recommendations: {e}")
else:
    st.info("Please upload your CV and fill in the required fields before recommending jobs.")


# import streamlit as st
# from streamlit_extras.switch_page_button import switch_page
# from io import StringIO
# import requests
# from open_ai.pdf_preproc import pdf_to_text
# import json
# import pdfplumber
# import io

# def pdf_bytes_to_string(pdf_bytes: bytes) -> str:
#     with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
#         text = ""
#         for page in pdf.pages:
#             text += page.extract_text()
#     return text


# # User input page
# st.markdown(''' # Cover Genie 🧞‍♀️''')

# st.markdown(''' Please enter the following information to generate relevant job postings:''')

# with st.form(key='upload_cv'):
#     job_title = st.text_input('Enter a desired job title: ')

#     industries = st.multiselect('Select the relevant industries for your job search: ',
#                 ['Healthcare and Biotechnology',
#                 'Technology',
#                 'Manufacturing',
#                 'Consumer Goods and Retail',
#                 'Finance, Banking, Insurance and Accounting',
#                 'Staffing and Recruiting',
#                 'Hospitality, Travel, and Food Service',
#                 'Education and Research',
#                 'Construction and Real Estate Development',
#                 'Legal and Consulting Services',
#                 'Transportation and Logistics'],
#                 key='industries')

#     location = st.multiselect(
#         'Enter the desired work location: ',
#         ['Montreal', 'Toronto', 'Vancouver',
#         'Calgary', 'Ottawa', 'Edmonton', 'Winnipeg'],
#         key='location')

#     if 'job_title' not in st.session_state:
#         st.session_state.job_title = job_title
#     if 'industries' not in st.session_state:
#         st.session_state.industries = industries
#     if 'location' not in st.session_state:
#         st.session_state.location = location


#     user_cv = None
#     upload = st.file_uploader('Upload your CV in PDF format: ', type=['pdf'], accept_multiple_files=False)
#     submitted = st.form_submit_button("Upload")
#     if submitted:
#         if upload is not None:
#             byte_pdf = upload.read()
#             # user_cv = pdf_to_text(byte_pdf)
#             user_cv = pdf_bytes_to_string(byte_pdf)

#             if 'user_cv' not in st.session_state:
#                 st.session_state.user_cv = user_cv
#             st.success("CV uploaded successfully!")

# query_params = {
#     'job_title': st.session_state.job_title,
#     'location': st.session_state.location[0] if st.session_state.location else "",
#     'industries': st.session_state.industries[0] if st.session_state.industries else "",
#     'user_cv': st.session_state.user_cv,
# }

# query_params = json.dumps(query_params)
# if 'query_params' not in st.session_state:
#     st.session_state.query_params = query_params


# # if st.button("Recommend jobs"):
# url = 'http://127.0.0.1:8000/recommend'
# prediction = requests.get(url, params=st.session_state.query_params).json()
# st.write(prediction)
#     # if 'prediction' not in st.session_state:
#     #     st.session_state.prediction = prediction
#     # switch_page("page_1_job_postings")
=======
    prediction = requests.get(url, params=params).json()
    st.write(prediction)
    # if 'prediction' not in st.session_state:
    #     st.session_state.prediction = prediction
    # switch_page("page_1_job_postings")
>>>>>>> 1c6c900f50e419ae9e68d2fb91aeb6a1238da7df
