"""
Netserver is the network communications module for Clockinator.

Netserver provides all network communications functions including web server,
TCP listeners/responders, calls to NTP servers, etc.
"""
import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s: %(message)s')
file_handler = logging.FileHandler('logs/netserver.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# Clear the log file
my_file = Path("./logs/netserver.log")
if my_file.is_file():
    with open("logs/netserver.log", "w") as file:
        file.truncate()
    logger.info("Log files cleared.")


class Netserver:

    def __init___(self):
        pass
