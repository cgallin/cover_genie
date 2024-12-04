import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai
# import packages to preprocess data, load model, and make predictions


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

# @app.get("/generate_cover_letter")
# Insert function to generate cover letters.


# @app.get("/recommend")
# Insert function to generate job recommendations

# def recommend(query_params: dict):
    #     job_title_1: str,
    #     job_title_2: str,
    #     job_title_3: str,
    #     location: str,
    #     user_cv:
    #     industries: str,
    # ):
    # """
    # Make a single course prediction.
    # Assumes `pickup_datetime` is provided as a string by the user in "%Y-%m-%d %H:%M:%S" format
    # Assumes `pickup_datetime` implicitly refers to the "US/Eastern" timezone (as any user in New York City would naturally write)
    # """
    # X_pred = pd.DataFrame(query_params)

    # X_pred = preprocess_features(X_pred)
    # model = app.state.model
    # y_pred = model.predict(X_pred)

    # return {'fare': float(y_pred[0])}


@app.get("/")
def read_root():
    return {"Hello": "World"}
