"""
Clockinator.py

Main module for clockinator
"""

#Python system modules
import sys
import logging
import os
from pathlib import Path
import logging.config
import datetime as dt

# Clockinator modules
#import clock_utils as cu
# from clock_utils import logit
import clock as ck
import dataserver as ds
import display as disp
import netserver as ns

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s: %(message)s')
file_handler = logging.FileHandler('logs/clockinator.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# Clear the log file
my_file = Path("./logs/clockinator.log")
if my_file.is_file():
    with open("logs/clockinator.log", "w") as file:
        file.truncate()

    logger.info("Log files cleared.")

# make a new clock

c1 = ck.Clock(remaining_time = 10)
c1.start()
