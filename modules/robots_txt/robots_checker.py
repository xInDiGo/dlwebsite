import requests
from urllib.parse import urlparse, urljoin
import logging

def fetch_robots_txt_using_requests(url):
    parsed_url = urlparse(url)
    robots_url = urljoin(url, "/robots.txt")
    
    try:
        response = requests.get(robots_url, timeout=10)
        if response.status_code == 200:
            return response.text
    except requests.RequestException as e:
        logging.error(f"An error occurred while fetching robots.txt from {url}: {e}")

    return None

def can_fetch(url, user_agent="*"):
    robots_txt_content = fetch_robots_txt_using_requests(url)
    if robots_txt_content is None:
        logging.warning(f"No robots.txt found for {url}. Proceeding with scraping.")
        return True
    
    # Simple parsing of robots.txt (for demo; should use a more robust parser)
    lines = robots_txt_content.strip().split("\n")
    disallow_paths = []
    for line in lines:
        if line.startswith("Disallow:"):
            disallow_paths.append(line.split(":")[1].strip())

    parsed_url = urlparse(url)
    return all(parsed_url.path.startswith(dp) == False for dp in disallow_paths)
