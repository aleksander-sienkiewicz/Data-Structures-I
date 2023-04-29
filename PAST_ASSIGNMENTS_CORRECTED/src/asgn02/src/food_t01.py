"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2019-01-25"
-------------------------------------------------------
"""
from Food import Food
from Food_utilities import by_origin, read_foods


fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)
fv.close()

for origin in range(len(Food.ORIGIN)):
    temp = by_origin(foods, origin)
    print("  Origin: {}".format(Food.ORIGIN[origin]))
    print()

    for f in temp:
        print(f)
    print()

print("Done")
