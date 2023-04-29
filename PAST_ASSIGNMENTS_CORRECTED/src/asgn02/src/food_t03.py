"""
-------------------------------------------------------
Assignment 2, Task 3
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2019-01-25"
-------------------------------------------------------
"""
from Food import Food
from Food_utilities import read_foods, calories_by_origin


fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)
fv.close()

for origin in range(len(Food.ORIGIN)):
    ac = calories_by_origin(foods, origin)
    print("Average calories: {:12}{:5d}".format(Food.ORIGIN[origin], ac))

print("Done")
