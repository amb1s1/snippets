#!/usr/bin/python
# Playing with Strings
ip = "192.168.1.1"
mask = "/24"

# Adding
full_prefix = ip + mask
print ("Full IP With Subnet Mask") # printing # 80 times
print(full_prefix + "\n")  #\n <- will add a line to the print

# Split Method
# Split a string into a list where each word is a list item
ip_split = ip.split(".")
ip_split[-1] = str(int(ip_split[-1]) + 1)
print("IP After The Split")
print(ip_split)

# Join String Function
# Will join a list of items with the given string
# In this case "."
ip = ".".join(ip_split)
# Other way of formating strings
print("\nYour full ip is: {}{}".format(ip, mask))

# Changing a String to all Upper Case
print ("\nUpper & Lower String Method")
foo = "bar"
baz = "QUZ"
print (foo.upper())
print (foo.lower())

