import os
os.environ['KERAS_BACKEND'] = 'tensorflow'

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf
import tensorflow_text as text
import keras_hub
import keras_core as keras
import pre_proc_linkedin as pp
import params as pm
import datetime





def train_model():
    X, y = pp.load_data()
    X = X.apply(lambda x: pp.clean_text(x))
    y_encoded = pp.features_encoder(y)

    X_train, X_test, y_train, y_test, X_val, y_val = pp.split_data(X, y_encoded)
    print("Data loaded and preprocessed")
    #define model parameters
    model = keras_hub.models.DistilBertClassifier.from_preset(
                    pm.PRE_TRAINED_MODEL_NAME,
                    preprocessor = keras_hub.models.DistilBertPreprocessor.from_preset(pm.PRE_TRAINED_MODEL_NAME,
                                                                    sequence_length=pm.SEQUENCE_LENGTH,
                                                                    name=pm.PREPROCESSOR_NAME),
                    num_classes=pm.NUM_CLASSES)
    #Compile the model
    model.compile(
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        optimizer=tf.keras.optimizers.Adam(learning_rate=pm.LEARNING_RATE),
        metrics= ["accuracy"])
    #Fit the model
    history = model.fit(x=X_train,
                         y=y_train,
                         batch_size=pm.BATCH_SIZE,
                         epochs=pm.EPOCHS,
                         validation_data=(X_val, y_val)
                        )
    # Save the model
    model.save(f"models/model_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")
    print("Model trained and saved")
    return {"model": model, "history": history}

def predict_model(model, X_test):
    # Predict the model
    y_prob = model.predict(X_test)
    y_pred = y_prob.argmax(axis=1)
    return y_pred, y_prob


train_model()
