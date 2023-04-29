"""
-------------------------------------------------------
Assignment 3, Task 5
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome_stack

print("Testing 'is_palindrome_stack'")
print()
strings = ("", "a", "aa", "aaa", "otto", "RaceCar", "Able was I ere I saw Elba",
           "A man, a plan, a canal, Panama!", "David")

for string in strings:
    print(f"Test: '{string}'")
    b = is_palindrome_stack(string)
    print(f"Palindrome: {b}")
    print()
print("Done")
