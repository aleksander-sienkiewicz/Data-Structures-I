"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-02-25"
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
from Food_utilities import read_foods
from List_linked import List

new = List()

fv = open("foods.txt", "rt")
foods = read_foods(fv)
fv.close()

for i in foods:
    new.append(i)

print(new.find(foods[1]))
print(new.index(foods[1]))
print(foods[1] in new)