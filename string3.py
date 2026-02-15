#😊string 
# we have 2 types of methods
# empty method ( )
# method with arguments/paramters (value)    
a = 'python java'
a
a.upper()  # empty method
# replace java by .net
#a.replace(old,new)
a.replace('java','.net')  #method with args.
x = a.replace('java','.net')
# in order to divide the str into words (default space is a splittiing criteria)
a.split()  # this will return a [] list of string
# we can speicify other splitting criteria as well
b.split('-')
b.split('-')[-1]
help(b.split)
type([])#list
c = ['Hello','Good evening','Python']
# convert above list into str --> use '--'.join(object) method
' '.join(c)
Assignment: Remaining methods of a string
#List
#syntax: []
#Background data structure of a list is an Array
#It preserves sequence order
# list accespts homo./hetro data
d1 = [1,2,3,4] # here data is of same type hence this list is homo.
d1
# when data inside a list is of mix type then it is hetro. list
d2 = [12,'vinay',44.22,5+4j,[2,3,4]]
d2
# indexing is supported
d2[0]
d2[-1]
