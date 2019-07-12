import re

from ..Exception.exceptions import IPfinderException


class Domainvalidation:
    """docstring for Domainvalidation"""

    def __init__(self, domain):
        if not re.match("^(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z\d]{1,63}$", domain):
            raise IPfinderException('Invalid asn number')
        super(Domainvalidation, self).__init__()
        self.domain = domain
