# Simple CLI-Based Search Engine

This project implements a simple command-line interface (CLI) search engine that crawls websites and stores their content in a local SQLite database for searching. It does not rely on external search engines.

## Features
- Crawl a webpage and store its text content in a database (`crawl.py`).
- Search for specific terms in the database and return matching URLs and content snippets (`search.py`).

## Requirements
- Python 3
- SQLite
- Required Python packages (install via `pip install -r requirements.txt`):
  - requests
  - beautifulsoup4

## Usage

### Crawling a Website
To crawl a webpage and store its content in the database, use the following command:
```
python3 crawl.py "<URL>"
```
Example:
```
python3 crawl.py "https://example.com"
```

### Searching the Database
To search the database for specific keywords, use the following command:
```
python3 search.py "<search query>"
```
Example:
```
python3 search.py "example keyword"
```

### Database Schema
The database (`urls.sqlite`) contains a single table `webpages` with the following fields:
- `id`: Unique identifier for each entry.
- `url`: The URL of the crawled webpage.
- `content`: The text content of the webpage.

## Limitations
- This tool does not follow links within webpages (no recursive crawling).
- The search is case-insensitive but matches full words only.
- Limited to text content; no support for multimedia or advanced parsing.

## Future Improvements
- Add support for recursive crawling.
- Implement more advanced search features (e.g., fuzzy matching).
- Improve error handling and logging.

## Contributing
Feel free to submit issues or pull requests for improvements or feature suggestions.
## Recursive Crawler Script

### Overview
The `crawl.py` script is a recursive web crawler that scans URLs, retrieves their content, and stores it in a SQLite database. It operates indefinitely until manually stopped, with user-friendly stopping instructions displayed during runtime.

### Features
- **Recursive Crawling**: Automatically extracts and follows links on web pages.
- **Database Storage**: Saves crawled content in a SQLite database to avoid duplicate processing.
- **User Control**: The script can be stopped gracefully using `Ctrl+C`.
- **Error Handling**: Handles HTTP errors, malformed URLs, and database issues gracefully.
- **Edge Case Handling**: Addresses challenges like circular links, duplicate content, and rate-limiting.

### Usage
1. Install the required dependencies using `pip install -r requirements.txt`.
2. Run the script with:
   ```bash
   python3 crawl.py "<starting_url>"
   ```
3. To stop the crawler, press `Ctrl+C`.

### Known Issues
- The script may time out during execution on certain websites.
- Infinite loops can occur if circular links are not fully addressed.

### Planned Improvements
- Add support for configurable crawling depth.
- Implement language-specific crawling and filtering.
- Enhance retry mechanisms for transient errors.

### Example
```bash
python3 crawl.py "https://example.com"
```
## Additional Features and Enhancements

### Multithreaded Crawling
The crawler now supports multithreaded crawling for improved performance. It uses Python's `threading` module to spawn multiple threads, each responsible for processing URLs from a shared queue.

### Depth Control
A new `--depth` argument has been added, allowing users to specify the maximum depth of crawling. The default depth is set to 2. This helps prevent infinite loops or excessively deep crawling.

### Error Handling
- Improved error logging for unreachable URLs and unexpected exceptions.
- Added safeguards to avoid revisiting URLs and exceeding the specified depth.

### Planned Enhancements
- **`robots.txt` Compliance**: Respect crawling restrictions specified in `robots.txt` files.
- **Retry Mechanism**: Implement retries with exponential backoff for transient network errors.
- **Improved Logging**: Include more granular details like response times and skipped URLs.

### Usage
Run the crawler with the following command:
```bash
python3 crawl.py <URL> [--depth=<depth>]
```
Example:
```bash
python3 crawl.py https://example.com --depth=3
```

### Contributing
Contributions are welcome! Please refer to the `CONTRIBUTING.md` file for guidelines.
## Enhancements to Search and Crawl Functionality

### Search Improvements
- **Domain Consolidation**: Group results from subdirectories of the same domain to reduce redundancy.
- **Relevance Filtering**: Implement filtering logic to exclude results with low keyword matching scores.

#### Planned Features:
- Add options to sort results by relevance or freshness.
- Introduce a `--unique-domains` flag to restrict results to unique domains.

### Crawl Enhancements
- **Metadata Enrichment**: Improve the extraction and storage of `title` and `description` fields to reduce empty or placeholder data.
- **URL Normalization**: Ensure all URLs are stored in a normalized format to avoid duplicates.

#### Planned Features:
- Implement `robots.txt` parsing to respect crawling restrictions.
- Add support for language-specific crawling and filtering.

### Edge Cases and Solutions
- **Circular Links**: Prevent infinite loops by maintaining a history of visited URLs.
- **Duplicate Content**: Use hashing to detect and skip duplicate pages.
- **Rate Limiting**: Include delays between requests to avoid overloading servers.

These enhancements aim to make the crawler and search functionalities more robust and user-friendly.