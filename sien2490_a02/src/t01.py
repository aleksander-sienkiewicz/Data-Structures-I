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

from Food import Food
from Food_utilities import read_foods, by_origin

file=open("food.txt","rt")
foods=read_foods(file)

file.close()

origin=int(input(f"Enter an origin (int)\n{Food.origins()}2"))
origins=by_origin(foods, origin)
for food in origins:
    print(food, end="\n\n")