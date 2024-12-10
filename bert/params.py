#Parameters for the BERT model

RANDOM_STATE = 42
SEQUENCE_LENGTH = 300
BATCH_SIZE = 32
TRAIN_SPLIT = 0.7
VAL_SPLIT = 0.3
EPOCHS = 2
LEARNING_RATE = 2e-6
PRE_TRAINED_MODEL_NAME = "distil_bert_base_en_uncased"
PREPROCESSOR_NAME = "distil_bert_base_en"
NUM_CLASSES = 11
SAMPLE_FRAC = 1
DROPOUT_RATE = 0.3
#Class weights for the imbalanceed full daataset
CLASS_WEIGHTS = {0:1.92971879,
                 1:0.93211113,
                 2:1.84661667,
                 3:0.72253217,
                 4:0.4758921 ,
                5:1.67547424,
                6:3.06134997,
                7:0.66806478,
                8:1.47934985,
                9:0.49944457,
                10:3.52695789}
#Whether to train the backbone of the model
TRAINABLE = True
#Labels for the industries
INDUSTRY_LABELS =  {0: 'Construction and Real Estate Development',
 1: 'Consumer Goods and Retail',
 2: 'Education and Research',
 3: 'Finance, Banking, Insurance and Accounting',
 4: 'Healthcare and Biotechnology',
 5: 'Hospitality, Travel, and Food Service',
 6: 'Legal and Consulting Services',
 7: 'Manufacturing',
 8: 'Sales, Marketing, and Recruitment',
 9: 'Technology',
 10: 'Transportation and Logistics'}
