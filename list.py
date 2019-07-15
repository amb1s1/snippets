'''
Python has few built-in data structure
 1. lists
 2. dictionaries
 3. tuples
 4. sets
''' 

# list are sequence of objects
# here we have hosts which has three objects
hosts = ['pr01.jfk01', 'pr02.jfk01', 'pr03.jfk01']

# access the objects
print (hosts[0]) # print the first object
['pr01.jfk01']

print (hosts[-1]) # access the last object in the list
['pr03.jfk01']

# Some of list methods
hosts.append('pr04.jfk01') # will add this object to the end of the list
print (hosts) 
['pr01.jfk01', 'pr02.jfk01', 'pr03.jfk01', 'pr04.jfk01']

# slicing - accessing range of objects
print (hosts[1:3]) # print range from 1 to 3-1 
['pr02.jfk01', 'pr03.jfk01']

hosts.insert(2, 'pr05.jfk01') # insert a new object in 2 second spot

hosts.sort() # will sort the objects in this list
hosts.reverse() # reverse the list
print (hosts)
['pr05.jfk01', 'pr04.jfk01', 'pr03.jfk01', 'pr02.jfk01', 'pr01.jfk01'] 
