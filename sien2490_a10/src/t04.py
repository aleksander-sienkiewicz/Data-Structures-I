"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-04-01"
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
from Sorts_Deque_linked import Sorts
from Deque_linked import Deque


array = [12,7,13,5,6,15,3,1,14,4,11,0,8,10,2]
#
a = Deque()

for i in array:
    a.insert_rear(i)
Sorts.gnome_sort(a)
for j in a:
    print(j, end=', ')
