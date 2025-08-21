import argparse
import requests
import sqlite3
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import time
import logging
import validators
import hashlib
from logging.handlers import RotatingFileHandler

# Initialize colorama
init(autoreset=True)

# Setup logging with rotation
handler = RotatingFileHandler('crawler.log', maxBytes=5000000, backupCount=5)
logging.basicConfig(handlers=[handler], level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def migrate_database(old_db_name, new_db_name):
    """Migrate data to a new database schema."""
    conn_old = sqlite3.connect(old_db_name)
    cursor_old = conn_old.cursor()

    conn_new = sqlite3.connect(new_db_name)
    cursor_new = conn_new.cursor()

    # Create new table with updated schema
    cursor_new.execute('''CREATE TABLE IF NOT EXISTS crawled_data (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            url TEXT UNIQUE,
                            title TEXT,
                            description TEXT,
                            content_hash TEXT UNIQUE
                         )''')

    # Migrate data from old table to new table
    cursor_old.execute('SELECT id, url, title, description FROM crawled_data')
    for row in cursor_old.fetchall():
        url, title, description = row[1], row[2], row[3]
        content_hash = hashlib.sha256((title + description).encode('utf-8')).hexdigest()
        try:
            cursor_new.execute('INSERT INTO crawled_data (url, title, description, content_hash) VALUES (?, ?, ?, ?)', 
                               (url, title, description, content_hash))
            conn_new.commit()
        except sqlite3.IntegrityError:
            logging.warning(f"Duplicate entry skipped during migration: {url}")

    conn_old.close()
    conn_new.close()
    logging.info("Database migration completed successfully.")

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS crawled_data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        url TEXT UNIQUE,
                        title TEXT,
                        description TEXT,
                        content_hash TEXT UNIQUE
                     )''')
    cursor.execute('''CREATE INDEX IF NOT EXISTS idx_content_hash ON crawled_data (content_hash)''')
    conn.commit()
    conn.close()

def save_to_database(db_name, url, title, description, content_hash):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO crawled_data (url, title, description, content_hash) VALUES (?, ?, ?, ?)', 
                       (url, title, description, content_hash))
        conn.commit()
    except sqlite3.IntegrityError:
        print(Fore.YELLOW + f"[Warning] Duplicate content or URL already exists in the database: {url}")
        logging.warning(f"Duplicate content or URL already exists in the database: {url}")
    finally:
        conn.close()

def crawl_url(url):
    if not validators.url(url):
        print(Fore.RED + f"[Error] Invalid URL: {url}")
        logging.error(f"Invalid URL: {url}")
        return None, None, None

    try:
        response = requests.get(url, timeout=5)

        if 'text/html' not in response.headers.get('Content-Type', ''):
            print(Fore.YELLOW + f"[Warning] Non-HTML content at {url}")
            logging.warning(f"Non-HTML content at {url}")
            return None, None, None

        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string if soup.title else 'No Title'
        description_tag = soup.find('meta', attrs={'name': 'description'})
        description = description_tag['content'] if description_tag else 'No Description'
        content_hash = hashlib.sha256(response.text.encode('utf-8')).hexdigest()

        print(Fore.GREEN + f"[Success] Crawled: {url}")
        logging.info(f"Successfully crawled: {url}")
        return title, description, content_hash
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[Error] Failed to crawl {url}: {e}")
        logging.error(f"Failed to crawl {url}: {e}")
        return None, None, None

def main():
    parser = argparse.ArgumentParser(description="A simple web crawler using requests and SQLite.")
    parser.add_argument('urls', metavar='U', type=str, nargs='+', help='List of URLs to crawl')
    parser.add_argument('--db', type=str, default='crawler.db', help='SQLite database file (default: crawler.db)')
    parser.add_argument('--delay', type=float, default=1.0, help='Delay between requests in seconds (default: 1.0)')
    parser.add_argument('--migrate', type=str, help='Migrate an old database to a new schema')

    args = parser.parse_args()

    if args.migrate:
        migrate_database(args.migrate, args.db)
    else:
        create_database(args.db)

        for url in args.urls:
            title, description, content_hash = crawl_url(url)
            if title and description and content_hash:
                save_to_database(args.db, url, title, description, content_hash)
            time.sleep(args.delay)

    print(Fore.CYAN + Style.BRIGHT + "Crawling completed!")
    logging.info("Crawling completed!")

if __name__ == '__main__':
    main()