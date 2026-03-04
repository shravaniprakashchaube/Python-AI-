# ctrl + / --> to comment and uncomment a line of code
# print('Welcome to Python programming!')
# print('Welcome to Python programming!')
# print('Welcome to Python programming!')
# print('Welcome to Python programming!')

# docstring - to comment multiple lines of code
# It is mainly used to provide documentation for a function, class, or module. It is a string literal that is used to describe the purpose and usage of the code it is associated with. Docstrings are typically enclosed in triple quotes (""" """) and can span multiple lines.
# example of docstring
# def my_function():
#"""This is a docstring for my_function."""
"""
This is a docstring.
This is a docstring.
print('Welcome to Python programming!')
"""
# comment and docstring are not executed by the Python interpreter, 
# they are only for the programmer's reference. 
# They are used to explain the code and make it more readable.
#=======================================================================
"""
# Modules in Python - A module is a file containing Python definitions and 
# statements.

# import module info

import info
print(info.x,info.y)
info.display()
#------------------------------
# Module aliasing - It is a way to give a module a different name when importing it.

import info as i
print(i.x,i.y)
i.display() 

#-------------------------------
# to read all memebers  of a module directly we can use
from module_name import * option

from info import *
display()
------------------------------
# Member aliasing - It is a way to give a member of a module a different name when importing it.

from info import x_information as x_info, display_corner as dc
print(x_info)
dc()
----------------------------
"""
from bank.info import a
print(a)







