<img src='https://camo.githubusercontent.com/46886c3e689a0d4a3f6c0733d1cab5d9f9a3926d/68747470733a2f2f697066696e6465722e696f2f6173736574732f696d616765732f6c6f676f732f6c6f676f2e706e67' height='60' alt='IP Finder'></a>
#  IPFinder Python Client Library

The official Python client library for the [IPFinder.io](https://ipfinder.io) get details for :
-  IP address details (city, region, country, postal code, latitude and more ..)
-  ASN details (Organization name, registry,domain,comany_type, and more .. )
-  Firewall by supported formats details (apache_allow,  nginx_deny, CIDR , and more ..)
-  IP Address Ranges by the Organization name  details (list_asn, list_prefixes , and more ..)
-  service status details (queriesPerDay, queriesLeft, key_type, key_info)
- Get Domain IP (asn, organization,country_code ....)
- Get Domain IP history (total_ip, list_ip,organization,asn ....)
- Get list Domain By ASN, Country,Ranges (select_by , total_domain  , list_domain ....)


## Getting Started
singup for a free account at [https://ipfinder.io/auth/signup](https://ipfinder.io/auth/signup), for Free IPFinder API access token.

The free plan is limited to 4,000 requests a day, and doesn't include some of the data fields
To enable all the data fields and additional request volumes see [https://ipfinder.io/pricing](https://ipfinder.io/pricing).

## Documentation

See the [official documentation](https://ipfinder.io/docs).

## Installation
Installing using pip:
```shell
pip install ipfinder
```

## How to Use
usage is quite simple:

## With `free` TOKEN

```python

import ipfinder

config = ipfinder.config() #  emty token == free

# lookup your IP address information
auth = con.Authentication()

auth.details
```

### Authentication

```python

import ipfinder

config = ipfinder.config('YOUR_TOKEN_GOES_HERE')

# lookup your IP address information
auth = con.Authentication()

auth.details
```

### Get IP address

```python
import ipfinder

config = ipfinder.config('YOUR_TOKEN_GOES_HERE')

# GET Get details for 1.0.0.0

ip = con.getAddressInfo('1.0.0.0')

ip.details

# lookup IP address information

```

### Get ASN
This API available as part of our Pro and enterprise [https://ipfinder.io/pricing](https://ipfinder.io/pricing).

```python
import ipfinder

config = ipfinder.config('YOUR_TOKEN_GOES_HERE')

# lookup Asn information
asn = con.getAsn('AS1')

asn.details
```

### Firewall
This API available as part of our  enterprise [https://ipfinder.io/pricing](https://ipfinder.io/pricing).
formats supported are :  `apache_allow`, `apache_deny`,`nginx_allow`,`nginx_deny`, `CIDR`, `linux_iptables`, `netmask`, `inverse_netmask`, `web_config_allow `, `web_config_deny`, `cisco_acl`, `peer_guardian_2`, `network_object`, `cisco_bit_bucket`, `juniper_junos`, `microtik`

```python
import ipfinder

config = ipfinder.config('YOUR_TOKEN_GOES_HERE')

asn = 'as36947';

# lookup Asn information

data = con.getFirewall(asn, 'nginx_deny')

data.details

```

### Get IP Address Ranges
This API available as part of our  enterprise [https://ipfinder.io/pricing](https://ipfinder.io/pricing).


```python
import ipfinder

config = ipfinder.config('YOUR_TOKEN_GOES_HERE')

# Organization name
org = 'Telecom Algeria';

# lookup Organization information
data = con.getRanges(org)

data.details



```

### Get service status

```python
import ipfinder

config = ipfinder.config('YOUR_TOKEN_GOES_HERE')

# lookup TOKEN information
data = con.getStatus()


data.details


```

### Get Domain IP


```python
import ipfinder

config = ipfinder.config('YOUR_TOKEN_GOES_HERE')


#  domain name
name = 'google.com';

data = con.getDomain(name)

data.details

```

### Get Domain IP history



```python
import ipfinder

config = ipfinder.config('YOUR_TOKEN_GOES_HERE')

# domain name
name = 'google.com';

data = con.getDomainHistory(name)

data.details


```

### Get list Domain By ASN, Country,Ranges


```python
import ipfinder

config = ipfinder.config('YOUR_TOKEN_GOES_HERE')

# list live domain by country DZ,US,TN,FR,MA
by = 'DZ';

dby = con.getDomainBy(by)

dby.details


```

### Add proxy
```python
import ipfinder

config = ipfinder.config('YOUR_TOKEN_GOES_HERE','https://ipfinder.yourdomain.com')
```

### Error handling

```python
import ipfinder
try:
    # do something
except Exception as e:
    print('error: ', e)


```

Sample codes under **examples/** folder.


## Contact

Contact Us With Additional Questions About Our API, if you would like more information about our API that isn’t available in our IP geolocation API developer documentation, simply [contact](https://ipfinder.io/contact) us at any time and we’ll be able to help you find what you need.

## License

----
[![GitHub license](https://img.shields.io/github/license/ipfinder-io/ip-finder-python.svg)](https://github.com/ipfinder-io/ip-finder-python)
