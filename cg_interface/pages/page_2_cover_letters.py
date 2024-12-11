import streamlit as st
import pyperclip

# Check if cover letters are available
if 'pred' not in st.session_state or not st.session_state.pred:
    st.error("No cover letters found! Please go back and generate cover letters first.")
else:
    cover_letters = st.session_state.pred['Cover letters']

    cover_letters = st.session_state.pred['Cover letters']  #['Cover letters']
    api_output = st.session_state.get('prediction', None)
    job_recommendations = api_output['Job recommendations']


    st.markdown('''# Your Generated Cover Letters 🧞‍♀️''')

    # Display each cover letter dynamically in expanders
    for i, (key, cover_letter) in enumerate(cover_letters.items()):
        with st.expander(f"{job_recommendations[i]['title']} - {job_recommendations[i]['company']}"):
            st.write(cover_letter)
            # Copy button for each cover letter
            if st.button(f"Copy Cover Letter", key=f'copy_{i}'):
                pyperclip.copy(cover_letter)
                st.success(f"Cover Letter copied successfully!")
            st.link_button("Job Posting", job_recommendations[i]['jobProviders'])
