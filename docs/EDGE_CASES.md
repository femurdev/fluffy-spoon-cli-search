# Edge Cases and How to Handle Them

This document outlines potential edge cases for the CLI-based search engine project and provides suggestions for handling them.

## Edge Cases for `crawl.py`

### 1. Invalid or Malformed URLs
- **Problem**: The script may crash or throw an error when provided with an invalid URL.
- **Solution**: Use a URL validation library like `validators` to check the URL format before making a request.

### 2. Timeout for Unresponsive Servers
- **Problem**: The script may hang indefinitely while waiting for a response from an unresponsive server.
- **Solution**: Set a timeout (e.g., 10 seconds) for HTTP requests using the `requests` library.

### 3. Duplicate Content
- **Problem**: The crawler might store duplicate content if the same URL is crawled multiple times.
- **Solution**: Implement a content hash (e.g., using MD5 or SHA-256) to detect and avoid storing duplicates.

### 4. Large or Binary Files
- **Problem**: Crawling large files or non-HTML content like images and PDFs can cause performance issues.
- **Solution**: Filter out non-HTML content using the `Content-Type` header and set a maximum size limit for responses.

### 5. Unsupported Encodings
- **Problem**: Parsing pages with unsupported or unusual encodings may fail.
- **Solution**: Use libraries like `chardet` to detect and handle encodings properly.

## Edge Cases for `search.py`

### 1. SQL Injection
- **Problem**: Unescaped user input may lead to SQL injection vulnerabilities.
- **Solution**: Always use parameterized queries to handle user input safely.

### 2. Case Sensitivity
- **Problem**: Search results may not match correctly due to case differences.
- **Solution**: Normalize stored content and search queries to lowercase for consistent matching.

### 3. Empty or Broad Queries
- **Problem**: Users may enter empty or overly generic queries, leading to poor performance or irrelevant results.
- **Solution**: Add input validation to reject empty or excessively broad queries.

### 4. Database Locking
- **Problem**: Simultaneous database writes may cause locking issues.
- **Solution**: Use a thread-safe database connection or implement database-level locks.

## General Edge Cases

### 1. Network Errors
- **Problem**: Network issues like DNS failures or connection resets could interrupt crawling.
- **Solution**: Implement retry logic with exponential backoff for transient errors.

### 2. Circular Redirects
- **Problem**: The crawler might enter infinite loops due to circular redirects.
- **Solution**: Detect and limit the number of redirects to avoid infinite loops.

### 3. Recursive Crawling
- **Problem**: If recursive crawling is implemented, it may lead to infinite loops or excessive resource usage.
- **Solution**: Maintain a set of visited URLs and limit the depth of recursion.

### 4. Invalid Database Schema
- **Problem**: If the database schema is corrupted or missing, the scripts may crash.
- **Solution**: Add checks to ensure the database schema is valid and initialize it if necessary.

By addressing these edge cases, the project can become more robust and user-friendly, while maintaining its simplicity.