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

lst = List()

lst.append(0)
lst.append(2)
lst.append(4)
lst.append(-2)
lst.append(-4)
print(lst.index(-1))
print(lst.find(-1))
if 2 in lst:
    print("2 is in lst")
else:
    print("2 is not in lst")
print(lst.count(0))
print(lst.min())
print(lst.max())