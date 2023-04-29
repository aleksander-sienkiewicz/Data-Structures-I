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

# Constants
from utilities import stack_test

from Food_utilities import read_foods
#use file for data
file = open('food.txt', "rt")
foods = read_foods(file)
file.close()
#run function with data
stack_test(foods)