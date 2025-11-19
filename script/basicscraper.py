import requests


def basic_scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None


if __name__ == "__main__":
    url = "http://example.com"
    content = basic_scraper(url)
    if content:
        print("Scraped content successfully.")
    else:
        print("Failed to scrape content.")
