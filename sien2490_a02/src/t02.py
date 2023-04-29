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

from Food_utilities import average_calories, read_foods

file = open('food.txt', "rt")
foods = read_foods(file)
file.close()

average = average_calories(foods)

print(f"Average Calories: {average}")
