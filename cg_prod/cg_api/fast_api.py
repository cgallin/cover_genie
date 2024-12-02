import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# @app.get("/predict")
# Insert function to make predictions here.

# @app.get("/")
# Insert function to return a welcome message here.
