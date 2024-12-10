import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import requests
import pyperclip
import json  # Import JSON module for encoding job_descriptions

# Ensure session state variables exist
if 'pred' not in st.session_state:
    st.session_state.pred = None

st.markdown(''' # Recommended Job Postings 🧞‍♀️''')

# Check if predictions are available
api_output = st.session_state.get('prediction', None)

if not api_output or 'Job recommendations' not in api_output:
    st.error("No job recommendations found. Please go back and try again.")
else:
    job_recommendations = api_output['Job recommendations']
    job_descriptions = []

    with st.form(key='recommend'):

        # Display job recommendations
        for item in job_recommendations:
            with st.expander(f"{item['title']} - {item['company']}"):
                st.write(f"**Description:** {item['description']}")
                st.write(f"**Job Provider:** {item['jobProviders']}")
                job_descriptions.append(item['description'])

        # Submit button to generate cover letters
        submitted = st.form_submit_button("Generate cover letters")

        if submitted:
            if st.session_state.pred:
                st.warning("Cover letters already generated.")
            else:
                # Convert job_descriptions to a JSON string
                try:
                    params = {
                        'user_cv': st.session_state.user_cv,
                        'job_descriptions': json.dumps(job_descriptions),  # Convert list to JSON string
                    }

                    url = 'http://127.0.0.1:8000/generate'

                    with st.spinner("Generating cover letters..."):
                        response = requests.get(url, params=params)

                    if response.status_code == 200:
                        try:
                            st.session_state.pred = response.json()
                            st.success("Cover letters generated!")
                            switch_page("page_2_cover_letters")
                        except Exception as e:
                            st.error(f"Failed to parse cover letter response. Error: {e}")
                    else:
                        st.error(f"Failed to fetch cover letters: {response.status_code}")
                except Exception as e:
                    st.error(f"Failed to encode job descriptions: {e}")

    # Display generated cover letters
    if st.session_state.pred:
        st.write("### Cover Letters")
        for i, (key, cover_letter) in enumerate(st.session_state.pred['Cover letters'].items(), start=1):
            with st.expander(f"Cover Letter {i}"):
                st.write(cover_letter)
            if st.button(f"Copy Cover Letter {i} to Clipboard", key=f'copy_{i}'):
                pyperclip.copy(cover_letter)
                st.success(f"Cover Letter {i} copied to clipboard!")
