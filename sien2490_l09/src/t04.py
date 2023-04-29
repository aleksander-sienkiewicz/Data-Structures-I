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

set= Hash_Set(1)
a= [1, 200, 3000, 40000, 500000, 2, 3, 4, 5]

for i in a:
    set.insert(i)

print("Hash set:")
set.debug()

for i in a:
    set.insert(i+ 1)
    set.insert(i+ 2)

print()
print("New hash set is:")
set.debug()