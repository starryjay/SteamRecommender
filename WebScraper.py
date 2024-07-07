# Import necessary libraries

import requests
from bs4 import BeautifulSoup

# Import csv module
import csv

# Import regex
import re

import json

url = " http://store.steampowered.com/api/appdetails?appids={APP_ID}"

response = requests.get(url)

page_content = response.text
page_content

doc = BeautifulSoup(page_content, 'html.parser')
games = doc.find_all('div', {'class': 'responsive_search_name_combined'})

with open('applist.json', mode='r') as applist:
    apps = json.load(applist)

for app in apps:
    url = " http://store.steampowered.com/api/appdetails?appids={app}"
    response = requests.get(url)
    page_content = response.text

print(page_content)

# Create the scraper component to save the result as a CSV file using the CSV module
# with open('games_topsellers.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Published Date', 'Original Price', 'Discount Price', 'Reviews'])

#     # Loop through each game and extract the relevant information
#     for game in games:
#         name = game.find('span', {'class': 'title'}).text
#         published_date = game.find('div', {'class': 'col search_released responsive_secondrow'}).text.strip()

#         # Check if the element is present before accessing the text attribute
#         original_price_elem = game.find('div', {'class': 'discount_original_price'})
#         original_price = original_price_elem.text.strip() if original_price_elem else 'N/A'

#         discount_price_elem = game.find('div', {'class': 'discount_final_price'})
#         discount_price = discount_price_elem.text.strip() if discount_price_elem else 'N/A'

#         # Extract review information using regular expressions
#         review_summary = game.find('span', {'class': 'search_review_summary'})
#         reviews_html = review_summary['data-tooltip-html'] if review_summary else 'N/A'

#         # Use regular expressions to extract the number of reviews
#         match = re.search(r'(\d+,*\d*)\s+user reviews', reviews_html)
#         reviews_number = match.group(1).replace(',', '') if match else 'N/A'

#         # Write the extracted information to the CSV file
#         writer.writerow([name, published_date, original_price, discount_price, reviews_number])

# # List of search filters
# search_filters = ['']

# # Create a CSV file to store the scraped data
# with open('games_all.csv', mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Name', 'Published_Date', 'Original Price', 'Discount Price', 'Reviews', 'Search Query'])

#     # Loop through each search query
#     for filter in search_filters:
#         # URL of the website to be scraped for the current search query
#         url = f'https://store.steampowered.com/search/?term='

#         # Send a GET request to the specified URL
#         response = requests.get(url)

#         # Parse the HTML content of the page using BeautifulSoup
#         webpage = BeautifulSoup(response.content, 'html.parser')

#         # Find the total number of pages
#         total_pages = int(webpage.find('div', {'class': 'search_pagination_right'}).find_all('a')[-2].text)

#         # Counter to keep track of the number of lines written
#         line_count = 0

#         # Loop through each page and extract the relevant information
#         for page in range(1, total_pages + 1):
#             # Send a GET request to the specified URL
#             response = requests.get(url + '&page=' + str(page))

#             # Parse the HTML content of the page using BeautifulSoup
#             doc = BeautifulSoup(response.content, 'html.parser')

#             # Find all the games on the page
#             games = doc.find_all('div', {'class': 'responsive_search_name_combined'})

#             # Loop through each game and extract the relevant information
#             for game in games:
#                 name = game.find('span', {'class': 'title'}).text
#                 published_date = game.find('div', {'class': 'col search_released responsive_secondrow'}).text.strip()

#                 # Check if the element is present before accessing the text attribute
#                 original_price_elem = game.find('div', {'class': 'discount_original_price'})
#                 original_price = original_price_elem.text.strip() if original_price_elem else 'N/A'

#                 discount_price_elem = game.find('div', {'class': 'discount_final_price'})
#                 discount_price = discount_price_elem.text.strip() if discount_price_elem else 'N/A'

#                 # Extract review information using regular expressions
#                 review_summary = game.find('span', {'class': 'search_review_summary'})
#                 reviews_html = review_summary['data-tooltip-html'] if review_summary else 'N/A'

#                 # Use regular expressions to extract the number of reviews
#                 match = re.search(r'(\d+,*\d*)\s+user reviews', reviews_html)
#                 reviews_number = match.group(1).replace(',', '') if match else 'N/A'

#                 # Write the extracted information to the CSV file
#                 writer.writerow([name, published_date, original_price, discount_price, reviews_number, filter])

#                 # Increment the line count
#                 line_count += 1

#                 # Stop scraping if we have reached the minimum data requirement
#                 if line_count > 100:
#                     break

#             # Stop scraping if we have reached the minimum data requirement
#             if line_count > 100:
#                 break

# # Create a function that takes url and get the total page
# def get_total_pages(url):
#     response = requests.get(url)
#     doc = BeautifulSoup(response.content, 'html.parser')
#     total_pages = int(doc.find('div', {'class': 'search_pagination_right'}).find_all('a')[-2].text)
#     return total_pages

# # Create a function that extracts game info from the webpage
# def extract_game_info(game):
#     name = game.find('span', {'class': 'title'}).text
#     published_date = game.find('div', {'class': 'col search_released responsive_secondrow'}).text.strip()

#     original_price_elem = game.find('div', {'class': 'discount_original_price'})
#     original_price = original_price_elem.text.strip() if original_price_elem else 'N/A'

#     discount_price_elem = game.find('div', {'class': 'discount_final_price'})
#     discount_price = discount_price_elem.text.strip() if discount_price_elem else 'N/A'

#     review_summary = game.find('span', {'class': 'search_review_summary'})
#     reviews_html = review_summary['data-tooltip-html'] if review_summary else 'N/A'

#     match = re.search(r'(\d+,*\d*)\s+user reviews', reviews_html)
#     reviews_number = match.group(1).replace(',', '') if match else 'N/A'

#     return name, published_date, original_price, discount_price, reviews_number

# # Create a function that scrapes the webpage
# def scrape_page(url, filter, writer):
#     # Invoking get total page function
#     total_pages = get_total_pages(url)

#     line_count = 0

#     for page in range(1, total_pages + 1):
#         response = requests.get(f"{url}&page={page}")
#         doc = BeautifulSoup(response.content, 'html.parser')
#         games = doc.find_all('div', {'class': 'responsive_search_name_combined'})

#         for game in games:
#             # Invoking the extract game info function
#             game_info = extract_game_info(game)
#             writer.writerow([*game_info, filter])

#             line_count += 1
#             if line_count > 100:
#                 break

#         if line_count > 100:
#             break


# # Creating the main function that takes the scrape page function and do the actual scraping
# def main(search_queries=["topsellers"]):

#     with open('games_all.csv', mode='w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerow(['Name', 'Date', 'Original Price', 'Discount Price', 'Reviews', 'Search Filter'])

#         for filter in search_filters:
#             url = f'https://store.steampowered.com/search/?filter={filter}'
#             # Invoking the scrape page function
#             scrape_page(url, filter, writer)


# # Invoking the main function
# search_queries = ['none']
# main(search_queries)