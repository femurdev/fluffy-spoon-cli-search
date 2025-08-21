# Extended Documentation for CLI-Based Search Engine

This document provides additional details and best practices for using and extending the CLI-based search engine.

## Best Practices for Crawling

### 1. Validate URLs Before Crawling
- Always ensure that the URL is well-formed and includes the scheme (e.g., `http://` or `https://`).
- Use a validation tool or library to catch malformed URLs early.

### 2. Avoid Overloading Servers
- Add a delay between consecutive requests to the same domain to avoid being flagged as a bot.
- Use polite crawling techniques and respect the `robots.txt` file.

### 3. Monitor Logs
- Regularly review logs to identify issues such as failed requests or skipped pages.
- Redirect logs to a file for long-running crawling sessions.

### 4. Handle Large Datasets
- If crawling a large number of pages, periodically back up the database to avoid data loss.
- Consider splitting the database into smaller chunks for easier management.

## Advanced Search Features

### 1. Use Specific Queries
- Use precise keywords to narrow down search results.
- Avoid overly generic terms to improve relevance.

### 2. Combine Scripts for Batch Searches
- Write a wrapper script to automate multiple searches based on a list of queries.
- Store the results in a separate file for analysis.

### 3. Optimize Database Performance
- Add indexes to frequently queried columns, such as `content` and `url`.
- Periodically vacuum the database to reclaim unused space.

## Extending the Project

### 1. Adding New Features
- Use the modular structure of the scripts to add new functionality without breaking existing features.
- Follow the code style guidelines outlined in `CONTRIBUTING.md`.

### 2. Supporting Additional Formats
- Extend the crawler to process non-HTML content, such as PDFs or JSON APIs.
- Use libraries like PyPDF2 for parsing PDFs or `requests` for handling APIs.

### 3. Scaling the System
- Implement multi-threaded crawling to process multiple URLs simultaneously.
- Consider moving to a distributed database like PostgreSQL for better scalability.

## Troubleshooting Tips

### 1. Debugging Logs
- Enable debug-level logs for detailed information during development.
- Use tools like `grep` to filter logs for specific keywords or errors.

### 2. Resolving Database Issues
- Run integrity checks on the SQLite database using the following command:
```
sqlite3 urls.sqlite "PRAGMA integrity_check;"
```
- If corruption is detected, restore the database from a backup.

### 3. Handling Network Errors
- Use retry logic for transient errors like timeouts or rate limits.
- Switch to a proxy server if your IP is blocked by the target website.

By following these best practices and tips, you can make the most out of the CLI-based search engine and extend its capabilities to suit your needs.