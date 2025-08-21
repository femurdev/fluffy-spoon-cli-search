import argparse
from search_utils import filter_by_date, sort_results
from termcolor import colored

def format_results(results):
    """Formats and color-codes the search results for display."""
    output = []
    for count, (url, title, description, timestamp) in enumerate(results, start=1):
        output.append(
            f"{colored(f'Result {count}:', 'yellow')}\n"
            f"{colored('URL:', 'blue')} {colored(url, 'cyan')}\n"
            f"{colored('Title:', 'blue')} {colored(title, 'green')}\n"
            f"{colored('Description:', 'blue')} {colored(description, 'white')}\n"
            f"{colored('Timestamp:', 'blue')} {colored(timestamp, 'magenta')}\n"
        )
    return "\n".join(output)

def validate_query(query):
    """Validates the search query."""
    if not query or query.strip() == "":
        print(colored("Error: Search query cannot be empty.", 'red'))
        exit(1)

def main():
    """Main function to parse arguments and perform the search."""
    parser = argparse.ArgumentParser(description='CLI Search Engine with Advanced Features')
    parser.add_argument('query', type=str, help='Search query (use "all" to return all results)')
    parser.add_argument('--start-date', type=str, help='Filter results from this date (YYYY-MM-DD)')
    parser.add_argument('--end-date', type=str, help='Filter results until this date (YYYY-MM-DD)')
    parser.add_argument('--sort-by', type=str, default='timestamp', choices=['timestamp', 'title'], help='Column to sort by (default: timestamp)')
    parser.add_argument('--ascending', action='store_true', help='Sort results in ascending order (default: descending)')
    parser.add_argument('--limit', type=int, default=10, help='Limit the number of results displayed')

    args = parser.parse_args()

    # Validate the query
    validate_query(args.query)

    # Filter by date range
    results = filter_by_date(args.start_date, args.end_date)

    # If a query is provided, filter results that match the query
    if args.query != "all":
        results = [result for result in results if args.query.lower() in result[0].lower() or
                   args.query.lower() in result[1].lower() or
                   args.query.lower() in result[2].lower()]

    # Sort results
    results = sort_results(results, order_by=args.sort_by, descending=not args.ascending)

    # Limit results
    results = results[:args.limit]

    # Display results
    if results:
        print(colored(f"\nFound {len(results)} result(s). Showing up to {args.limit} result(s):\n", 'green'))
        print(format_results(results))
    else:
        print(colored("No results found.", 'red'))

if __name__ == '__main__':
    main()