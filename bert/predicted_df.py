import pickle
import pandas as pd
import bert.bert_model as bert_model
import bert.pre_proc_linkedin as pp
import bert.params as pm

import tensorflow as tf
import tensorflow_text as text
import keras_hub
import keras_core as keras






def predict_industry_df(data_path,model_path):

    classifier = tf.keras.models.load_model(model_path)
    classifier.compile(
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        optimizer=tf.keras.optimizers.Adam(learning_rate=pm.LEARNING_RATE),
        metrics= ["accuracy"])

    with open(data_path, 'rb') as file:
        df = pickle.load(file)
    df["description"]=df["title"]+df["compay"]+df["description"]
    df["description_cleaned"]=df["description"].apply(pp.clean_text)
    df["industries"]= classifier.predict(df["description_cleaned"]).argmax(axis=1)
    #df["industry_probs"]= classifier.predict(df["description_cleaned"])
    with open(data_path.replace(".pkl","")+"_with_predictions.pkl", 'wb') as file:
        pickle.dump(df, file)

if __name__ == "__main__":
    data_path = input("Please enter the data path: ")
    model_path = input("Please enter the model path: ")
    predict_industry_df(data_path=data_path,model_path=model_path)
