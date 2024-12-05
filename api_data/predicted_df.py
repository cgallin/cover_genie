import pickle
import pandas as pd
import bert.bert_model as bert_model

file = open("data_vancouver_jobs.pkl", "rb")
van_df=pickle.load(file)

def predict_industry_df(df):
    df["description_cleaned"]=df["description"].apply(bert_model.clean_text)
    df["industry"]=df["description_cleaned"].apply(bert_model.predict_industry)
    return df

predict_industry_df(van_df)
