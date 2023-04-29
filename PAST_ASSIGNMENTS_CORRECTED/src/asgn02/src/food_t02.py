"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2019-01-25"
-------------------------------------------------------
"""
from Food_utilities import read_foods, average_calories


fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)
fv.close()

ac = average_calories(foods)

print("Average calories for all foods: {}".format(ac))
print("Done")
