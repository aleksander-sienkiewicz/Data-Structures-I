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




from Stack_array import Stack
#ariable
stack = Stack()
#print stack status
if stack.is_empty():
    print("Stack is empty\n")
else:
    print("Stack is not empty\n")

stack.push(1)
item = stack.pop()

print(f"{item} is no longer in the stack\n")

stack.push("bottom\n")
stack.push("top\n")

print(stack.peek())