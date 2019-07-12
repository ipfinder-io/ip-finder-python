import ipfinder

con = ipfinder.config('f67f788f8a02a188ec84502e0dff066ed4413a85') # YOUR_TOKEN_GOES_HERE

asn = 'as36947' # as36947

# GET FIREWALL BY AS1
data = con.getFirewall(asn, 'nginx_deny')


print(data.all)
