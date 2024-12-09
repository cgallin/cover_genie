from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
import os

API_KEY = os.environ.get('API_KEY')
# Define the function
def generate_cover_letters(user_cv, job_descriptions):
    """
    Generate customized cover letters based on a resume PDF and a list of job descriptions.

    Args:
        user_cv: Input the text that is extracted from the users cv.
        job_descriptions (list): A list each containing 'job_description'.

    Returns:
        list: A list of cover letters.
    """

    # Step 2: Set up the OpenAI API and LLM
    llm = OpenAI(
        openai_api_key=API_KEY,
        temperature=0.7,
        max_tokens=800
    )

    # Step 3: Create the PromptTemplate
    cover_letter_prompt = PromptTemplate(
        input_variables=["user_cv", "job_description"],
        template="""
        You are a professional career counselor. Write a customized cover letter based on the following:

        - **Candidate's CV**:
        {user_cv}

        - **Job Description**:
        {job_description}

        This cover letter should:
        1. Start with an engaging opening.
        2. Highlight the candidate's relevant skills, experience, and accomplishments.
        3. Explain why the candidate is a good fit for the position.

        Ensure that it is professional and concise, using approximately 3-4 paragraphs.
        """
    )

    # Step 4: Set up the chain
    cover_letter_chain = LLMChain(
        llm=llm,
        prompt=cover_letter_prompt
    )

    # Step 5: Generate cover letters for each job description
    cover_letters = []
    for job_description in job_descriptions:
        cover_letter = cover_letter_chain.run(user_cv=user_cv, job_description=job_description)
        cover_letters.append(cover_letter)

    return cover_letters
