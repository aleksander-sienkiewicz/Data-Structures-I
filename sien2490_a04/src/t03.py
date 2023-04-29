"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-02-03"
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
from Queue_array import Queue

source = Queue()
source.insert(1)
source.insert(2)
source.insert(3)

target1, target2 = source.split_alt()

#print statements
print("Printing target 1")
while len(target1) > 0:
    print(target1.remove())

print("Printing target 2")
while len(target2) > 0:
    print(target2.remove())