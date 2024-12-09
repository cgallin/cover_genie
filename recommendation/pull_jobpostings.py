import pickle
import pandas as pd

# Import the API data, enter the path as string
def pull_api_data(path):
    with open(path, "rb") as file:
        df_api = pickle.load(file)
    return df_api

import pandas as pd

def save_dataframe_to_csv(dataframe, file_path):
    """
    Save a pandas DataFrame to a CSV file.

    Args:
        dataframe (pd.DataFrame): The DataFrame to save.
        file_path (str): The full file path where the CSV will be saved.
    """
    dataframe.to_csv(file_path, index=False)
    print(f"DataFrame successfully saved to {file_path}")
