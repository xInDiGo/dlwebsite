# main.py
from modules.logging_and_error.script_logging import setup_logging
from modules.config_handling.config_handler import load_config
from modules.robots_txt.robots_checker import can_fetch
from modules.sitemap.sitemap_parser import fetch_sitemap, parse_sitemap
from modules.url_filtering.url_filter import filter_urls
from modules.page_downloading.page_downloader import download_page
from modules.html_modifying.html_modifier import modify_html
import argparse
import logging
import os

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Download and localize a website for offline use.',
        epilog='Example: python main.py http://example.com my_output_folder -v'
    )
    parser.add_argument('url', type=str, help='The URL of the website to download.')
    parser.add_argument('output_folder', type=str, help='The folder where the downloaded website will be stored.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging.')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = parse_arguments()

    # Set up logging
    setup_logging(args.verbose)

    # Load configuration
    config = load_config()

    # Check if the website can be scraped based on its robots.txt
    if can_fetch(args.url):
        logging.info(f"Proceeding to scrape {args.url}.")
        
        # Fetch and parse the sitemap
        sitemap_content = fetch_sitemap(args.url)  # Corrected the variable name here
        if sitemap_content:
            urls_to_scrape = parse_sitemap(sitemap_content)
            logging.info(f"Found {len(urls_to_scrape)} URLs in the sitemap.")
            
            # Filter URLs
            disallowed_paths = []  # You would populate this from robots.txt
            filtered_urls = filter_urls(urls_to_scrape, disallowed_paths)
            logging.info(f"Proceeding with {len(filtered_urls)} filtered URLs.")

            os.makedirs(args.output_folder, exist_ok=True)
            
            # Download and modify pages
            for url in filtered_urls:
                downloaded_file_path = download_page(url, args.output_folder, config)
                if downloaded_file_path:
                    modify_html(downloaded_file_path)
            
        else:
            logging.warning("No sitemap found. Proceeding with alternative scraping methods.")

    else:
        logging.error(f"Scraping not allowed for {args.url} based on robots.txt. Exiting.")
        exit(1)
    
    logging.info(f"Website URL: {args.url}")
    logging.info(f"Output Folder: {args.output_folder}")
    logging.info(f"Verbose Logging: {args.verbose}")
