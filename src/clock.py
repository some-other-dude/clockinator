"""
Clock.py is the Clock class for clockinator

CLOCK STATES
============
stopped - stopped or paused
running - ticking
ended - operator has ended the clock_utils

"""
import sys
import datetime as dt
from pathlib import Path
import logging
import os

import clock_utils


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s: %(message)s')
file_handler = logging.FileHandler('logs/clock.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# Clear the log file
my_file = Path("./logs/clock.log")
if my_file.is_file():
    with open("logs/clock.log", "w") as file:
        file.truncate()
    logger.info("Log files cleared.")


class Clock:

    def __init__(self,
                name = "New Clock",
                total_time = 0,
                remaining_time = 0,
                start_time = None,
                end_time = None,
                current_state = "stopped"):

        self.name = name
        self.total_time = total_time
        self.remaining_time = remaining_time
        self.start_time = start_time
        self.end_time = end_time
        self.current_state = current_state


        logger.info("New clock created. name: %s total: %i remain: %i start: %s end: %s state: %s" %
                    (self.name,
                    self.total_time,
                    self.remaining_time,
                    str(self.start_time),
                    str(self.end_time),
                    self.current_state))

    def start(self):
        self.current_state = "running"
        self.start_time = dt.datetime.now()
        self.end_time = self.start_time + dt.timedelta(seconds=self.remaining_time)
        logger.info("%s clock current_state changed to 'running'" % (self.name))
        logger.info("%s clock start_time changed to %s" % (self.name, self.start_time))
        logger.info("%s clock end_time changed to %s" % (self.name, self.end_time))


    def tick(self):
        """
        Handle the increment of the clock.
        """
        # now = dt.datetime.now()
        # if self.current_state == "running":
        #     if self.
        #     self.remaining_time =
