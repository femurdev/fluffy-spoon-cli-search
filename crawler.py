import csv
import json

try:
    # Placeholder for crawling logic
    url = 'http://example.com'  # Example URL definition
    data = [
        {
            'url': url,
            'title': 'Example Title',
            'description': 'Example Description',
        }
    ]

    # Export to JSON
    with open('crawled_data.json', 'w') as json_file:
        json.dump(data, json_file)

    # Export to CSV
    with open('crawled_data.csv', 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['url', 'title', 'description'])
        writer.writeheader()
        writer.writerows(data)

    print("Data exported successfully to JSON and CSV.")

except Exception as e:
    print(f"Failed to crawl {url}: {e}")
