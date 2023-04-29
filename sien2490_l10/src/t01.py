"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-03-26"
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
from test_Sorts_array import create_sorted, create_reversed, create_randoms

val1 = create_sorted()

print('1st value in values1: ')
print(val1[0])
#
val2 = create_reversed()

print()
print('1st value in values2: ')
print(val2[0])

val3 = create_randoms()

print()
print('1st value in first array in values3: ')
print(val3[0][0])