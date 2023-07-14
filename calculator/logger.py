# logger.py

import logging

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create console handler and set level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add formatter to the console handler
console_handler.setFormatter(formatter)

# Add console handler to the logger
logger.addHandler(console_handler)
