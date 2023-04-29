"""
-------------------------------------------------------
Assignment 1, Task 3
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-19"
-------------------------------------------------------
"""
# Imports
from functions import file_analyze

filename = "pelee.txt"
print(f"File: {filename}")
fv = open(filename, "r", encoding="utf-8")
r = file_analyze(fv)
fv.close()
print(f"Results: {r}")
print()
print("Done")
