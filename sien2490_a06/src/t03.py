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
from Deque_linked import Deque

queue = Deque()

print("Queue is empty?: ")
print(queue.is_empty())

queue.insert_front(100)
queue.insert_rear(200)

print("Length of queue: ")
print(len(queue))
print()
print("Value at Front: ")
print(queue.peek_front())
print()
print("Value at Rear: ")
print(queue.peek_rear())
print()
print("Value Removed: ")
print(queue.remove_front())
print()
print("Value Removed: ")
print(queue.remove_rear())

queue.insert_front(100)
queue.insert_rear(200)
queue.insert_rear(300)
queue.insert_rear(400)

queue._swap(queue._rear, queue._front)

print()
print("Values in queue: ")
for value in queue:
    print(value)