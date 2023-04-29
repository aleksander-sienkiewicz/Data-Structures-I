"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-03-05"
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

lst2 = List()

a = [2, 4, 3, 5, 1]
a1 = [2, 4, 12, 5, 1]

for i in a:
    lst.append(i)

for i in a1:
    lst1.append(i)

lst2.union_r(lst, lst1)

for i in lst2:
    print(i)