import sys
import sqlite3
import requests
from bs4 import BeautifulSoup
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_database():
    logging.debug("Initializing the database.")
    conn = sqlite3.connect('urls.sqlite')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS webpages (
                        id INTEGER PRIMARY KEY,
                        url TEXT UNIQUE,
                        content TEXT)''')
    conn.commit()
    conn.close()
    logging.debug("Database initialized successfully.")

def crawl_url(url):
    try:
        logging.info(f"Crawling URL: {url}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        store_webpage(url, text)
        logging.info(f"Successfully crawled and stored content for: {url}")
    except requests.exceptions.RequestException as e:
        logging.error(f"HTTP request failed for {url}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error while crawling {url}: {e}")

def store_webpage(url, content):
    try:
        logging.debug("Storing webpage content in the database.")
        conn = sqlite3.connect('urls.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO webpages (url, content) VALUES (?, ?)", (url, content))
        conn.commit()
        conn.close()
        logging.info(f"Stored content for URL: {url}")
    except sqlite3.Error as e:
        logging.error(f"Database error while storing content for {url}: {e}")

def main():
    if len(sys.argv) != 2:
        logging.error("Invalid number of arguments. Usage: python3 crawl.py \"url\"")
        sys.exit(1)

    url = sys.argv[1]
    logging.debug("Starting the crawling process.")
    initialize_database()
    crawl_url(url)
    logging.debug("Crawling process completed.")

if __name__ == "__main__":
    main()