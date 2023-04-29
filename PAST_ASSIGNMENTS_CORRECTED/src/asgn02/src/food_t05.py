"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2019-01-25"
-------------------------------------------------------
"""
from Food import Food
from Food_utilities import food_search, read_foods

fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)
fv.close()

print("  Default Search")
print()
temp = food_search(foods, -1, 0, False)

for f in temp:
    print(f)
print()
print("  Origin Search")
print()
temp = food_search(foods, 2, 0, False)
print("  Origin: {}".format(Food.ORIGIN[2]))

for f in temp:
    print(f)
print()

print("  Calorie Search")

cals = 100
temp = food_search(foods, -1, cals, False)
print("  Calories <= {}".format(cals))

for f in temp:
    print(f)
print()

print("  Vegetarian Search")

temp = food_search(foods, -1, 0, True)

for f in temp:
    print(f)
print()

print("  All Search")

temp = food_search(foods, 1, 200, True)
print("  Search for Chinese Vegetarian <= 200 Calories")

for f in temp:
    print(f)
print()

print("Done")
