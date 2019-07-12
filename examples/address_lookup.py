import ipfinder


con = ipfinder.config() # YOUR_TOKEN_GOES_HERE || emty token == free


try:
    ip = con.getAddressInfo('1.0.0.0.333')

    print(ip.all)

    # print country_name || pass existe key
    print(ip.country_name)
except Exception as e:
    print('error:', e)
