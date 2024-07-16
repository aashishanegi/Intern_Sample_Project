import requests
from bs4 import BeautifulSoup
import re
import csv

# Function to extract salon data from a single salon page
def extract_salon_data(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Example: Extracting salon name
            salon_name = soup.find('h1').text.strip()

            # Example: Extracting categories
            categories = []
            category_tags = soup.find_all('div', {'class': 'category'})
            for tag in category_tags:
                categories.append(tag.text.strip())

            # Example: Extracting photos (assuming photo URLs are in img tags)
            photos = []
            photo_tags = soup.find_all('img', {'class': 'salon-photo'})
            for tag in photo_tags:
                photos.append(tag['src'])

            # Example: Extracting website URL
            website_url = soup.find('a', {'class': 'salon-website'})['href']

            # Example: Extracting phone number (assuming it's in a specific format)
            phone_number = None
            phone_tag = soup.find('span', {'class': 'phone-number'})
            if phone_tag:
                phone_number = phone_tag.text.strip()

            return {
                'salon_name': salon_name,
                'categories': categories,
                'photos': photos,
                'website_url': website_url,
                'phone_number': phone_number
            }
        else:
            print(f"Failed to retrieve page: {url}")
            return None
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return None

# Function to scrape salons for a given city
def scrape_salons_in_city(city_url):
    try:
        response = requests.get(city_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Example: Finding all salon links on the city page
            salon_links = []
            link_tags = soup.find_all('a', {'class': 'salon-link'})
            for tag in link_tags:
                salon_links.append(tag['href'])

            # Scraping data for each salon link
            salon_data_list = []
            for link in salon_links:
                salon_data = extract_salon_data(link)
                if salon_data:
                    salon_data_list.append(salon_data)

            return salon_data_list
        else:
            print(f"Failed to retrieve page: {city_url}")
            return None
    except Exception as e:
        print(f"Error scraping {city_url}: {str(e)}")
        return None

# Example usage: Scrape salons in multiple cities
cities = [
    'https://example-city1-salons.com',
    'https://example-city2-salons.com',
    # Add more cities as needed
]

all_salons_data = []
for city_url in cities:
    city_salons_data = scrape_salons_in_city(city_url)
    if city_salons_data:
        all_salons_data.extend(city_salons_data)

# Example: Save scraped data to CSV
if all_salons_data:
    keys = all_salons_data[0].keys()
    with open('salons_data.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_salons_data)

    print("Salon data saved to salons_data.csv")
else:
    print("No salon data scraped.")