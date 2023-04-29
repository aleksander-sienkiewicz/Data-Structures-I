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
#imports
from Queue_circular import Queue

q = Queue(3)

print(len(q))

print(q.is_empty())

q.insert(50)

print(len(q))

value = q.peek()

print(value)

removed = q.remove()

print(removed)

q.insert(50)
q.insert(100)
q.insert(200)
print(q.is_full())