import pickle


# Import the API data, enter the path as string
def pull_api_data(path):
    with open(path, "rb") as file:
        df_api = pickle.load(file)
    return df_api
