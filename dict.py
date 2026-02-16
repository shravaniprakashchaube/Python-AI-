#Dictionary
a = {}  #empty dict
type(a)
# set vs dict
# set is a collection of objects separated by comma ,
# dict is a collection of key:value pairs
b = {1:100,2:200,3:300}
b
c = {'name':'python','age':36,2:22.2}
c
# Features of a dict
# duplicate keys are not allowed
g = {1:10,1:1000,1:'java'}
g
# Rule- If we have multiple values with same key present in the dict then it takes last recent pair
# in above case 1:'java' is last key value pair
# Iterable: collection of elements, we have more than oe element
s = {(1,2),'sourabh'}
s
h = {1:10,[2,4]:1000,3:'java'}  # here we are trying to set a list as a key which is not allowd- check below rule
h
# in a set we can not give/add MUTABLE objects
# & in dict we can not set key as a mutable object
