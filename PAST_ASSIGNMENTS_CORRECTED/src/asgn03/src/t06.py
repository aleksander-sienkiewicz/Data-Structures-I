"""
-------------------------------------------------------
Assignment 3, Task 6
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""
# Imports
from functions import reroute

print("Testing 'reroute'")
print()
tuples = (
    ('', []), ('', [1]), ('SX', []), ('SX', [1]), ("SSSSXXXX", [1, 2, 3, 4]),
    ("SXSXSXSX", [1, 2, 3, 4]), ("XXXXSSSS", [1, 2, 3, 4]),
)

for case in tuples:
    print(f"Test: '{case[0]}' - '{case[1]}'")
    b = reroute(case[0], case[1])
    print(f"Reroute: {b}")
    print()
print("Done")
