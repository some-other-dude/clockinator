"""
Dataserver.py is the data services module for clockinatorself.

It will handle the local database interface, data import and export.

"""
import os
import logging
from pathlib import Path

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s: %(message)s')
file_handler = logging.FileHandler('logs/dataserver.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# Clear the log file
my_file = Path("./logs/dataserver.log")
if my_file.is_file():
    with open("logs/dataserver.log", "w") as file:
        file.truncate()
    logger.info("Log files cleared.")

class Dataserver:

    def ___init___(self):
        pass

    def import_csv(self, payload):
        pass

    def export_csv(self, payload):
        pass

    def log_it(self, payload):
        """
        Payload should be a dict containing:
        "Type" - type of event
            debug - debugging info
            info -
            notice -
            warn -
            err -
            crit -
            emerg -
        "Module" - the module logging the event
        "Function" - the function logging the event

        """
