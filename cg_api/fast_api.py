import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from open_ai.prompt import generate_cover_letters
from recommendation.rec_model import recommendation
from recommendation.pre_proc_jobs import preprocess_text, filter_location_and_industries
from typing import List

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
def generate_end(user_cv: str, job_descriptions: list):
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

@app.get("/recommend")
def recommend(job_title: str, location:str, industries: str, user_cv: str):
    ''' API end which generates job recommendations based on user input.'''

    job_postings = pd.read_csv('/Users/juliagreenwood/code/cgallin/cover_genie/notebooks/processed_w_industries.csv') # change to actual complete csv when ready

    user_cv = preprocess_text(user_cv)
    recommended_jobs = recommendation(user_cv=user_cv,job_title=job_title, filtered_jobs=job_postings, k=5)


    return {"Job recommendations": recommended_jobs}


@app.get("/")
def read_root():
    return {"Hello": "World"}
