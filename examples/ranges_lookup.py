import ipfinder

con = ipfinder.config('f67f788f8a02a188ec84502e0dff066ed4413a85') # YOUR_TOKEN_GOES_HERE

# Organization name
org = 'Telecom Algeria'

data = con.getRanges(org)

print(data.all)
