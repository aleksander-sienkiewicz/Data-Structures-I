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
from Queue_circular import Queue
from functions import queue_split_alt

source = Queue(3)
source.insert(1)
source.insert(2)
source.insert(3)

target1, target2 = queue_split_alt(source)

#print statements
print("Printing target 1")
while len(target1) > 0:
    print(target1.remove())

print("Printing target 2")
while len(target2) > 0:
    print(target2.remove())