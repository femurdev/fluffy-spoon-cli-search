# CLI Search Engine with SQLite and Web Crawler

## Overview
This project consists of a command-line interface (CLI) search engine and a web crawler. The system uses SQLite to store URLs, titles, and descriptions of web pages, which are indexed by the crawler. The search engine allows users to query the database for stored content.

## Features
### Crawler (`crawler.py`)
- Recursively crawls web pages starting from a given URL.
- Extracts and stores URLs, titles, and meta descriptions in an SQLite database.
- Supports depth-based crawling with the `--depth` argument.
- Includes a `--delay` option to set a delay between requests and avoid overloading servers.
- Avoids revisiting already-crawled URLs.

#### Planned Features for Crawler
- **Dynamic Content Handling**: Use headless browsers (e.g., Selenium) to handle JavaScript-rendered content.
- **Export Options**: Allow exporting crawled data in JSON and CSV formats.
- **Rate Limiting**: Implement domain-specific rate limits for polite crawling.
- **Error Retry Mechanisms**: Enhance retry logic with exponential backoff.

### Search Engine (`cli_search.py`)
- Queries the SQLite database for URLs, titles, or descriptions matching a user-provided search term.
- Outputs search results in a readable format.
- **Added Feature:** Color-coded output for better readability using the `termcolor` library. Success messages are displayed in green, and errors or warnings are displayed in red.
- **New Validation:** Handles empty or invalid search queries gracefully.
- **Planned Filters:** Add advanced search filters such as keyword exclusion and domain-specific filtering.

### `.gitignore`
- Excludes sensitive and unnecessary files, such as SQLite database files (`*.sqlite`), Python bytecode, and log files.

## Requirements
- Python 3.6+
- `requests`
- `beautifulsoup4`
- `termcolor`

Install the required packages using the following command:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Crawler
To crawl a website, run the following command:
```bash
python crawler.py <url> [--depth DEPTH] [--delay DELAY]
```
- `<url>`: The starting URL for the crawl.
- `--depth DEPTH`: (Optional) Depth for recursive crawling (default: 1).
- `--delay DELAY`: (Optional) Delay between requests in seconds (default: 1).

Example:
```bash
python crawler.py https://example.com --depth 2 --delay 2
```

### Using the Search Engine
To search the database, run:
```bash
python cli_search.py <query>
```
- `<query>`: The search term for querying URLs, titles, or descriptions. Use "all" to display all stored records.

Optional arguments:
- `--start-date`: Filter results from this date (YYYY-MM-DD).
- `--end-date`: Filter results until this date (YYYY-MM-DD).
- `--sort-by`: Column to sort by (`timestamp` or `title`).
- `--ascending`: Sort results in ascending order (default: descending).
- `--limit`: Limit the number of results displayed (default: 10).

Example:
```bash
python cli_search.py example --start-date 2023-01-01 --end-date 2023-12-31 --limit 5
```

### Color-Coded Output
The CLI search engine includes color-coded output:
- **Green**: Success messages, such as the number of results found.
- **Red**: Errors or warnings, such as "No results found." or invalid query inputs.

## Edge Case Handling
1. **Empty Search Queries**:
   - The system validates query inputs and exits gracefully if the query is empty.

2. **Invalid Dates**:
   - Ensures that date filters follow the YYYY-MM-DD format. Provides an error message for invalid formats.

3. **Large Queries**:
   - Limits the number of displayed results with the `--limit` argument to prevent overwhelming output.

4. **Corrupted Database**:
   - Catches SQLite errors and provides instructions for recovery.

5. **Unreachable Websites**:
   - Implements retries and backoff mechanisms in the crawler to handle slow or unreachable websites.

## Debugging Instructions
1. **Crawler**:
   - Use verbose logging by modifying the logging level in `crawler.py`.
   - Ensure robots.txt compliance by verifying with the `RobotsHandler` class.
   - Add breakpoints for debugging logic related to dynamic content handling.

2. **Search Engine**:
   - Verify database connectivity using SQLite CLI tools.
   - Use test queries like `all` to ensure the database is populated.

## File Structure
- `crawler.py`: Contains the web crawler implementation.
- `cli_search.py`: Implements the CLI search engine.
- `urls.sqlite`: SQLite database for storing crawled data (excluded from version control).
- `.gitignore`: Specifies files and directories to exclude from version control.
- `requirements.txt`: Lists required Python packages.
- `README.md`: Documentation for the project.

## Future Improvements
1. **Dynamic Content Handling**:
   - Support for JavaScript-rendered content using tools like Selenium.
2. **Database Management**:
   - Command-line options to prune or archive old entries.
3. **Advanced Search**:
   - Add filters for date ranges or specific domains.
4. **Improved Error Handling**:
   - Retry logic for failed requests.
5. **Real-Time Monitoring**:
   - Build a dashboard to monitor crawling progress and stats.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

---

Happy crawling and searching!