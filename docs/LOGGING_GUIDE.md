# Logging Guide for Simple CLI-Based Search Engine

This document provides an overview of the logging features added to the `crawl.py` script to aid in debugging and monitoring.

## Purpose of Logging
Logging is essential for:
- Debugging issues during development.
- Monitoring the status of crawling and search operations.
- Identifying and resolving runtime errors.

## Logging Configuration
Logging is configured using the `logging` module in Python. The configuration is as follows:
- **Level**: `INFO`
- **Format**: `%(asctime)s - %(levelname)s - %(message)s`

This configuration ensures that all logs include a timestamp, the severity level, and a descriptive message.

## Log Levels Used
1. **INFO**
   - Used to log successful events, such as starting a crawl or storing content in the database.
   - Example:
     ```
     2023-03-15 10:00:00 - INFO - Crawling URL: https://example.com
     ```

2. **ERROR**
   - Used to log errors, such as failed HTTP requests or database operations.
   - Example:
     ```
     2023-03-15 10:00:05 - ERROR - Failed to crawl https://example.com: Timeout
     ```

## Adding Logs to Your Code
To add a log, use the following syntax:
- For informational messages:
  ```python
  logging.info("Your message here")
  ```
- For error messages:
  ```python
  logging.error("Your error message here")
  ```

## Examples of Logged Events
### Successful Crawl
```
2023-03-15 10:00:00 - INFO - Crawling URL: https://example.com
2023-03-15 10:00:01 - INFO - Successfully crawled and stored content for: https://example.com
```

### Failed Crawl
```
2023-03-15 10:00:00 - INFO - Crawling URL: https://invalid-url
2023-03-15 10:00:01 - ERROR - Failed to crawl https://invalid-url: Invalid URL
```

### Database Error
```
2023-03-15 10:00:02 - ERROR - Database error: UNIQUE constraint failed: webpages.url
```

## Reviewing Logs
Logs are output to the console by default. To redirect logs to a file, modify the logging configuration as follows:
```python
logging.basicConfig(filename='crawler.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
```

## Best Practices
- Always log at appropriate levels (`INFO` for normal operations, `ERROR` for issues).
- Avoid logging sensitive information, such as database credentials or user data.
- Regularly review logs to identify and resolve issues.

By following this guide, you can effectively use logging to debug and monitor the CLI-based search engine.