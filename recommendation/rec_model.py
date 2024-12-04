from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommendation(resume_words, job_desc_words, k=5):
    # Combine all text data for fitting the vectorizer
    resumes = resume_words['processed_description'].str.split().sum()
    job_desc = job_desc_words['processed_description'].str.split().sum()

    # Vectorizing the text data
    vectorizer = TfidfVectorizer()
    job_desc_tfidf = vectorizer.fit_transform(job_desc_words['processed_description'])
    resume_tfidf = vectorizer.transform(resume_words['processed_description'])

    # Compute the cosine similarity between job descriptions and resumes
    tfidf_similarity_matrix = cosine_similarity(job_desc_tfidf, resume_tfidf)

    # Iterate through each resume and find the top k most similar jobs
    for resume_idx in range(tfidf_similarity_matrix.shape[1]):  # Loop over resumes
        top_jobs = tfidf_similarity_matrix[:, resume_idx].argsort()[::-1][:k]
        print(f"Resume {resume_idx}: Top {k} jobs")
        for job_idx in top_jobs:
            similarity_score = tfidf_similarity_matrix[job_idx, resume_idx]
            print(f"  Job {job_idx}, Similarity: {similarity_score:.4f}")