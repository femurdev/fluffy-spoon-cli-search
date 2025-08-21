# Simple Web Crawler

This is a Python-based web crawler that uses `requests`, `sqlite3`, and `BeautifulSoup` to fetch and store webpage metadata. The crawler is designed to handle edge cases like invalid URLs, non-HTML content, and duplicate entries. It features robust logging and colored console output for better readability.

## Features
- **Crawl Web Pages**: Extract titles, meta descriptions, and content hashes.
- **SQLite Database**: Store crawled data in a database with indexing for performance.
- **Duplicate Detection**: Detect and avoid duplicate content using content hashing.
- **Schema Migration**: Automatically migrate database schema to handle updates seamlessly.
- **Robust Logging**: Log successes, warnings, and errors, with log rotation support.
- **Configurable Delay**: Set delay between requests to respect server rate limits.

## Requirements
- Python 3.x
- `requests`
- `sqlite3`
- `beautifulsoup4`
- `colorama`
- `validators`

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the crawler with a list of URLs:
```bash
python3 simple_crawler.py <list_of_urls> --db <database_name> --delay <delay_in_seconds>
```

**Example:**
```bash
python3 simple_crawler.py https://www.example.com https://www.python.org --db crawler.db --delay 1.0
```

### Command-Line Arguments
- `urls`: List of URLs to crawl.
- `--db`: SQLite database file (default: `crawler.db`).
- `--delay`: Delay between requests in seconds (default: `1.0`).

## Database Schema
The crawler uses an SQLite database to store data with the following schema:
- `id`: Auto-incrementing primary key.
- `url`: The URL of the webpage (unique).
- `title`: The title of the webpage.
- `description`: The meta description of the webpage.
- `content_hash`: SHA-256 hash of the page content (unique).

### Schema Management
The script includes automatic schema migration to ensure compatibility. If the schema needs to be updated (e.g., adding new columns), the script will migrate the database without data loss.

## Log File
Logs are saved to `crawler.log` with rotation enabled to prevent excessive growth. The log file captures:
- Successfully crawled URLs
- Warnings for duplicate content or non-HTML resources
- Errors for invalid or unreachable URLs

## Notes
- Ensure the URLs are valid and reachable.
- The script avoids inserting duplicate entries based on URL and content hash.
- For JavaScript-heavy sites, consider extending the script with a headless browser.

## License
This project is licensed under the MIT License.