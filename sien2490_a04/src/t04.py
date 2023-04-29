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
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

source = Priority_Queue()
source.insert(1)
source.insert(2)
source.insert(3)
#define key
key = 2

#use function
target1, target2 = pq_split_key(source, key)
#print
print("Printing target 1")
while len(target1) > 0:
    print(target1.remove())

print("Printing target 2")
while len(target2) > 0:
    print(target2.remove())