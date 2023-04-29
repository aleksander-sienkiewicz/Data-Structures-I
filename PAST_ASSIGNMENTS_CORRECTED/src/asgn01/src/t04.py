"""
-------------------------------------------------------
Assignment 1, Task 4
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-19"
-------------------------------------------------------
"""
# Imports
from functions import is_leap_year

CASES = (1900, 1999, 2000, 2004)
for case in CASES:
    print(f"Year: {case}")
    b = is_leap_year(case)
    print(f"Leap year: {b}")
    print()

print("Done")
