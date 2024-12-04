import os
os.environ['KERAS_BACKEND'] = 'tensorflow'

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf
import tensorflow_text as text
import keras_hub
import keras_core as keras
import pre_proc_linkedin as pp




def train_model():
    X, y = pp.load_data()
    X = X.apply(lambda x: pp.clean_text(x))
    y_encoded = pp.features_encoder(y)

    X_train, X_test, y_train, y_test, X_val, y_val = pp.split_data(X, y_encoded)
    #define model parameters
    model = keras_hub.models.DistilBertClassifier.from_preset(
                    PRE_TRAINED_MODEL_NAME,
                    preprocessor = keras_hub.models.DistilBertPreprocessor.from_preset(PRE_TRAINED_MODEL_NAME,
                                                                    sequence_length=SEQUENCE_LENGTH,
                                                                    name=PREPROCESSOR_NAME),
                    num_classes=NUM_CLASSES)
    #Compile the model
    model.compile(
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE),
        metrics= ["accuracy"])
    #Fit the model
    history = model.fit(x=X_train,
                         y=y_train,
                         batch_size=BATCH_SIZE,
                         epochs=EPOCHS,
                         validation_data=(X_val, y_val)
                        )
    return {"model": model, "history": history,"Score": model.evaluate(X_test, y_test)}

def save_model(model, path):
    model.save(path)
