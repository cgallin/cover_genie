import pickle

with open("api_data/data_toronto_jobs.pkl", "rb") as file:
    df = pickle.load(file)
