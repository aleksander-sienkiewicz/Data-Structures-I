"""
-------------------------------------------------------
Assignment 1, Task 8
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-19"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats

CASES = (
    [[0]],
    [[10]],
    [[1, 1], [1, 1]],
    [[1, 1, 1, 1], [1, 1, 1, 1]],
    [[1, 1], [1, 1], [1, 1], [1, 1]],
    [[4, 5, 6], [3, 2, 1], [9, 8, 7]]
)
for case in CASES:
    print(f"Matrix: {case}")
    stats = matrix_stats(case)
    print(f"Stats: {stats}")
    print()
print("Done")
