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

def preprocessor(text):
    # Function to remove emojis using regex
    def remove_emoji(text):
        # Unicode range for most emojis
        emoji_pattern = re.compile(
            "["   
            "\U0001F600-\U0001F64F"  # emoticons
            "\U0001F300-\U0001F5FF"  # symbols & pictographs
            "\U0001F680-\U0001F6FF"  # transport & map symbols
            "\U0001F700-\U0001F77F"  # Alchemical symbols
            "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
            "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
            "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
            "\U0001FA00-\U0001FA6F"  # Chess Symbols
            "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
            "\U00002702-\U000027B0"  # Dingbats
            "\U000024C2-\U0001F251"  # Enclosed characters
            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

    # Clean the text
    def text_cleaner(text):
        # Remove emojis from the text
        text = remove_emoji(text)
        
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
