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
from Priority_Queue_array import Priority_Queue
from utilities import array_to_pq, pq_to_array, priority_queue_test
from Food_utilities import read_foods

pq=Priority_Queue()

values=[1,2]
array_to_pq(pq, values)

while len(pq)>0:
    val = pq.remove()
    print(val)
    values.append(val)

array_to_pq(pq, values)
pq_to_array(pq, values)
print(values)
fv=open("foods.txt","rt")
food=read_foods(fv)
fv.close()
priority_queue_test(food)