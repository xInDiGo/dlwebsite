import logging
import datetime

def setup_logging(verbose=False):
    # Generate a timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    # Create a log filename with the timestamp
    log_filename = f"logs/localized_website_scraper_{timestamp}.log"

    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    log_level = logging.DEBUG if verbose else logging.INFO
    
    # Setup basic logging configuration
    logging.basicConfig(filename=log_filename, level=log_level, format=log_format)


if __name__ == "__main__":
    args = type("Args", (object,), {"verbose": True, "url": "http://example.com", "output_folder": "output"})()

    # Setup logging
    setup_logging(args.verbose)

    logging.info(f"Website URL: {args.url}")
    logging.info(f"Output Folder: {args.output_folder}")
    logging.info(f"Verbose Logging: {args.verbose}")
