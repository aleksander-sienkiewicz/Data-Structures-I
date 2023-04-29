"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-03-19"
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
    
from Hash_Set_array import Hash_Set

set= Hash_Set(10)
set.insert(200)
set.insert(3000)
set.insert(4000)

print('Printing hash set: ')
for i in set:
    print(i)

removed= set.remove(3000)
print('Removing value: ')
print(removed)

print('Printing hash set: ')
for i in set:
    print(i)