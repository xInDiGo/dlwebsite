from bs4 import BeautifulSoup
import os
import logging

def modify_html(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')
        
        for a_tag in soup.find_all('a'):
            href = a_tag.get('href', '')
            if href.startswith('http'):
                # Convert to relative path (this is a simplified example)
                a_tag['href'] = os.path.basename(href)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        
        logging.info(f"Modified internal links in {file_path}")

    except Exception as e:
        logging.error(f"An error occurred while modifying HTML: {e}")
