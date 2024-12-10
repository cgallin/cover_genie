import streamlit as st
import pyperclip

# Check if cover letters are available
if 'pred' not in st.session_state or not st.session_state.pred:
    st.error("No cover letters found! Please go back and generate cover letters first.")
else:
    cover_letters = st.session_state.pred['Cover letters']  #['Cover letters']

    api_output = st.session_state.get('prediction', None)
    job_recommendations = api_output['Job recommendations']


    st.markdown('''# Your Generated Cover Letters 🧞‍♀️''')

    for i,item in enumerate(job_recommendations):

        with st.expander(f"{item['title']} - {item['company']}"):
            st.write(cover_letters[f'cover_letter_{i+1}'])
        # Copy button for each cover letter
            if st.button(f"Copy Cover Letter", key=f'copy_{i+1}'):
                pyperclip.copy(cover_letters[f'cover_letter_{i+1}'])
                st.success(f"Cover Letter copied successfully!")
            st.link_button("Job Posting", item['jobProviders'])
