'''
Created on Aug 31, 2020

@author: Dattatray.Jadhav
'''

# Keywords: def, del,elif,from, gloabl,yield-To end a function, returns a generator,

#Python has no command for declaring a variable.''
'''Text Type:    str
Numeric Types:    int, float, complex
Sequence Types:    list, tuple, range
Mapping Type:    dict
Set Types:    set, frozenset
Boolean Type:    bool
Binary Types:    bytes, bytearray, memoryview
'''

x = tuple(("apple", "banana", "cherry"))

print(x)

# Type conversion

num_int=123
num_float=12.22
num_str="456"
num_str2=int(num_str)   # type cast str to int 

print("data type of num_int" ,type(num_int))
print("data type of num_float" ,type(num_float))

print(num_int+num_float)
print(num_int+num_str2)

print(1, 2, 3, 4, sep='#', end='&')

# Output Formating
x=12;y=22
print("/n")
print("value of x is {} and y is {}".format(x, y))

print("My name is {0} and I studid in {1}".format('Dattatray','10'))

print("My name is {name} and I studid in {clg} ".format(name='Dattatray', clg='SP college'))

#Import

import math
print(math.asin(1))
print(math.pi)

import sys

#namespace
# Note: You may get different values for the id

a = 2
print('id(2) =', id(2))

print('id(a) =', id(a))

def printHello():
    print("Hello")


a = printHello

a()