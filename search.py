import sys
import sqlite3
from argparse import ArgumentParser
from termcolor import colored

def search_database(query, limit, offset):
    """Search the database for a query with pagination."""
    conn = sqlite3.connect('urls.sqlite')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT url, title, description FROM webpages WHERE content LIKE ? LIMIT ? OFFSET ?",
        (f'%{query}%', limit, offset),
    )
    results = cursor.fetchall()
    conn.close()
    return results

def display_results(results):
    """Display search results with color-coded output."""
    for url, title, description in results:
        print(colored(f"URL: {url}", "blue"))
        print(colored(f"Title: {title}", "green"))
        print(colored(f"Description: {description[:200]}\n", "yellow"))

def main():
    """Main function to parse arguments and perform the search."""
    parser = ArgumentParser(description="Search the database for a query.")
    parser.add_argument("query", type=str, help="Search query")
    parser.add_argument("--page", type=int, default=1, help="Page number (default: 1)")
    parser.add_argument(
        "--results", type=int, default=10, help="Number of results per page (default: 10)"
    )

    args = parser.parse_args()

    # Calculate limit and offset for pagination
    limit = args.results
    offset = (args.page - 1) * args.results

    # Perform the search
    results = search_database(args.query, limit, offset)

    if results:
        display_results(results)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()