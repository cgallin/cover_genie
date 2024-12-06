import pickle
import pandas as pd
import bert.bert_model as bert_model
import bert.pre_proc_linkedin as pp
import bert.params as pm

import tensorflow as tf
import tensorflow_text as text
import keras_hub
import keras_core as keras


with open('/Users/camerongallinger/code/cgallin/cover_genie/api_data/data_vancouver_jobs.pkl', 'rb') as file:
    df = pickle.load(file)

classifier = tf.keras.models.load_model("/Users/camerongallinger/code/cgallin/cover_genie/bert/models/model_20241206_161522.keras")
classifier.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer=tf.keras.optimizers.Adam(learning_rate=pm.LEARNING_RATE),
    metrics= ["accuracy"]
)

def predict_industry_df(df):
    df["description_cleaned"]=df["description"].apply(pp.clean_text)
    df["industries"]= classifier.predict(df["description_cleaned"]).argmax(axis=1)
    #df["industry_probs"]= classifier.predict(df["description_cleaned"])
    with open('/Users/camerongallinger/code/cgallin/cover_genie/api_data/data_vancouver_jobs_with_predictions.pkl', 'wb') as file:
        pickle.dump(df, file)



predict_industry_df(df)
