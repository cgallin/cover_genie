import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommendation(resume_text, job_text, df, k=5):
    """
    Recommends top k jobs for a given resume based on text similarity and retrieves job details.

    Parameters:
    - resume_text: A single resume description or list of resume descriptions (processed).
    - job_text: A list or Series of job descriptions (processed).
    - df: A DataFrame containing job details with columns 'title', 'company_name', 'description'.
    - k: Number of top job recommendations.

    Returns:
    - pd.DataFrame: A DataFrame containing top job recommendations with 'title', 'company_name', 'description'.
    """
    # Ensure that resume_text is a list of strings
    if isinstance(resume_text, str):  # If it's a single resume string
        resume_text = [resume_text]  # Convert to a list

    if isinstance(job_text, pd.Series):  # If job_text is a pandas Series
        job_text = job_text.tolist()  # Convert to a list of strings

    # Ensure job_text is a list of strings
    if not isinstance(job_text, list):
        raise ValueError("job_text should be a list of strings.")

    # Vectorizing the text data
    vectorizer = TfidfVectorizer()
    job_desc_tfidf = vectorizer.fit_transform(job_text)

    # Prepare to store all DataFrames for top recommendations
    all_top_jobs_df = []

    # Process each resume in resume_text
    for resume in resume_text:
        resume_tfidf = vectorizer.transform([resume])  # Transform the single resume

        # Compute the cosine similarity between the resume and all job descriptions
        tfidf_similarity_scores = cosine_similarity(job_desc_tfidf, resume_tfidf).flatten()

        # Find the top k most similar jobs
        top_jobs = tfidf_similarity_scores.argsort()[::-1][:k]

        # Index rows from the DataFrame
        top_jobs_df = df.iloc[top_jobs][['title', 'company_name', 'description']]

        # Append to the list of results
        all_top_jobs_df.append(top_jobs_df)

    # Return the results as a list of DataFrames (one per resume) or a concatenated DataFrame
    return all_top_jobs_df if len(all_top_jobs_df) > 1 else all_top_jobs_df[0]
