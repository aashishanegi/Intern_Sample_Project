import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the job listings CSV file into a DataFrame
jobs_df = pd.read_csv('job_listings.csv')

# Display basic information about the DataFrame
print(jobs_df.info())
print(jobs_df.head())

# Plot the distribution of job titles
plt.figure(figsize=(12, 6))
sns.countplot(y='Job Title', data=jobs_df, order=jobs_df['Job Title'].value_counts().index)
plt.title('Distribution of Job Titles')
plt.xlabel('Count')
plt.ylabel('Job Title')
plt.show()

# Plot the distribution of companies
plt.figure(figsize=(12, 6))
sns.countplot(y='Company', data=jobs_df, order=jobs_df['Company'].value_counts().index)
plt.title('Distribution of Companies')
plt.xlabel('Count')
plt.ylabel('Company')
plt.show()

# Plot the distribution of job locations
plt.figure(figsize=(12, 6))
sns.countplot(y='Location', data=jobs_df, order=jobs_df['Location'].value_counts().index)
plt.title('Distribution of Job Locations')
plt.xlabel('Count')
plt.ylabel('Location')
plt.show()

# Plot the distribution of salaries (if available)
plt.figure(figsize=(12, 6))
salaries = jobs_df[jobs_df['Salary'] != 'N/A']['Salary']
sns.countplot(y=salaries, order=salaries.value_counts().index)
plt.title('Distribution of Salaries')
plt.xlabel('Count')
plt.ylabel('Salary')
plt.show()
