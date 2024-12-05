import streamlit as st
import pyperclip

st.markdown(''' # Your Generated Cover Letters 🧞‍♀️''')


with st.expander("# Job title - Company"):
    cover_1 = st.write(''' Cover letter text ... ''')
    st.write(''' Here is the {url} to apply to this job.''')
    if st.button('Copy Cover Letter', key='copy_1'):
        pyperclip.copy(cover_1)
        st.success('Text copied successfully!')


with st.expander("# Job title - Company"):
    cover_2 = st.write(''' Cover letter ... ''')
    st.write(''' Here is the {url} to apply to this job.''')
    if st.button('Copy Cover Letter', key='copy_2'):
        pyperclip.copy(cover_1)
        st.success('Text copied successfully!')

with st.expander("# Job title - Company"):
    cover_3 = st.write(''' Cover letter... ''')
    st.write(''' Here is the {url} to apply to this job.''')
    if st.button('Copy Cover Letter', key='copy_3'):
        pyperclip.copy(cover_1)
        st.success('Text copied successfully!')

with st.expander("# Job title - Company"):
    cover_4 = st.write(''' Cover letter ... ''')
    st.write(''' Here is the {url} to apply to this job.''')
    if st.button('Copy Cover Letter', key='copy_4'):
        pyperclip.copy(cover_1)
        st.success('Text copied successfully!')

with st.expander("# Job title - Company"):
    cover_5 = st.write(''' Cover letter ... ''')
    st.write(''' Here is the {url} to apply to this job.''')
    if st.button('Copy Cover Letter', key='copy_5'):
        pyperclip.copy(cover_1)
        st.success('Text copied successfully!')
