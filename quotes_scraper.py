import requests
from bs4 import BeautifulSoup
import csv
from prettytable import PrettyTable

base_url = "https://quotes.toscrape.com"
url = base_url
cleaned_data = []

while url:
    # Step 1: Fetch and parse the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 2: Extract quotes
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        raw_text = quote.find('span', class_='text').get_text()
        raw_author = quote.find('small', class_='author').get_text()

        # Step 3: Clean text
        clean_text = raw_text.strip().replace('“', '').replace('”', '').replace('’', "'")
        clean_author = raw_author.strip()

        cleaned_data.append({"quote": clean_text, "author": clean_author})

    # Step 4: Check for next page
    next_btn = soup.find('li', class_='next')
    if next_btn:
        next_link = next_btn.find('a')['href']
        url = base_url + next_link
    else:
        url = None

# Step 5: Save to CSV
with open('cleaned_quotes.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["quote", "author"])
    writer.writeheader()
    writer.writerows(cleaned_data)

print("✅ All pages scraped. Data saved to cleaned_quotes.csv")

# Step 6: Display in table
table = PrettyTable()
table.field_names = ["Quote", "Author"]

for item in cleaned_data:
    table.add_row([item['quote'], item['author']])

print("\n📋 All Cleaned Quotes:\n")
print(table)
