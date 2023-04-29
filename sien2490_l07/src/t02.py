"""
-------------------------------------------------------
l07 t01
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-03-04"
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
from List_linked import List

lst = List()
lst1 = List()

a = [2, 3, 5, 4, 1]
a1 = [4, 3, 2, 1, 5]

for value in a:
    lst.append(value)
for value in a1:
    lst1.append(value)
#
print(lst.is_identical_r(lst1))