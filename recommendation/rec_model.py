import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommendation(combine_input, filtered_jobs, k=5):
    """
    Recommends top k jobs for a given resume based on text similarity and retrieves job details.

    Parameters:
    - combine_input: A single resume description or list of resume descriptions (processed).
    - filtered_jobs: A DataFrame containing job details with columns 'processed_title' and 'processed_description'.
    - k: Number of top job recommendations.

    Returns:
    - pd.DataFrame: A DataFrame containing top job recommendations with 'title', 'company_name', 'description'.
    """
    # Ensure that combine_input is a list of strings
    if isinstance(combine_input, str):  # If it's a single resume string
        combine_input = [combine_input]  # Convert to a list

    # Create the 'combined' column in filtered_jobs by merging 'processed_title' and 'processed_description'
    filtered_jobs['combined'] = filtered_jobs['processed_title'] + " " + filtered_jobs['processed_description']

    # Vectorizing the text data (using the 'combined' column)
    vectorizer = TfidfVectorizer()
    job_desc_tfidf = vectorizer.fit_transform(filtered_jobs['combined'])

    # Prepare to store all DataFrames for top recommendations
    top_five_jobs_df = []

    # Process each resume in combine_input
    for resume in combine_input:
        resume_tfidf = vectorizer.transform([resume])  # Transform the single resume

        # Compute the cosine similarity between the resume and all job descriptions
        tfidf_similarity_scores = cosine_similarity(job_desc_tfidf, resume_tfidf).flatten()

        # Find the top k most similar jobs
        top_jobs = tfidf_similarity_scores.argsort()[::-1][:k]

        # Index rows from the DataFrame and get the relevant job details
        top_jobs_df = filtered_jobs.iloc[top_jobs][['title', 'company', 'description', 'jobProviders']]

        # Append to the list of results
        top_five_jobs_df.append(top_jobs_df)

    # Return the results as a list of DataFrames (one per resume) or a concatenated DataFrame
    return top_five_jobs_df if len(top_five_jobs_df) > 1 else top_five_jobs_df[0]