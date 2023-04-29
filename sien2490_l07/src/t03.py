"""
-------------------------------------------------------
l07 t03
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-03-04"
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
from List_linked import List

lst = List()
a = [2,3,1,4,5]

for i in a:
    lst.append(i)

target1, target2 = lst.split_alt_r()

print("Target1: ")
for value in target1:
    print(value)
print("---------------")
print("Target2: ")
for i in target2:
    print(value)