"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-01-20"
-------------------------------------------------------
"""
# Imports

# Constants
from Food_utilities import read_foods, food_table
f = open('food.txt', "rt")
foods = read_foods(f)
f.close()

food_table(foods)