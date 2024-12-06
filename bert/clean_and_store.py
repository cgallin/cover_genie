import pickle
import pandas as pd
from bert.pre_proc_linkedin import clean_text, load_data, features_encoder

X, y = load_data()
X = X.apply(lambda x: clean_text(x))
y_encoded = features_encoder(y)

df = pd.DataFrame({'description_cleaned': X, 'industry': y, 'label': y_encoded})

with open('/Users/camerongallinger/code/cgallin/cover_genie/bert/clean_data/data.pkl', 'wb') as f:
    pickle.dump(df, f)

print(df.shape, df.industry.nunique())
