import os
os.environ['KERAS_BACKEND'] = 'tensorflow'

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf
import tensorflow_text as text
import keras_hub
import keras_core as keras
import bert.pre_proc_linkedin as pre_proc_linkedin
import bert.params as pm
import datetime
import pickle





def train_model():


    # Load cleaned data
    with open('/Users/camerongallinger/code/cgallin/cover_genie/bert/clean_data/data.pkl', 'rb') as file:
        data = pickle.load(file)

    data = data.sample(frac=pm.SAMPLE_FRAC, random_state=pm.RANDOM_STATE)

    X = data["description_cleaned"]
    y = data["label"]


    X_train, X_test, y_train, y_test, X_val, y_val = pre_proc_linkedin.split_data(X, y)
    print("Data loaded and preprocessed")
    #define model parameters




    model = keras_hub.models.DistilBertClassifier.from_preset(
                    pm.PRE_TRAINED_MODEL_NAME,
                    preprocessor = keras_hub.models.DistilBertPreprocessor.from_preset(pm.PRE_TRAINED_MODEL_NAME,
                                                                    sequence_length=pm.SEQUENCE_LENGTH,
                                                                    name=pm.PREPROCESSOR_NAME),
                                                                    num_classes=pm.NUM_CLASSES,
                                                                    activation="softmax",
                                                                    dropout_rate=pm.DROPOUT_RATE)
    model.backbone.trainable = pm.TRAINABLE
    #Compile the model
    model.compile(
        loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        optimizer=tf.keras.optimizers.Adam(learning_rate=pm.LEARNING_RATE),
        metrics= ["accuracy"] )
    #Fit the model
    history = model.fit(x=X_train,
                         y=y_train,
                         batch_size=pm.BATCH_SIZE,
                         epochs=pm.EPOCHS,
                         validation_data=(X_val, y_val),
                         class_weight=pm.CLASS_WEIGHTS,
                        )
    # Save the model
    model.save(f"/Users/camerongallinger/code/cgallin/cover_genie/bert/models/model_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.keras")
    print("Model trained and saved")
    with open(f"/Users/camerongallinger/code/cgallin/cover_genie/bert/models/history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.keras", 'wb') as file_pi:
        pickle.dump(history.history, file_pi)
    return {"model": model, "history": history}

def predict_model(model, X_test):
    # Predict the model
    y_prob = model.predict(X_test)
    y_pred = y_prob.argmax(axis=1)
    return y_pred, y_prob


if __name__ == "__main__":
    train_model()
