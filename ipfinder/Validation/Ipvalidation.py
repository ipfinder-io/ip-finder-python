import re

from ..Exception.exceptions import IPfinderException


class Ipvalidation:
    """docstring for Ipvalidation"""

    def __init__(self, ip):
        if not re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", ip):
            raise IPfinderException('Invalid IPaddress')
        super(Ipvalidation, self).__init__()
        self.ip = ip
