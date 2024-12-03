import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

def preprocessor(df):
    def text_cleaner(df):
        # Ensure 'description' column exists
        if 'description' not in df.columns:
            raise ValueError("DataFrame must contain a 'description' column.")
        
        # Drop rows with missing 'description' values
        df_cleaned = df.dropna(subset=['description'])
        
        # Convert text to lowercase and remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        df_cleaned['description'] = df_cleaned['description'].str.lower().str.translate(translator)
        
        # Remove numbers
        df_cleaned['description'] = df_cleaned['description'].str.replace(r'\d+', '', regex=True)
        
        return df_cleaned['description']

    text = text_cleaner(df)

    # Tokenize the text
    def tokenizer(texts):
        word_tokens = []
        for word in texts:
            word_tokens.append(word_tokenize(word))
        return word_tokens

    tokens = tokenizer(text)

    # Remove stopwords
    def stopword(text):
        stop_words = set(stopwords.words('english', 'french'))
        tokens_cleaned = [w for w in text if not w in stop_words]
        return tokens_cleaned

    no_stopword_tokens = stopword(tokens[0])

    # Lemmatize text
    def lemmatizer(text):
        # Lemmatizing the verbs
        verb_lemmatized = [
            WordNetLemmatizer().lemmatize(word, pos = "v") # v --> verbs
            for word in text
        ]

        # 2 - Lemmatizing the nouns
        noun_lemmatized = [
            WordNetLemmatizer().lemmatize(word, pos = "n") # n --> nouns
            for word in verb_lemmatized
        ]
        return noun_lemmatized

    imp_words = lemmatizer(no_stopword_tokens)

    return imp_words