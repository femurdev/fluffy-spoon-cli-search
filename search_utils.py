import sqlite3
from datetime import datetime

def create_connection():
    """Establishes a connection to the SQLite database."""
    return sqlite3.connect('urls.sqlite')

def filter_by_date(start_date=None, end_date=None):
    """Filters database entries by a given date range.

    Args:
        start_date (str): The start date in YYYY-MM-DD format.
        end_date (str): The end date in YYYY-MM-DD format.

    Returns:
        list: Filtered results.
    """
    query = "SELECT url, title, description, timestamp FROM urls WHERE 1=1"
    params = []

    if start_date:
        query += " AND timestamp >= ?"
        params.append(start_date)

    if end_date:
        query += " AND timestamp <= ?"
        params.append(end_date)

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        return results

def sort_results(results, order_by="timestamp", descending=True):
    """Sorts results by a specified column.

    Args:
        results (list): The list of results to sort.
        order_by (str): The column name to sort by (default: "timestamp").
        descending (bool): Sort in descending order (default: True).

    Returns:
        list: Sorted results.
    """
    return sorted(results, key=lambda x: x[3] if order_by == "timestamp" else x[1], reverse=descending)

def format_results(results):
    """Formats the search results for display.

    Args:
        results (list): The list of results to format.

    Returns:
        str: Formatted string of results.
    """
    output = []
    for count, (url, title, description, timestamp) in enumerate(results, start=1):
        output.append(f"Result {count}:\nURL: {url}\nTitle: {title}\nDescription: {description}\nTimestamp: {timestamp}\n")
    return "\n".join(output)

# Example usage (can be integrated into cli_search.py or a different script):
if __name__ == "__main__":
    start_date = "2023-01-01"
    end_date = "2023-12-31"
    results = filter_by_date(start_date, end_date)
    sorted_results = sort_results(results)
    print(format_results(sorted_results))