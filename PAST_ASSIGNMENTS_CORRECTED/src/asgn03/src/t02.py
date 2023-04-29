"""
-------------------------------------------------------
Assignment 3, Task 2
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_combine

# Constants
SIZE = 6
BASE = 11
RANGE = range(BASE, BASE * SIZE + 1, BASE)
ORDERED = list(RANGE)

print("Testing 'stack_combine'")
print()

source1 = Stack()

for v in ORDERED[:3]:
    source1.push(v)

print("source1 contents:")
for v in source1:
    print(v, end=", ")
print()

source2 = Stack()
for v in ORDERED[3:]:
    source2.push(v)

print("source2 contents:")
for v in source2:
    print(v, end=", ")
print()

print()
print("Combine:")
target = stack_combine(source1, source2)

print("source1 contents:")
for v in source1:
    print(v, end=", ")
print()

print("source2 contents:")
for v in source2:
    print(v, end=", ")
print()

print("target contents:")
for v in target:
    print(v, end=", ")
print()

print()
print("Compare to Stack 'combine'")
print()

source1 = Stack()
for v in ORDERED[:3]:
    source1.push(v)

print("source1 contents:")
for v in source1:
    print(v, end=", ")
print()

source2 = Stack()
for v in ORDERED[3:]:
    source2.push(v)

print("source2 contents:")
for v in source2:
    print(v, end=", ")
print()

target = Stack()

print()
print("Combine:")
target.combine(source1, source2)

print("source1 contents:")
for v in source1:
    print(v, end=", ")
print()

print("source2 contents:")
for v in source2:
    print(v, end=", ")
print()

print("target contents:")
for v in target:
    print(v, end=", ")
print()

print()
print("Done")
