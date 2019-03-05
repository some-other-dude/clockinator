"""
Clock_utils.py

Utility module for clockinator

"""
import logging
import datetime
import os
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s: %(message)s')
file_handler = logging.FileHandler('logs/clock_utils.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# Clear the log file
my_file = Path("./logs/clock_utils.log")
if my_file.is_file():
    with open("logs/clock_utils.log", "w") as file:
        file.truncate()
    logger.info("Log files cleared.")
