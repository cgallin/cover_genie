import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests

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

params = {
    job_des_1: job_des_1,
    job_des_2: job_des_2,
    job_des_3: job_des_3,
    job_des_4: job_des_4,
    job_des_5: job_des_5
}

if st.button("Generate cover letters"):
        # url = ''
        # response = requests.get(url, params=params).json()
        # save prediction to session state
        switch_page("2_cover_letters" )
