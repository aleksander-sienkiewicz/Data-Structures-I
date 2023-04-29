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
from test_Sorts_List_linked import SORTS, test_sort

# IMPORTANT!!!! for this task to work you need to download the assignment 07 solution
# And write the clear method for the linked list
# Thanks to @cgram_00 from discord for the help

print(
    f'n:   100       |      Comparisons       | |         Swaps          |')
print('Algorithm      In Order Reversed   Random In Order Reversed   Random')
print('-------------- -------- -------- -------- -------- -------- --------')

for i in SORTS:
    test_sort(i[0], i[1])