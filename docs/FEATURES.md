# Features of Simple CLI-Based Search Engine

This document outlines the features implemented in the CLI-based search engine project.

## Core Features

### 1. Crawling Webpages (`crawl.py`)
- **Description**: Fetches the content of a specified URL and stores it in a local SQLite database.
- **Key Details**:
  - Stores the URL and its text content.
  - Implements logging for debugging and monitoring.
  - Automatically initializes the database if it does not exist.

### 2. Searching the Database (`search.py`)
- **Description**: Searches for user-specified keywords in the database and returns matching URLs and content snippets.
- **Key Details**:
  - Uses parameterized SQL queries to prevent SQL injection.
  - Displays the first 200 characters of matching content as a snippet.

## Additional Features

### 1. Logging
- **Description**: Logs events and errors to aid in debugging and monitoring.
- **Key Details**:
  - Configured to log messages with timestamps, severity levels, and descriptions.
  - Supports both `INFO` and `ERROR` log levels.

### 2. Timeout for HTTP Requests
- **Description**: Ensures that the crawler does not hang indefinitely on unresponsive servers.
- **Key Details**:
  - Sets a 10-second timeout for HTTP requests.

## Planned Features

### 1. Recursive Crawling
- **Description**: Extend the crawler to follow links within a webpage and crawl additional pages.
- **Key Details**:
  - Maintain a set of visited URLs to prevent infinite loops.
  - Limit the depth of recursion to avoid excessive resource usage.

### 2. Search Result Ranking
- **Description**: Rank search results based on relevance to the query.
- **Key Details**:
  - Use algorithms like TF-IDF or keyword frequency for ranking.

### 3. Multi-Threaded Crawling
- **Description**: Improve performance by crawling multiple pages concurrently.
- **Key Details**:
  - Use Python's `concurrent.futures` or `threading` library.

### 4. Enhanced Parsing
- **Description**: Improve content extraction by handling special cases like JavaScript-rendered pages.
- **Key Details**:
  - Use libraries like `selenium` for advanced parsing.

### 5. Configurable Settings
- **Description**: Allow users to configure settings like timeout duration and database file path.
- **Key Details**:
  - Use a configuration file (e.g., `config.json`) to store settings.

By implementing these features, the project aims to provide a robust and user-friendly CLI-based search engine.