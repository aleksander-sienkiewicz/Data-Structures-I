"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2019-01-25"
-------------------------------------------------------
"""
from Food_utilities import read_foods, food_table


fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)
fv.close()

food_table(foods)
print("Done")
