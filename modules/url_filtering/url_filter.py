import logging

def filter_urls(url_list, disallowed_paths=[]):
    """
    Filter out duplicate and disallowed URLs.
    """
    unique_urls = set(url_list)
    filtered_urls = {url for url in unique_urls if not any(url.startswith(dp) for dp in disallowed_paths)}
    
    logging.info(f"Filtered {len(url_list) - len(filtered_urls)} URLs based on rules and duplicates.")
    
    return list(filtered_urls)
