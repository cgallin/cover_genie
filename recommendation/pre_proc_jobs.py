import pandas as pd
import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

def filter_location_and_industries(df, location, industries):
    """
    Filters the jobs dataframe by location and industries.

    Parameters:
    df (pd.DataFrame): The dataframe containing job listings.
    location (str): The location to filter by.
    industries (list): The list of industries to filter by.

    Returns: A dataframe containing jobs in the specified location and industries.
    """
    filtered_df = df[df['location'] == location]
    if industries:
        filtered_df = filtered_df[filtered_df['industries'].isin(industries)]

    columns_to_keep = ['title', 'company', 'description']
    filtered_df = filtered_df[columns_to_keep]

    return filtered_df


def preprocessor(text):
    # Clean the text
    def text_cleaner(text):
        # Apply regex to clean text (keep only letters, replace others with space)
        cleaned_text = re.sub('[^a-zA-Z]', ' ', text)

        # Convert to lowercase
        cleaned_text = cleaned_text.lower()

        return cleaned_text

    # Process sentences within the cleaned text
    def process_sentences(text):
        # Set up stopwords and lemmatizer
        stop_words = set(stopwords.words('english')).union(stopwords.words('french'))
        lemmatizer = WordNetLemmatizer()

        # Extract features from sentences
        def extract_features(text):
            features = ""
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
                features += " ".join(lemmatized_words) + " "
            return features.strip()

        # Apply feature extraction to the text
        return extract_features(text)

    # Apply text cleaning
    cleaned_text = text_cleaner(text)

    # Process sentences and extract features
    processed_text = process_sentences(cleaned_text)

    return processed_text
