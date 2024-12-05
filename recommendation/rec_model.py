from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommendation(resume_text, job_texts, k=5):
    """
    Recommends top k jobs for a given resume based on text similarity.

    Parameters:
    - resume_text: A single resume description (processed).
    - job_texts: List or Series of job descriptions (processed).
    - k: Number of top job recommendations.

    Returns:
    - List of tuples containing job indices and similarity scores for the top k jobs.
    """
    # Ensure inputs are in the correct format
    if isinstance(job_texts, list):
        job_texts = pd.Series(job_texts)

    # Vectorizing the text data
    vectorizer = TfidfVectorizer()
    job_desc_tfidf = vectorizer.fit_transform(job_texts)
    resume_tfidf = vectorizer.transform([resume_text])  # Transform single resume

    # Compute the cosine similarity between the resume and all job descriptions
    tfidf_similarity_scores = cosine_similarity(job_desc_tfidf, resume_tfidf).flatten()

    # Find the top k most similar jobs
    top_jobs = tfidf_similarity_scores.argsort()[::-1][:k]
    top_job_scores = [(job_idx, tfidf_similarity_scores[job_idx]) for job_idx in top_jobs]

    return top_job_scores