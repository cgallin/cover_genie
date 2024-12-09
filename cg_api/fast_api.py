import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from open_ai.prompt import generate_cover_letters
from recommendation.rec_model import recommendation
from recommendation.pre_proc_jobs import preprocess_text, filter_location_and_industries

app = FastAPI()
app.state.model = None #function to load model.

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/generate")
def generate_end(user_cv, job_descriptions):
    ''' API end which generates cover letters based on user CV and job descriptions using OpenAI API.
    Returns a dictionary with 5 cover letters. '''

    cover_letters = generate_cover_letters(user_cv, job_descriptions)
    sep_cover_letters = {
        "cover_letter_1": cover_letters[0],
        "cover_letter_2": cover_letters[1],
        "cover_letter_3": cover_letters[2],
        "cover_letter_4": cover_letters[3],
        "cover_letter_5": cover_letters[4]
    }
    return sep_cover_letters

@app.post("/recommend")
def recommend(job_title, location, industries, user_cv):
    ''' API end which generates job recommendations based on user input.'''

<<<<<<< HEAD
    job_postings = pd.read_csv('/Users/juliagreenwood/code/cgallin/cover_genie/processed_w_industries.csv') # change to actual complete csv when ready
    filtered_jobs = filter_location_and_industries(job_postings, location, industries)

    user_cv = preprocess_text(user_cv)
    recommended_jobs = recommendation(user_cv=user_cv,job_title=job_title, filtered_jobs=filtered_jobs, k=5)
=======
    job_postings = pd.read_csv('/Users/juliagreenwood/code/cgallin/cover_genie/filtered_jobs.csv') # change to actual complete csv when ready
    filtered_jobs = filter_location_and_industries(job_postings, location, industries)

    recommended_jobs = recommendation(user_cv,job_title, filtered_jobs, k=5)
    # recommended_jobs = filtered_jobs[['title', 'company', 'description', 'jobProviders']].sample(5)
>>>>>>> 1c6c900f50e419ae9e68d2fb91aeb6a1238da7df

    return recommended_jobs.to_dict()


@app.get("/")
def read_root():
    return {"Hello": "World"}
