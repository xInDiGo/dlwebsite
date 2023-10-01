import json
import os
import logging

def load_config(config_path="config/settings.json"):
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
            logging.info(f"Loaded configuration from {config_path}.")

            # Check if there's a Selenium logging level specified in the config
            selenium_logging_level = config.get("selenium_logging_level", "WARNING")
            logging.basicConfig(level=getattr(logging, selenium_logging_level.upper()))  # Set Selenium's logging level

            return config
        except json.JSONDecodeError as e:
            logging.error(f"An error occurred while decoding the JSON configuration file: {e}")
    else:
        logging.warning(f"No configuration file found at {config_path}. Using default settings.")

    return {}