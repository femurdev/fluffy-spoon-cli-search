import sys
import sqlite3
import requests
from bs4 import BeautifulSoup
import logging
import time
import threading
from queue import Queue

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_database():
    logging.info("Initializing the database.")
    conn = sqlite3.connect('urls.sqlite')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS webpages (
                        id INTEGER PRIMARY KEY,
                        url TEXT UNIQUE,
                        title TEXT,
                        description TEXT,
                        content TEXT)''')
    cursor.execute('DELETE FROM webpages')  # Wipe old data
    conn.commit()
    conn.close()
    logging.info("Database initialized successfully.")

def crawl_url(url, visited_urls, depth, max_depth, queue):
    if url in visited_urls or depth > max_depth:
        return

    visited_urls.add(url)

    try:
        logging.info(f"Crawling URL: {url} at depth {depth}")
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract webpage metadata
        title = soup.title.string if soup.title else "Untitled"
        description_meta = soup.find('meta', attrs={'name': 'description'})
        description = description_meta['content'] if description_meta else "No description available."
        content = soup.get_text()

        store_webpage(url, title, description, content)

        # Extract and enqueue links for further crawling
        for link in soup.find_all('a', href=True):
            absolute_url = requests.compat.urljoin(url, link['href'])
            if absolute_url not in visited_urls:
                queue.put((absolute_url, depth + 1))

    except requests.exceptions.RequestException as e:
        logging.error(f"HTTP request failed for {url}: {e}")
    except Exception as e:
        logging.error(f"Unexpected error while crawling {url}: {e}")

def store_webpage(url, title, description, content):
    try:
        logging.info("Storing webpage content in the database.")
        conn = sqlite3.connect('urls.sqlite')
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO webpages (url, title, description, content) VALUES (?, ?, ?, ?)", (url, title, description, content))
        conn.commit()
        conn.close()
        logging.info(f"Stored content for URL: {url}")
    except sqlite3.Error as e:
        logging.error(f"Database error while storing content for {url}: {e}")

def worker(queue, visited_urls, max_depth):
    while not queue.empty():
        url, depth = queue.get()
        crawl_url(url, visited_urls, depth, max_depth, queue)
        queue.task_done()

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        logging.error("Invalid number of arguments. Usage: python3 crawl.py \"url\" [--depth=2]")
        sys.exit(1)

    url = sys.argv[1]
    max_depth = 2  # Default depth

    # Parse optional depth argument
    if len(sys.argv) == 3 and sys.argv[2].startswith('--depth='):
        try:
            max_depth = int(sys.argv[2].split('=')[1])
        except ValueError:
            logging.error("Invalid depth value. It must be an integer.")
            sys.exit(1)

    logging.info("Starting the crawling process. Press Ctrl+C to stop.")
    initialize_database()

    visited_urls = set()
    queue = Queue()
    queue.put((url, 0))

    try:
        threads = []
        for _ in range(4):  # Number of threads
            thread = threading.Thread(target=worker, args=(queue, visited_urls, max_depth))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        logging.info("Crawling stopped by user.")

if __name__ == "__main__":
    main()