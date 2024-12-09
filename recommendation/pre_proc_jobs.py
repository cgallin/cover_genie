import pandas as pd
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
import nltk
from bert.pre_proc_linkedin import clean_text

# path1 = 'raw_data/jobs_api_data.csv'
# jobs_df = pd.read_csv(path1)

# path2 = "raw_data/marketing-resume-example.pdf"
# resume = pdf_to_text(path2)

def filter_dataframe(df, location, industry):
    """
    Filters the DataFrame by location and industry.

    Parameters:
        df (pd.DataFrame): The DataFrame to filter. Must have 'location' and 'industries' columns.
        location (str): The location to filter by.
        industry (str): The industry to filter by.

    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    if 'location' not in df.columns or 'industries' not in df.columns:
        raise ValueError("The DataFrame must contain 'location' and 'industries' columns.")

    filtered_df = df[(df['location'] == location) & (df['industries'] == industry)]
    return filtered_df



# Function to clean the text
def text_cleaner(input_text):
    """
    Cleans text by removing emojis, non-alphabetic characters (except periods),
    and converting to lowercase.

    Args:
        input_text (str): The input string to clean.

    Returns:
        str: The cleaned string.
    """
    def remove_emoji(text):
        emoji_pattern = re.compile(
            "[" "\U0001F600-\U0001F64F" "\U0001F300-\U0001F5FF" "\U0001F680-\U0001F6FF"
            "\U0001F700-\U0001F77F" "\U0001F780-\U0001F7FF" "\U0001F800-\U0001F8FF"
            "\U0001F900-\U0001F9FF" "\U0001FA00-\U0001FA6F" "\U0001FA70-\U0001FAFF"
            "\U00002702-\U000027B0" "\U000024C2-\U0001F251" "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

    # Remove emojis
    text = remove_emoji(input_text)
    # Remove non-alphabetic characters except periods and convert to lowercase
    cleaned_text = re.sub('[^a-zA-Z. ]', ' ', text).lower()
    return cleaned_text


# Function to tokenize and process sentences
def tokenize(text):
    """
    Tokenizes text by removing stopwords, lemmatizing, and filtering POS tags.

    Args:
        text (str): The input string to tokenize and process.

    Returns:
        list: A list of tokenized words after processing.
    """
    stop_words = set(stopwords.words('english')).union(stopwords.words('french'))
    lemmatizer = WordNetLemmatizer()

    tokenized_words = []

    sentences = sent_tokenize(text)  # Tokenize sentences
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
        # Extend the tokenized_words list
        tokenized_words.extend(lemmatized_words)

    return " ".join(tokenized_words)

# CALL: filtered_df = filter_dataframe(jobs_df, "Toronto", "Technology")


# Example preprocessor function
def preprocessor(input_text):
    """
    Preprocess a single string by cleaning and tokenizing.

    Args:
        input_text (str): The input string to preprocess.

    Returns:
        str: The processed string.
    """
    cleaned_text = text_cleaner(input_text)
    processed_text = tokenize(cleaned_text)
    return processed_text

# CALL: rec = recommendation("engineer", resume, jobs_df.loc[:1000], k=5)
# rec
