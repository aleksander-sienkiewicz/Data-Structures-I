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


from utilities import array_to_stack

from Stack_array import Stack
#variables
stack = Stack()
source = ["top\n", "bottom\n"]
#call function
array_to_stack(stack, source)
#print only when the stack is not empty
while not stack.is_empty():
    item = stack.pop()
    print(item)