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

from Food_utilities import read_foods, calories_by_origin
file = open('food.txt', "rt")
foods = read_foods(file)
file.close()
average = calories_by_origin(foods, 2)

print(f'Average Calories: {average}')