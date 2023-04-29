"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-01-29"
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
from utilities import array_to_queue, queue_to_array, queue_test
from Queue_array import Queue

q = Queue()
values=[1,2,3,4,5]

array_to_queue(q, values)
for i in range(len(q)):
    value = q.remove()
    
    print(value)
    values.append(value)

array_to_queue(q, values)
queue_to_array(q, values)

print(values)

queue_test(values)