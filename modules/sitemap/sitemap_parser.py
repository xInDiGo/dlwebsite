import requests
import xml.etree.ElementTree as ET
import logging

def fetch_sitemap(url):
    sitemap_url = url if url.endswith('.xml') else f"{url}/sitemap.xml"
    logging.debug(f"Fetching sitemap from: {sitemap_url}")  # Debugging line
    try:
        response = requests.get(sitemap_url)
        if response.status_code == 200:
            logging.debug("Successfully fetched sitemap.")  # Debugging line
            return response.content
        else:
            logging.warning(f"Received status code {response.status_code} while fetching sitemap.")  # Debugging line
    except requests.RequestException as e:
        logging.error(f"An error occurred while fetching the sitemap: {e}")

    return None


def parse_sitemap(sitemap_content):
    logging.debug("Parsing sitemap content.")  # Debugging line
    
    # Create an XML ElementTree object
    root = ET.fromstring(sitemap_content)
    
    # Define XML namespaces
    namespaces = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    # List to store all URLs to scrape
    urls_to_scrape = []
    
    # Check if this sitemap contains other sitemaps
    for sitemap_tag in root.findall('sm:sitemap', namespaces=namespaces):
        nested_sitemap_url = sitemap_tag.find('sm:loc', namespaces=namespaces).text
        logging.info(f"Found nested sitemap: {nested_sitemap_url}")  # Debugging line
        nested_sitemap_content = fetch_sitemap(nested_sitemap_url)
        if nested_sitemap_content:
            logging.debug("Parsing nested sitemap.")  # Debugging line
            urls_to_scrape.extend(parse_sitemap(nested_sitemap_content))
    
    # Extract URLs from this sitemap
    for url_tag in root.findall('sm:url', namespaces=namespaces):
        url = url_tag.find('sm:loc', namespaces=namespaces).text
        logging.info(f"Found URL in sitemap: {url}")  # Debugging line
        urls_to_scrape.append(url)

    logging.debug(f"Total URLs found: {len(urls_to_scrape)}")  # Debugging line

    return urls_to_scrape

if __name__ == "__main__":
    # This is for testing purposes
    sitemap_content = fetch_sitemap("http://example.com")
    if sitemap_content:
        urls = parse_sitemap(sitemap_content)
        print(urls)
