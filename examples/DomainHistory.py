import ipfinder

con = ipfinder.config('f67f788f8a02a188ec84502e0dff066ed4413a85') # YOUR_TOKEN_GOES_HERE

# domain name
name = 'google.com';

data = con.getDomainHistory(name)


print(data.all)
