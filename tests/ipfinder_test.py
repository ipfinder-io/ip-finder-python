import pytest

from ipfinder.ipfinder import Ipfinder
from ipfinder.info import Info
from ipfinder.Exception.exceptions import IPfinderException
from ipfinder.Validation.Asnvalidation import Asnvalidation
from ipfinder.Validation.Domainvalidation import Domainvalidation
from ipfinder.Validation.Firewallvalidation import Firewallvalidation
from ipfinder.Validation.Ipvalidation import Ipvalidation
from ipfinder.Validation.Tokenvalidation import Tokenvalidation


def test_token():
    token = 'asdasdasdasdasdsdasdasdasdasdasdasdasdasd'
    api = Ipfinder(token)
    assert token == api.token
    pass


def test_freeToken():
    token = 'free'
    api = Ipfinder()
    assert token == api.token
    pass


def test_badToken():
    token = 'a'
    with pytest.raises(Exception) as me:
        # invalid firewall format to raise exception
        assert Ipfinder(token)
        assert me.value.message == 'Invalissd IPFINDER API Token'
    pass



def test_baseUrl():
    url = 'https://api.ipfinder.io/v1/'
    api = Ipfinder.DEFAULT_BASE_URL
    assert url == api
    pass


def test_getStatus():
    path = 'info'
    api = Ipfinder.STATUS_PATH
    assert path == api
    pass


def test_getRanges():

    path = 'ranges/'
    api = Ipfinder.RANGES_PATH
    assert path == api
    pass


def test_getFirewall():
    path = 'firewall/'
    api = Ipfinder.FIREWALL_PATH
    assert path == api
    pass


def test_getDomain():
    path = 'domain/'
    api = Ipfinder.DOMAIN_PATH
    assert path == api
    pass


def test_getDomainHistory():

    path = 'domainhistory/'
    api = Ipfinder.DOMAIN_H_PATH
    assert path == api
    pass


def test_getDomainBy():

    path = 'domainby/'
    api = Ipfinder.DOMAIN_BY_PATH
    assert path == api
    pass


def test_address():

    ip = "1..0.0.0"
    with pytest.raises(Exception) as me:
        # invalid firewall format to raise exception
        assert Ipfinder.getAddressInfo(None,ip)
        assert me.value.message == 'Invalid IPaddress'
    pass


def test_asn():

    asn = "ip"

    """test that exception is raised for invalid firewall format"""
    with pytest.raises(Exception) as me:
        # invalid firewall format to raise exception
        assert Ipfinder.getAsn(None,asn)
        assert me.value.message == 'Invalid asn number'
    pass


def test_domain():

    domain = "fsdf"

    """test that exception is raised for invalid firewall format"""
    with pytest.raises(Exception) as me:
        # invalid firewall format to raise exception
        assert Ipfinder.getDomain(None,domain)
        assert me.value.message == 'Invalid Domain name'
    pass

    pass


def test_firewall_format():

    asn = 'as1'
    forma = 'asdasdasdasdsadasd'
    """test that exception is raised for invalid firewall format"""
    with pytest.raises(Exception) as me:
        # invalid firewall format to raise exception
        assert Ipfinder.getFirewall(None,asn,forma)
        assert me.value.message == 'Invalid Format supported format https://ipfinder.io/docs/?shell#firewall'
    pass


def test_firewall_by():

    country = "DZZ"
    forma = "nginx_allow"

    """test that exception is raised for invalid firewall by"""
    with pytest.raises(Exception) as me:
        # invalid firewall by to raise exception
        assert Ipfinder.getFirewall(None,country,forma)
        assert str(
            me.value.message) == 'Invalid Firewall string please use AS number or ISO 3166-1 alpha-2 country'
    pass
