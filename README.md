# CLI Search Engine with SQLite and Web Crawler

This project is a simple command-line interface (CLI) based search engine that allows users to search for URLs and their metadata stored in an SQLite database. The project also includes a web crawler for indexing URLs and their metadata.

## Features

### Core Features
1. **SQLite Database**: Stores URLs, titles, descriptions, and timestamps.
2. **CLI Search Tool**: Allows users to search the database for URLs and their metadata.
3. **Web Crawler**: Fetches URLs, titles, and descriptions from web pages and stores them in the database.
4. **.gitignore**: Excludes the SQLite database from version control.

### Additional Features
- Graceful handling of errors during crawling.
- Prevention of duplicate entries in the database.

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Create the SQLite database schema:
   ```bash
   python crawler.py  # This will also create the database and table if not already present.
   ```

## Usage

### Web Crawler
Run the crawler to index a URL:
```bash
python crawler.py
```
By default, the crawler will fetch `https://example.com`. You can modify `crawler.py` to include other URLs.

### CLI Search Tool
Search for URLs and their metadata:
```bash
python cli_search.py <search-query>
```
Example:
```bash
python cli_search.py example
```

## Project Structure
- `crawler.py`: Script for crawling web pages and saving metadata to the database.
- `cli_search.py`: CLI tool for searching the database.
- `database_schema.sql`: SQLite database schema.
- `.gitignore`: Excludes SQLite database files from version control.

## Future Enhancements
- Add support for exporting data to CSV or JSON.
- Implement advanced search filters (e.g., by timestamp or domain).
- Add a scheduling feature for the crawler.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to contribute by submitting issues or pull requests!