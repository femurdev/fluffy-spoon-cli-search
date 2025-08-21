import sys
import sqlite3
from argparse import ArgumentParser
from termcolor import colored
from urllib.parse import urlparse
from fuzzywuzzy import fuzz

def search_database(query, limit, offset):
    """Search the database for a query with pagination and relevance ranking."""
    conn = sqlite3.connect('urls.sqlite')
    cursor = conn.cursor()

    # Use Full-Text Search (FTS) if available
    try:
        cursor.execute(
            "SELECT url, title, description, content FROM webpages_fts WHERE content MATCH ?",
            (query,)
        )
        all_results = cursor.fetchall()
    except sqlite3.OperationalError:
        # Fallback to LIKE query if FTS is not setup
        cursor.execute(
            "SELECT url, title, description, content FROM webpages WHERE content LIKE ?",
            (f'%{query}%',)
        )
        all_results = cursor.fetchall()

    # Compute fuzzy matching scores
    scored_results = []
    for url, title, description, content in all_results:
        score = fuzz.partial_ratio(query.lower(), content.lower())
        scored_results.append((score, url, title, description))

    # Sort results by relevance score (descending)
    scored_results.sort(reverse=True, key=lambda x: x[0])

    # Extract main domains and consolidate results
    consolidated_results = {}
    for _, url, title, description in scored_results:
        domain = urlparse(url).netloc
        main_domain = ".".join(domain.split(".")[-2:])  # Extract main domain (e.g., google.com)
        if main_domain not in consolidated_results:
            consolidated_results[main_domain] = []
        consolidated_results[main_domain].append((url, title, description))

    # Flatten consolidated results with a limit and offset for pagination
    flat_results = [item for domain, items in consolidated_results.items() for item in items]
    paginated_results = flat_results[offset:offset + limit]

    conn.close()
    return paginated_results

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