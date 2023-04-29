"""
-------------------------------------------------------
Assignment 1, Task 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-19"
-------------------------------------------------------
"""
# Imports
from functions import clean_list
from copy import copy

CASES = (
    [],
    list(range(6)),
    [0] * 6,
    list(range(4)) * 3
)
for case in CASES:
    print(f"List: {case}")
    # Make a copy to preserve the list being cleaned
    a = copy(case)
    clean_list(a)
    print(f"Cleaned list: {a}")
    print()
print("Done")
