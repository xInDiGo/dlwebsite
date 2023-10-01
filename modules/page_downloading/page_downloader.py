import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from urllib.parse import urlparse
import logging
import time

def download_page(url, output_folder, config):
    try:
        # Set up ChromeDriver
        chrome_driver_path = 'C:\\Users\\Eric\\Desktop\\AIBrowser\\chromedriver\\chromedriver-win64\\chromedriver.exe'
        chrome_exe_path = 'C:\\Users\\Eric\\Desktop\\AIBrowser\\chrome\\chrome-win64\\chrome.exe'
        chrome_service = Service(chrome_driver_path)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = chrome_exe_path


        # Apply Chrome options from configuration
        selenium_logging_level = config.get("selenium_logging_level", "WARNING")
        chrome_options.add_argument(f"--log-level={selenium_logging_level}")
        for option in config.get("chrome_options", []):
            chrome_options.add_argument(option)

        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        
        # Open the URL
        driver.get(url)

        # Wait for JavaScript to load (adjust this time as needed)
        time.sleep(5)
        
        # Get the page's HTML content
        page_source = driver.page_source

        # Close the browser
        driver.quit()

        # Parse URL to generate a file name
        parsed_url = urlparse(url)
        file_name = os.path.basename(parsed_url.path)
        if not file_name:
            file_name = "index.html"
        elif not os.path.splitext(file_name)[1]:
            # If the file_name has no extension, add ".html"
            file_name += ".html"

        # Generate output path and save HTML
        output_path = os.path.join(output_folder, file_name)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page_source)
        
        logging.info(f"Downloaded {url} to {output_path}")
        return output_path

    except Exception as e:
        logging.error(f"An error occurred while downloading {url}: {e}")

    return None
