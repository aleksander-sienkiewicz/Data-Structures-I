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

from Stack_array import Stack
from functions import stack_reverse
from utilities import array_to_stack

stack=Stack()
array_to_stack(stack, [1,5,6,9])
stack_reverse(stack)
while not stack.is_empty():
    value = stack.pop()
    print(value)