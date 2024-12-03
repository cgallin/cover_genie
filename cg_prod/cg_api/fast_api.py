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

# def predict(
    #     pickup_datetime: str,  # 2014-07-06 19:18:00
    #     pickup_longitude: float,    # -73.950655
    #     pickup_latitude: float,     # 40.783282
    #     dropoff_longitude: float,   # -73.984365
    #     dropoff_latitude: float,    # 40.769802
    #     passenger_count: int
    # ):      # 1
    # """
    # Make a single course prediction.
    # Assumes `pickup_datetime` is provided as a string by the user in "%Y-%m-%d %H:%M:%S" format
    # Assumes `pickup_datetime` implicitly refers to the "US/Eastern" timezone (as any user in New York City would naturally write)
    # """
    # X_pred = pd.DataFrame({
    #     'pickup_datetime': [pd.Timestamp(pickup_datetime, tz="US/Eastern")],
    #     'pickup_longitude': [pickup_longitude],
    #     'pickup_latitude': [pickup_latitude],
    #     'dropoff_longitude': [dropoff_longitude],
    #     'dropoff_latitude': [dropoff_latitude],
    #     'passenger_count': [passenger_count]
    #     })

    # X_pred = preprocess_features(X_pred)
    # model = app.state.model
    # y_pred = model.predict(X_pred)

    # return {'fare': float(y_pred[0])}


# @app.get("/")
# Insert function to return a welcome message here.
