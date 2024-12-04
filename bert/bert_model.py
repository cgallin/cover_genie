import os
os.environ['KERAS_BACKEND'] = 'tensorflow'

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf
import tensorflow_text as text
import keras_hub
import keras_core as keras




# Load a DistilBERT model.
preset= "distil_bert_base_en_uncased"

# Use a shorter sequence length.
preprocessor = keras_hub.models.DistilBertPreprocessor.from_preset(preset,
                                                                   sequence_length=SEQUENCE_LENGTH,
                                                                   name="preprocessor_4_tweets"
                                                                  )

# Pretrained classifier.
classifier = keras_hub.models.DistilBertClassifier.from_preset(preset,
                                                               preprocessor = preprocessor,
                                                               num_classes=12)

classifier.summary()
