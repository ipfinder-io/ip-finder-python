import ipfinder
from ipfinder.ipfinder import Ipfinder


def test_get_config():
    config = ipfinder.config()
    assert isinstance(config, Ipfinder)
