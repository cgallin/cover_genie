import pandas as pd
import json
import http.client
import urllib.parse
import numpy as np

def fetch_jobs_from_api(job_names, location, desired_job_count):
    """
    Fetches job postings from the API based on job titles and location.

    Parameters:
        job_names (list): A list of 3 job titles to search for.
        location (str): The location for the job search.
        desired_job_count (int): The maximum number of job postings to fetch.

    Returns:
        list: A list of job postings up to the desired count.
    """
    if len(job_names) != 3:
        raise ValueError("job_names must contain exactly 3 job titles.")
    if not isinstance(location, str):
        raise ValueError("location must be a string.")
    if not isinstance(desired_job_count, int) or desired_job_count <= 0:
        raise ValueError("desired_job_count must be a positive integer.")

    # API connection and headers
    conn = http.client.HTTPSConnection("jobs-api14.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "173d9a60b9msh53fa01c37acf944p113340jsn2647853edbca",
        'x-rapidapi-host': "jobs-api14.p.rapidapi.com"
    }

    all_jobs = []  # To store the fetched jobs

    # Nested loop to iterate over job names combinations
    for job_name1 in job_names:
        for job_name2 in job_names:  # Second loop through job_names
            # Set query parameters dynamically
            params = {
                "location": location,
                "query": f"{job_name1} {job_name2}"  # Combine job names
            }
            # Encode parameters into a query string
            query_string = urllib.parse.urlencode(params)
            url = f"/v2/list?{query_string}"

            # Send API request
            conn.request("GET", url, headers=headers)
            res = conn.getresponse()
            data = res.read()

            # Parse response
            decoded = json.loads(data.decode("utf-8"))
            jobs = decoded.get("jobs", [])

            # Add jobs to the list
            all_jobs.extend(jobs)

            # Stop if we reach the desired job count
            if len(all_jobs) >= desired_job_count:
                break
        if len(all_jobs) >= desired_job_count:
            break

    # Limit to the desired number of jobs
    all_jobs = all_jobs[:desired_job_count]

    # Print the number of jobs fetched
    print(f"Total jobs fetched: {len(all_jobs)}")
    return all_jobs

def clean_api_jobs(all_jobs):
    df = pd.DataFrame(all_jobs)
    df['jobProviders'] = df['jobProviders'].apply(
        lambda row: ", ".join([d.get('url', '') for d in row]) if isinstance(row, list) else row)
    df = df.drop(columns=["image", "salaryRange"])
    df = df.drop_duplicates()
    df["industries"] = np.nan
    return df
