from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from concurrent.futures import ThreadPoolExecutor
import os

API_KEY = os.getenv("API_KEY")

def generate_cover_letters(user_cv, job_descriptions):
    """
    Generate customized cover letters in parallel based on a CV and a list of job descriptions.

    Args:
        user_cv: Input text extracted from the user's CV.
        job_descriptions (list): A list of job descriptions.

    Returns:
        list: A list of cover letters.
    """

    # Set up the OpenAI LLM
    llm = OpenAI(
        openai_api_key=API_KEY,
        temperature=0.7,
        max_tokens=800
    )

    # Create the PromptTemplate
    cover_letter_prompt = PromptTemplate(
        input_variables=["user_cv", "job_description"],
        template="""\
        You are an experienced professional applying for a job.
        Write a customized cover letter from the perspective of the applicant whose CV has been inputted based on the following,
        refer to the education and experience in the c.v. to tailor it to the job description.
        Please leave the name and address blank to be filled in by the user later

        - **Candidate's CV**:
        {user_cv}

        - **Job Description**:
        {job_description}

        This cover letter should:
        1. Start with an engaging opening.
        2. Highlight the candidate's relevant skills, experience, and accomplishments.
        3. Explain why the candidate is a good fit for the position.
        4. Not lie about or embellish the candidate's qualifications.
        5. Write with the active  and in the first person.

        Ensure that it is professional and concise, using approximately 3-4 paragraphs.
        """
    )

    # Set up the chain
    cover_letter_chain = LLMChain(
        llm=llm,
        prompt=cover_letter_prompt
    )

    # Function to generate a single cover letter
    def generate_single_cover_letter(job_description):
        return cover_letter_chain.run(user_cv=user_cv, job_description=job_description)

    # Generate cover letters in parallel
    with ThreadPoolExecutor() as executor:
        cover_letters = list(executor.map(generate_single_cover_letter, job_descriptions))

    return cover_letters
