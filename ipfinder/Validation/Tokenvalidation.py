import re

from ..Exception.exceptions import IPfinderException


class Tokenvalidation(object):
    """docstring for Tokenvalidation"""

    def __init__(self, token):
        if len(token) <= 25:
            raise IPfinderException('Invalid IPFINDER API Token')
        super(Tokenvalidation, self).__init__()
        self.token = token
