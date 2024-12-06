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

def filter_location_and_industries(df, location, industries):
    """
    Filters the jobs dataframe by location and industries.

    """
    filtered_df = df[df['location'] == location]
    if industries:
        filtered_df = filtered_df[filtered_df['industries'].isin(industries)]
    return filtered_df

# Is used to preprocess the cv_text that will be inputed by the user

def preprocess_text(input_text):
    """
    Preprocess a single string:
    - Remove emojis
    - Clean text (remove non-alphabetic characters, convert to lowercase)
    - Process sentences (remove stopwords, lemmatize, extract features)

    Args:
        input_text (str): The input string to preprocess.

    Returns:
        str: The processed string.
    """

    # Function to remove emojis using regex
    def remove_emoji(text):
        emoji_pattern = re.compile(
            "[" "\U0001F600-\U0001F64F" "\U0001F300-\U0001F5FF" "\U0001F680-\U0001F6FF"
            "\U0001F700-\U0001F77F" "\U0001F780-\U0001F7FF" "\U0001F800-\U0001F8FF"
            "\U0001F900-\U0001F9FF" "\U0001FA00-\U0001FA6F" "\U0001FA70-\U0001FAFF"
            "\U00002702-\U000027B0" "\U000024C2-\U0001F251" "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

    # Function to clean the text
    def text_cleaner(text):
        # Remove emojis
        text = remove_emoji(text)
        # Remove non-alphabetic characters and convert to lowercase
        cleaned_text = re.sub('[^a-zA-Z]', ' ', text).lower()
        return cleaned_text

    # Function to process sentences and extract features
    def process_sentences(text):
        stop_words = set(stopwords.words('english')).union(stopwords.words('french'))
        lemmatizer = WordNetLemmatizer()

        def extract_features(text):
            features = ""
            sentences = sent_tokenize(text)
            for sent in sentences:
                # Tokenize words
                words = word_tokenize(sent)
                # Remove stopwords
                words = [word for word in words if word not in stop_words]
                # Tag parts of speech
                tagged_words = pos_tag(words)
                # Filter out specific POS tags
                filtered_words = [word for word, tag in tagged_words if tag not in ['DT', 'IN', 'TO', 'PRP', 'WP']]
                # Lemmatize words
                lemmatized_words = [lemmatizer.lemmatize(word, pos='v') for word in filtered_words]
                lemmatized_words = [lemmatizer.lemmatize(word, pos='n') for word in lemmatized_words]
                # Append processed words to features
                features += " ".join(lemmatized_words) + " "
            return features.strip()

        # Extract features from the text
        return extract_features(text)

    # Apply preprocessing steps
    cleaned_text = text_cleaner(input_text)
    processed_text = process_sentences(cleaned_text)

    return processed_text
