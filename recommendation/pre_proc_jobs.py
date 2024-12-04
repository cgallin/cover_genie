import pandas as pd
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import nltk

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def preprocessor(df):
    # Clean and preprocess text
    def text_cleaner(df):
        if 'description' not in df.columns:
            raise ValueError("DataFrame must contain a 'description' column.")
        
        # Drop rows with missing descriptions
        df_cleaned = df.dropna(subset=['description']).copy()
        
        # Apply regex to clean text (keep only letters, replace others with space)
        df_cleaned['description'] = df_cleaned['description'].apply(lambda x: re.sub('[^a-zA-Z]', ' ', x))
        
        # Convert to lowercase
        df_cleaned['description'] = df_cleaned['description'].str.lower()
        
        return df_cleaned['description']

    # Process sentences within the cleaned text
    def process_sentences(texts):
        # Set up stopwords and lemmatizer
        stop_words = set(stopwords.words('english')).union(stopwords.words('french'))
        lemmatizer = WordNetLemmatizer()
        
        # Extract features from sentences
        def extract_features(text):
            features = {'feature': ""}
            sentences = sent_tokenize(text)
            for sent in sentences:
                # Tokenize, remove stopwords, and filter by POS tags
                words = word_tokenize(sent)
                words = [word for word in words if word not in stop_words]
                tagged_words = pos_tag(words)
                filtered_words = [word for word, tag in tagged_words if tag not in ['DT', 'IN', 'TO', 'PRP', 'WP']]
                
                # Lemmatize remaining words
                lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in filtered_words]
                lemmatized_words = [lemmatizer.lemmatize(word, pos='n') for word in lemmatized_words]
                
                # Append to features
                features['feature'] += " ".join(lemmatized_words) + " "
            return features['feature']
        
        # Apply feature extraction to all texts
        return texts.apply(extract_features)
    
    # Apply text cleaning
    cleaned_text = text_cleaner(df)
    
    # Process sentences and extract features
    processed_text = process_sentences(cleaned_text)
    
    # Add processed text as a new column
    df['processed_description'] = processed_text
    return df[['processed_description']].copy()
