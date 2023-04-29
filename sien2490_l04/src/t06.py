"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-02-05"
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
from List_array import List
from utilities import array_to_list, list_to_array

lst = List()
values = [2, 4, 6, 8, 10]
array_to_list(lst, values)
print("Printing LList: ")
for i in lst:
    print(i)
list_to_array(lst, values)
print()
print("Printing List: ")
for i in values:
    print(i)