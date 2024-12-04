import pickle

with open("api_data/data_toronto_jobs.pkl", "rb") as file:
    df_toronto = pickle.load(file)

with open("api_data/data_montreal_jobs.pkl", "rb") as file:
    df_montreal = pickle.load(file)
