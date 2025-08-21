# Frequently Asked Questions (FAQ)

## General Questions

### 1. What is this project about?
This project implements a simple CLI-based search engine. It includes two main components:
- `crawl.py`: Crawls webpages and stores their content in a local SQLite database.
- `search.py`: Searches the database for specific terms and returns matching URLs and content snippets.

### 2. How do I install dependencies?
Install the required Python packages using the following command:
```
pip install -r requirements.txt
```

### 3. Where is the data stored?
The data is stored in an SQLite database named `urls.sqlite` in the project directory.

## Crawling Questions

### 4. How do I crawl a webpage?
Use the following command to crawl a webpage:
```
python3 crawl.py "<URL>"
```
Example:
```
python3 crawl.py "https://example.com"
```

### 5. What happens if a webpage is already crawled?
The crawler will skip URLs that are already in the database, ensuring no duplicate entries.

### 6. Can I crawl multiple webpages at once?
Currently, the crawler processes one URL at a time. Multi-threaded crawling is planned as a future feature.

### 7. What if the webpage takes too long to load?
The crawler has a timeout of 10 seconds for HTTP requests. If the webpage does not respond within this time, it will be skipped.

### 8. Does the crawler support JavaScript-rendered pages?
No, the crawler only processes static HTML content. Support for JavaScript-rendered pages may be added in the future using tools like Selenium.

## Search Questions

### 9. How do I search the database?
Use the following command to search the database:
```
python3 search.py "<search query>"
```
Example:
```
python3 search.py "example keyword"
```

### 10. What if no results are found?
If no results match the query, the script will display a message indicating that no results were found.

### 11. Can I filter search results by language?
Language-specific filtering is not yet implemented but is planned as a future feature.

## Troubleshooting

### 12. Why is the crawler not working?
Check the following:
- Ensure the URL is valid and includes the scheme (e.g., `http://` or `https://`).
- Verify your internet connection.
- Check the logs for error messages.

### 13. Why is the database empty after crawling?
Possible reasons:
- The webpage had no content to store.
- The URL was already crawled.
- There was an error during the crawling process (check the logs).

### 14. How do I view logs?
Logs are displayed in the console by default. To redirect logs to a file, modify the logging configuration in `crawl.py`.

### 15. What should I do if the search is slow?
If the database is large, search performance may degrade. Consider adding an index to the `content` column in the database to optimize search queries.

If your question is not listed here, feel free to submit an issue or reach out for support.