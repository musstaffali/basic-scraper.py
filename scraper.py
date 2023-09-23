import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "http://quotes.toscrape.com/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract and print quotes
quotes = soup.select(".text")
for quote in quotes:
    print(quote.get_text())

# Extract and print authors
authors = soup.select(".author")
for author in authors:
    print(author.get_text())
