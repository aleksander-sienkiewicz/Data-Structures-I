"""
-------------------------------------------------------
Assignment 1, Task 2
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-19"
-------------------------------------------------------
"""
# Imports
from functions import dsmvwl

CASES = (
    "",
    "A",
    "a",
    "B",
    "b",
    "a bAB o",
    "aye"
)
for case in CASES:
    print(f"String: {case}")
    new_string = dsmvwl(case)
    # Printing the '|' shows spaces.
    print(f'Disemvowelled: |{new_string}|')
    print()

print("Done")
