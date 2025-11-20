"""Simple web scraper module."""
import requests


def basic_scraper(target_url):
    """
    Scrape content from a given URL.
    
    Args:
        target_url: The URL to scrape content from.
        
    Returns:
        str: The scraped content if successful, None otherwise.
    """
    response = requests.get(target_url, timeout=10)
    if response.status_code == 200:
        return response.text
    return None


if __name__ == "__main__":
    URL = "http://example.com"
    content = basic_scraper(URL)
    if content:
        print("Scraped content successfully.")
    else:
        print("Failed to scrape content.")
