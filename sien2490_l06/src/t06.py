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

new_list = List()

fv = open("foods.txt", "rt")
foods = read_foods(fv)
fv.close()

for i in foods:
    new_list.append(i)

print(new_list[5])
new_list[5] = foods[9]
print("---------")
print(new_list[5])