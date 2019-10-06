#!/usr/bin/python
# Dictionaries are list of unordered pairs of keys and values
# here is a simple demo
# creating dictionary
# we have vlans numbers as the key and the vlan name as the value
vlan = {"10":"data", "20": "voice", "30":"security"}

# access a dictionary objects
# you always access the value using the key
print (vlan["10"])
"data"

# to add an item you have to pass a value with a key
vlan["40"] = "secret"

# Some of dictionaries methods
# TIP to see all the object method you can use the dir function
print (dir(vlan))
['clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']

# you see the  method get, this method is to access the value
print (vlan.get("20"))
"voice"
# the values method will return a list of values
print (vlan.values())
['data', 'security', 'voice', 'secret']

# updating the vlan dictionary
vlan["40"] = "notSecret"
print (vlan.values())
['data', 'security', 'voice', 'notSecret']

for k, v in vlan.items():
    print k, v
# This loop will print the dictionary keys and values
10 data
30 security
20 voice
40 notSecret
