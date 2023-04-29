"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-01-12"
-------------------------------------------------------
"""
# Imports

# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
         name - description (type)
    ------------------------------------------------------
    """
from functions import file_analyze

file = open('words.txt', 'rt')

u, l, d, w, r = file_analyze(file)

file.close()
print(f"Uppercase Letters:    {u:>3}")
print(f"Lowercase Letters:    {l:>3}")
print(f"Digits:               {d:>3}")
print(f"Whitespace Characters:{w:>3}")
print(f"Remaining Characters: {r:>3}")