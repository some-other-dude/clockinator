"""
Display.py facilitates the display of the clock for presentation on screenself.

It is a tkinter implementation to show the clock, progress indicators, messages,
and other items on the main display of the RaspberryPi.

"""

import tkinter as tk
import os
import logging
from pathlib import Path


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s: %(message)s')
file_handler = logging.FileHandler('logs/display.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# Clear the log file
my_file = Path("./logs/display.log")
if my_file.is_file():
    with open("logs/display.log", "w") as file:
        file.truncate()
    logger.info("Log files cleared.")


class Display:

    def __init__(self):
        pass
