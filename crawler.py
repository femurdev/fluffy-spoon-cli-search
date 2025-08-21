import sqlite3
import requests
from bs4 import BeautifulSoup
import argparse
from urllib.parse import urlparse

def create_connection():
    return sqlite3.connect('urls.sqlite')

def create_table():
    with create_connection() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL UNIQUE,
            title TEXT,
            description TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')

def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def crawl(url):
    if not is_valid_url(url):
        print(f"Invalid URL: {url}")
        return

    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch {url}: HTTP {response.status_code}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string if soup.title else 'No title'
        description_tag = soup.find('meta', attrs={'name': 'description'})
        description = description_tag['content'] if description_tag else 'No description'

        with create_connection() as conn:
            conn.execute('INSERT OR IGNORE INTO urls (url, title, description) VALUES (?, ?, ?)', (url, title, description))
            print(f"Crawled and saved: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Network error while crawling {url}: {e}")
    except Exception as e:
        print(f"Failed to crawl {url}: {e}")

def main():
    parser = argparse.ArgumentParser(description='Web Crawler')
    parser.add_argument('url', type=str, help='The URL to crawl')
    args = parser.parse_args()

    create_table()
    crawl(args.url)

if __name__ == '__main__':
    main()