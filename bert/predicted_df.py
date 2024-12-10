import pickle
import pandas as pd
import bert.bert_model as bert_model
import bert.pre_proc_linkedin as pp
import bert.params as pm

import tensorflow as tf
import tensorflow_text as text
import keras_hub
import keras_core as keras



## Function to predict the industry of jobs scraped from the web

def predict_industry_df(data_path,model_path):
    #load\compile the model
    classifier = tf.keras.models.load_model(model_path)
    classifier.compile(
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        optimizer=tf.keras.optimizers.Adam(learning_rate=pm.LEARNING_RATE),
        metrics= ["accuracy"])
    #load the data
    with open(data_path, 'rb') as file:
        df = pickle.load(file)
    #clean and concatenate the text data
    df["description_cleaned"]=df["title"]+" "+ df["company"]+" " +df["description"]
    df["description_cleaned"]=df["description_cleaned"].apply(pp.clean_text)
    df["industries"]= classifier.predict(df["description_cleaned"]).argmax(axis=1)
    df["industries"]=df["industries"].map(pm.INDUSTRY_LABELS)

    with open(data_path.replace(".pkl","")+"_with_predictions.pkl", 'wb') as file:
        pickle.dump(df, file)

if __name__ == "__main__":
    data_path = input("Please enter the data path: ")
    model_path = input("Please enter the model path: ")
    predict_industry_df(data_path=data_path,model_path=model_path)
