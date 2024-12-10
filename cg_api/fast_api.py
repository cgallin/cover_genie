import pandas as pd
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from open_ai.prompt import generate_cover_letters
from recommendation.rec_model import recommendation
from recommendation.pre_proc_jobs import preprocessor, filter_dataframe
from typing import List, Annotated
import json


app = FastAPI()
app.state.model = None  # Placeholder for model loading

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for dev purposes
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/generate")
def generate_end(user_cv: str, job_descriptions: str):
    """
    API endpoint to generate cover letters based on user CV and job descriptions using OpenAI API.
    Returns a dictionary with cover letters.
    """
    try:
        # Parse the incoming job descriptions (expects JSON list as string)
        job_descriptions_list = json.loads(job_descriptions)

        # Call the parallelized generate_cover_letters function
        cover_letters = generate_cover_letters(user_cv, job_descriptions_list)

        # Structure the cover letters into a dictionary
        sep_cover_letters = {
            f"cover_letter_{i+1}": cover_letter for i, cover_letter in enumerate(cover_letters)
        }

        return {'Cover letters': sep_cover_letters}
    except json.JSONDecodeError:
        return {"error": "Invalid format for job_descriptions. Expected JSON string of list."}
    except Exception as e:
        return {"error": str(e)}

@app.get("/recommend")
async def recommend(
    job_title: str,
    user_cv: str,
    location: Annotated[List[str]|None,Query()]=None,
    industries: Annotated[List[str]|None,Query()]=None):
    """
    API endpoint to generate job recommendations based on user input.
    """


    job_postings = pd.read_csv('raw_data/jobs_data.csv')
 
    filtered_jobs = filter_dataframe(job_postings, location, industries)

    user_cv = preprocessor(user_cv)
    recommended_jobs = recommendation(user_cv_input=user_cv, job_title=job_title, filtered_jobs=filtered_jobs, k=5)

    return {"Job recommendations": recommended_jobs.to_dict(orient='records')}


@app.get("/")
def read_root():
    """
    Root endpoint for health check.
    """
    return {"Hello": "World"}
