import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "http://quotes.toscrape.com/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print("Successfully connected to the website.")
else:
    print(f"Failed to connect to the website. Status code: {response.status_code}")
    exit()

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract and print quotes
quotes = soup.select(".text")
print("Quotes:")
for quote in quotes:
    # Use .get_text() to extract the text content of the HTML element
    print(quote.get_text())

# Extract and print authors
authors = soup.select(".author")
print("\nAuthors:")
for author in authors:
    # Use .get_text() to extract the text content of the HTML element
    print(author.get_text())

# Suggestions for building upon this project:
# 1. Data Storage: Save the scraped data to a file or a database for later analysis.
# 2. Advanced Scraping: Learn how to navigate through multiple pages and scrape data from paginated websites.
# 3. Data Analysis: Analyze the scraped data, perform sentiment analysis, or generate statistics.
# 4. Visualizations: Create graphs or visual representations of the data using libraries like Matplotlib or Plotly.
# 5. User Interaction: Build a simple web interface or CLI for users to input URLs and see the results.
# 6. Error Handling: Implement more robust error handling to gracefully handle various HTTP and parsing errors.
# 7. Scheduled Scraping: Set up a scheduler (e.g., using Cron) to run the scraper at specified intervals.
# 8. Legal Compliance: Ensure that your scraping activities comply with the website's terms of service and legal requirements.
# 9. User Agents: Consider setting custom user agents to mimic different web browsers and avoid being blocked.

# Don't forget to document any changes or additional functionalities in your README.md file.
