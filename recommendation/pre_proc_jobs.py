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
        return texts.apply(word_tokenize)

    tokens = tokenizer(text)

    # Remove stopwords
    def remove_stopwords(tokens):
        stop_words = set(stopwords.words('english')).union(stopwords.words('french'))
        return tokens.apply(lambda words: [w for w in words if w not in stop_words])

    no_stopword_tokens = remove_stopwords(tokens)

    # Lemmatize text
    def lemmatize(tokens):
        lemmatizer = WordNetLemmatizer()
        
        def lemmatize_words(words):
            # Lemmatize verbs and nouns
            lemmatized_verbs = [lemmatizer.lemmatize(word, pos='v') for word in words]
            lemmatized_nouns = [lemmatizer.lemmatize(word, pos='n') for word in lemmatized_verbs]
            return lemmatized_nouns
        
        return tokens.apply(lemmatize_words)

    lemmatized_tokens = lemmatize(no_stopword_tokens)

    # Return lemmatized tokens as a new DataFrame column
    df['processed_description'] = lemmatized_tokens
    
    #Return new DataFrame with cleaned text
    return pd.DataFrame(df['processed_description'])