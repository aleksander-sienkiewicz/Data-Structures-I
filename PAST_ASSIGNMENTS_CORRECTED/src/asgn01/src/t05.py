"""
-------------------------------------------------------
Assignment 1, Task 5
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-19"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome

CASES = ("David", "Otto", "racecar", "Able was I ere I saw Elba")
for case in CASES:
    print(f"String: {case}")
    result = is_palindrome(case)
    print(f"Palindrome: {result}")
    print()

print("Done")
