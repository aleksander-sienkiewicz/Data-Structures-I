"""
-------------------------------------------------------
Assignment 1, Task 9
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-19"
-------------------------------------------------------
"""
# Imports
from functions import pig_latin

CASES = (
    "car",
    "yard",
    "lynx",
    "art",
    "David",
    "track"
)
for case in CASES:
    print(f"String: {case}")
    pl = pig_latin(case)
    print(f"Pig Latin: {pl}")
    print()
print("Done")
