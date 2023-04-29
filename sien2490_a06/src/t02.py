"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-03-03"
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
from Priority_Queue_linked import Priority_Queue

queue = Priority_Queue()

print("Queue is empty?: ")
print(queue.is_empty())
print("Length: ")
print(len(queue))
queue.insert(100)

print()
print("Length: ")
print(len(queue))

queue.insert(200)
print()
print("Removed: ")
print(queue.remove())
print()
print("First item: ")
print(queue.peek())

queue1 = Priority_Queue()
queue1.insert(300)
queue2 = Priority_Queue()
queue2.combine(queue, queue1)

print()
print("Printing queue2: ")
for value in queue2:
    print(value)
target1, target2 = queue2.split_alt()
print()
print("Printing target1: ")
for value in target1:
    print(value)

print()
print("Printing target2: ")
for value in target2:
    print(value)

queue2.insert(100)
queue2.insert(200)
queue2.insert(300)
queue2.insert(400)

target3, target4 = queue2.split_key(33)

print()
print("Printing target1: ")
for value in target3:
    print(value)

print()
print("Printing target2: ")
for value in target4:
    print(value)