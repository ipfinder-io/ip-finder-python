import json
import requests
import urllib.parse

from .info import Info
from .Exception.exceptions import IPfinderException
from .Validation.Asnvalidation import Asnvalidation
from .Validation.Domainvalidation import Domainvalidation
from .Validation.Firewallvalidation import Firewallvalidation
from .Validation.Ipvalidation import Ipvalidation
from .Validation.Tokenvalidation import Tokenvalidation


class Ipfinder:

    # or add proxy pass with your domain
    DEFAULT_BASE_URL = "https://api.ipfinder.io/v1/"

    DEFAULT_API_TOKEN = "free"  # limited to 4,000 requests a day

    FORMATS = 'json'

    STATUS_PATH = 'info'

    RANGES_PATH = 'ranges/'

    FIREWALL_PATH = 'firewall/'

    DOMAIN_PATH = 'domain/'

    DOMAIN_H_PATH = 'domainhistory/'

    DOMAIN_BY_PATH = 'domainby/'

    """docstring for Ipfinder"""

    def __init__(self, token=None, baseUrl=None):

        if token is None:
            self.token = self.DEFAULT_API_TOKEN
        else:
            Tokenvalidation(token)
            self.token = token

        if baseUrl is None:
            self.baseUrl = self.DEFAULT_BASE_URL
        else:
            self.baseUrl = baseUrl

    def call(self, path=None, formats=None):

        if formats is None:
            self.formats = self.FORMATS
        else:
            self.formats = formats

        headers = {
            'Content-type': 'application/json',
            'user-agent': 'IPfinder Python-client'
            #  'X-Authorization' :self.token # test this happy coding
        }
        payload = {
            'token': self.token,
            'format': self.formats
        }

        r = requests.post(
            self.DEFAULT_BASE_URL + path,
            json=payload,
            headers=headers
        )

        status = r.status_code

        if status != 200:

            message = "The HTTP response for get call to the server is not 200."
            raise IPfinderException(
                message, r.status_code, self.DEFAULT_BASE_URL + path, "Error", r.text)

        else:

            if self.formats == 'json':
                return Info(json.loads(r.text))
            else:
                return Info(r.text)

        # return Info(raw_details)


    def Authentication(self):

        return self.call('', '')

        pass

    def getAddressInfo(self, path):

        Ipvalidation(path)
        return self.call(path, None)

        pass

    def getAsn(self, path):

        Asnvalidation(path)
        return self.call(path, None)

        pass

    def getStatus(self):

        return self.call(self.STATUS_PATH, None)

        pass

    def getRanges(self, path):

        return self.call(self.RANGES_PATH + urllib.parse.quote(path))

        pass

    def getFirewall(self, path, formats):

        Firewallvalidation(path, formats)
        return self.call(self.FIREWALL_PATH + path, formats)

        pass

    def getDomain(self, path):

        Domainvalidation(path)
        return self.call(self.DOMAIN_PATH + path)

        pass

    def getDomainHistory(self, path):

        Domainvalidation(path)
        return self.call(self.DOMAIN_H_PATH + path)

        pass

    def getDomainBy(self, path):

        return self.call(self.DOMAIN_BY_PATH + path)

        pass
