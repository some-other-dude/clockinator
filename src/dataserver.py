"""
Dataserver.py is the data services module for clockinatorself.

It will handle the local database interface, data import and export.

"""

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
