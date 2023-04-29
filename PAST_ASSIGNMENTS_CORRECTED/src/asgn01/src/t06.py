"""
-------------------------------------------------------
Assignment 1, Task 6
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-19"
-------------------------------------------------------
"""
# Imports
from functions import max_diff

CASES = (
    [],
    [0],
    [0, 0, 0, 0],
    [0, 1, 2, 3],
    [40, 20, 10, 5],
    [3, -5, 5, 11, 7]
)
for case in CASES:
    print(f"List: {case}")
    md = max_diff(case)
    print(f"Maximum difference: {md}")
    print()
print("Done")
