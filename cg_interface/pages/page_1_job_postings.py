import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests
from open_ai.pdf_preproc import pdf_to_text

for prediction in st.session_state.prediction:
    st.write(prediction)

recommended_jobs = st.session_state.prediction
st.write(recommended_jobs)

st.markdown(''' # Recommended Job Postings 🧞‍♀️''')

with st.expander("# Job title - Company"):
    job_des_1 = st.write(''' Job description ... ''')
    st.write(''' url ''')

with st.expander("# Job title - Company"):
    job_des_2 = st.write(''' Job description ... ''')
    st.write(''' url ''')

with st.expander("# Job title - Company"):
    job_des_3 = st.write(''' Job description ... ''')
    st.write(''' url ''')

with st.expander("# Job title - Company"):
    job_des_4 = st.write(''' Job description ... ''')
    st.write(''' url ''')

with st.expander("# Job title - Company"):
    job_des_5 = st.write(''' Job description ... ''')
    st.write(''' url ''')

job_descriptions = [job_des_1, job_des_2, job_des_3, job_des_4, job_des_5]

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
