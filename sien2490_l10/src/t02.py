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
from test_Sorts_array import SORTS, test_sort
#
print(
    f'n:   100       |      Comparisons       | |         Swaps          |')
print('Algorithm      In Order Reversed   Random In Order Reversed   Random')
print('-------------- -------- -------- -------- -------- -------- --------')
test_sort(SORTS[0][0], SORTS[0][1])