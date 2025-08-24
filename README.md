# quotes_scraper

🕸️ Web Quotes Scraper

A Python-based scraper that collects inspirational quotes from the web and stores them in a clean dataset.
This project demonstrates web scraping, data cleaning, and storage using Scrapy and Python.

🔧 Features

Scrapes quotes (text + author) from websites

Handles pagination automatically

Cleans and structures scraped data

Exports to CSV/JSON format

🛠️ Tech Stack

Language: Python

Framework: Scrapy

Libraries: Pandas, Requests, BeautifulSoup (optional)

Output: CSV, JSON

📂 Project Structure

quotes_scraper/
│── quotes/
│ ├── spiders/
│ │ └── quotes_spider.py # Core scraper logic
│ ├── items.py # Data structure
│ ├── pipelines.py # Data cleaning pipeline
│ └── settings.py # Scrapy settings
│── data/
│ └── quotes.csv # Cleaned output
│── README.md

🚀 Getting Started

Clone the repo
git clone https://github.com/yourusername/quotes_scraper.git
cd quotes_scraper

Install dependencies
pip install scrapy pandas

Run the scraper
scrapy crawl quotes -o data/quotes.csv

📌 Future Enhancements

Add multi-site scraping

Build a REST API for serving scraped quotes

Integrate with frontend dashboard
