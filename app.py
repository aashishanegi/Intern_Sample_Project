import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL of the job listings page
base_url = "https://remoteok.com/remote-dev-jobs"

# Define headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

try:
    # Send a request to the website and get the HTML content
    response = requests.get(base_url, headers=headers)
    response.raise_for_status()  # Check if the request was successful

    soup = BeautifulSoup(response.content, 'html.parser')

    # Parse the HTML to extract job details
    job_titles = []
    companies = []
    locations = []
    salaries = []
    descriptions = []

    # Find all job cards on the page
    jobs = soup.find_all('tr', class_='job')

    for job in jobs:
        # Extract job title
        title = job.find('h2', itemprop='title')
        title = title.text.strip() if title else 'N/A'

        # Extract company name
        company = job.find('h3', itemprop='name')
        company = company.text.strip() if company else 'N/A'

        # Extract job location
        location = job.find('div', class_='location')
        location = location.text.strip() if location else 'Remote'

        # Extract salary (if available)
        salary = job.find('div', class_='salary')
        salary = salary.text.strip() if salary else 'N/A'

        # Extract job description
        description = job.find('td', class_='description')
        description = description.text.strip().replace('\n', ' ') if description else 'N/A'

        # Append details to lists
        job_titles.append(title)
        companies.append(company)
        locations.append(location)
        salaries.append(salary)
        descriptions.append(description)

    # Create a DataFrame and save the data to a CSV file
    jobs_df = pd.DataFrame({
        'Job Title': job_titles,
        'Company': companies,
        'Location': locations,
        'Salary': salaries,
        'Description': descriptions
    })

    jobs_df.to_csv('job_listings.csv', index=False)

    print("Job listings have been scraped and saved to 'job_listings.csv'")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
