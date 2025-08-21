import sqlite3
import argparse

def create_connection():
    return sqlite3.connect('urls.sqlite')

def search_database(query):
    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT url, title, description FROM urls WHERE url LIKE ? OR title LIKE ? OR description LIKE ?', (f'%{query}%', f'%{query}%', f'%{query}%'))
        results = cursor.fetchall()
        return results

def main():
    parser = argparse.ArgumentParser(description='CLI Search Engine')
    parser.add_argument('query', type=str, help='Search query')
    args = parser.parse_args()

    results = search_database(args.query)
    if results:
        for url, title, description in results:
            print(f"URL: {url}\nTitle: {title}\nDescription: {description}\n")
    else:
        print("No results found.")

if __name__ == '__main__':
    main()