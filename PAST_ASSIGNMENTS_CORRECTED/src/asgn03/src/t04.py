"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_reverse

# Constants
RANGE = range(11, 67, 11)
ORDERED = list(RANGE)


print("Testing 'stack_reverse'")
print()

source = Stack()
for v in ORDERED:
    source.push(v)

print("source contents:")
for v in source:
    print(v, end=", ")
print()

print()
print("Reverse")
stack_reverse(source)
print("source contents:")
for v in source:
    print(v, end=", ")
print()

print()
print("Done")
