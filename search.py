import sys
import sqlite3

def search_database(query):
    conn = sqlite3.connect('urls.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT url, content FROM webpages WHERE content LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()
    return results

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 search.py \"search query\"")
        sys.exit(1)

    query = sys.argv[1]
    results = search_database(query)

    if results:
        for url, content in results:
            print(f"URL: {url}\nSnippet: {content[:200]}\n")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()