#!/usr/bin/python
# script to get your public ip
# good module to make api call
import requests
from pprint import pprint

# api call to ifconfig.io and we ask for json response format
response = requests.get("http://ifconfig.io/all.json")

# catching http request error
# 200 mean we got a good response
# != operator is not equal or is not
if response.status_code != 200:
    print ("Error requesting the public ip")
else:
    # we grab the json
    json_response = response.json()
    # we get a dictionary with some of my public ip information
    # let print the output with a module called pprint
    # it will who a pretty print of the output 
    pprint(json_response)
    print("==================================")
    # this dictionary has an key name ip that has your public ip as the value
    # to grab the ip, just use ['ip'] key to access the ip value
    ip = (json_response['ip'])
    # let's print the IP with some format
    print("My Public IP is {}".format(ip))


