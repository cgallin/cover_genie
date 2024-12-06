import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommendation(user_cv, job_title, filtered_jobs, k=5):
    """
    Recommends top k jobs for a given resume based on text similarity and retrieves job details.

    Parameters:
    - user_cv: A processed resume description (string).
    - job_title: A processed job title (string).
    - filtered_jobs: A DataFrame containing job details with columns 'processed_title' and 'processed_description'.
    - k: Number of top job recommendations.

    Returns:
    - pd.DataFrame: A DataFrame containing top job recommendations with 'title', 'company_name', 'description'.
    """
    # Combine job title and user CV into one string
    combine_input = job_title + " " + user_cv  # Combine job title and CV

    # Create the 'combined' column in filtered_jobs by merging 'processed_title' and 'processed_description'
    filtered_jobs['combined'] = filtered_jobs['processed_title'] + " " + filtered_jobs['processed_description']

    # Vectorizing the text data (using the 'combined' column)
    vectorizer = TfidfVectorizer()
    job_desc_tfidf = vectorizer.fit_transform(filtered_jobs['combined'])

    # Vectorizing the resume input
    resume_tfidf = vectorizer.transform([combine_input])  # Transform the combined job title + user CV

    # Compute the cosine similarity between the resume and all job descriptions
    tfidf_similarity_scores = cosine_similarity(job_desc_tfidf, resume_tfidf).flatten()

    # Find the top k most similar jobs
    top_jobs = tfidf_similarity_scores.argsort()[::-1][:k]

    # Index rows from the DataFrame and get the relevant job details
    top_jobs_df = filtered_jobs.iloc[top_jobs][['title', 'company', 'description', 'jobProviders']]

    # Return the top k job recommendations
    return top_jobs_df
