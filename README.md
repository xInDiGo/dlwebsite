# Localized Website and Web Scraping Application

## Overview

This application allows you to download and localize websites for offline use. It's built in Python and offers a range of features including robots.txt checking, URL filtering, and more.

## Features

- Command-line interface for ease of use
- Robots.txt file compliance checking
- Sitemap handling for thorough scraping
- URL filtering to avoid duplicate downloads
- Verbose logging and error handling
- Configuration file for easy customization

## Installation

1. Clone this repository
    ```bash
    git clone https://github.com/yourusername/localized_website_scraper.git
    ```

2. Navigate to the project directory
    ```bash
    cd localized_website_scraper
    ```

3. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the application, execute the following command:

```bash
python main.py [website_url] [output_folder] [-v]

    website_url: The URL of the website you want to download.
    output_folder: The folder where the downloaded website will be stored.
    -v: Enable verbose logging (optional).

For example:
    python main.py http://example.com my_output_folder -v

Configuration
You can customize the application settings by modifying the config/settings.json file.

Contributing
Contributions are welcome! Please read the contributing guidelines.

License
This project is licensed under the MIT License.


Folder Structure

localized_website_scraper/
|-- main.py
|-- config/
|   |-- settings.json
|-- modules/
|   |-- user_input/
|   |   |-- __init__.py
|   |   |-- cli_parser.py
|   |-- robots_txt/
|   |   |-- __init__.py
|   |   |-- robots_checker.py
|   |-- logging_and_error/
|   |   |-- __init__.py
|   |   |-- log_handler.py
|   |-- sitemap/
|   |   |-- __init__.py
|   |   |-- sitemap_parser.py
|   |-- url_filter/
|   |   |-- __init__.py
|   |   |-- url_filter.py
|   |-- downloader/
|   |   |-- __init__.py
|   |   |-- page_downloader.py
|   |-- html_modifier/
|   |   |-- __init__.py
|   |   |-- link_modifier.py
|-- logs/
|   |-- localized_website_scraper.log
|-- tests/
|   |-- test_cli_parser.py
|   |-- test_robots_checker.py
|   |-- test_log_handler.py
|   |-- test_sitemap_parser.py
|   |-- test_url_filter.py
|   |-- test_page_downloader.py
|   |-- test_link_modifier.py
|-- README.md
|-- requirements.txt