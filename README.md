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