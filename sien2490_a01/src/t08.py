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
from functions import matrix_stats
a = [[100, 10, 3, 99], [1000, -29, 10,43]]
print(a)
small, large, total, average = matrix_stats(a)

print(f'Smallest Value: {small}')
print(f"Largest Value: {large}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")