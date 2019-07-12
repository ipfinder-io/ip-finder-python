import re

from ..Exception.exceptions import IPfinderException


class Asnvalidation:
    """docstring for Asnvalidation"""

    def __init__(self, asn):
        if not re.match("^(as|AS)(\d+)$", asn):
            raise IPfinderException('Invalid asn number')

        super(Asnvalidation, self).__init__()
        self.asn = asn
