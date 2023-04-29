"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-01-25"
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
from functions import stack_combine
from Stack_array import Stack
from utilities import array_to_stack

source1 = Stack()
source2 = Stack()

array_to_stack(source1, [5, 8, 12, 8])
array_to_stack(source2, [3, 6, 1, 7, 9, 14])
i = Stack()

i.combine(source1, source2)

while not i.is_empty():
    val = i.pop()
    print(val)