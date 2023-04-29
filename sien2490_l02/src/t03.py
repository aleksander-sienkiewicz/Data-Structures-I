"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-01-22"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack, stack_to_array

from Stack_array import Stack
#establish variables
stack = Stack()
target = []
source = ["top", "bottom"]
#array to stack function
array_to_stack(stack, source)
#call stack to array function
stack_to_array(stack, target)
#print statement
print(target)