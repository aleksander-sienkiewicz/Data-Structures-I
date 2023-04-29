"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-03-11"
-------------------------------------------------------
"""
# Imports

# Constants

def func():
    """
    -------------------------------------------------------
    description
    Use: 
    -------------------------------------------------------
    Parameters:
        name - description (type)
    Returns:
         name - description (type)
    ------------------------------------------------------
    """
from Food_utilities import read_foods
from Sorted_List_linked import Sorted_List


file = open("foods.txt", "rt")

foods = read_foods(file)

file.close()

sl = Sorted_List()

for value in foods:
    sl.insert(value)

sl.insert(foods[8])
for value in sl:
    print(f"{value.name:35} {sl.count(value):>5}")

sl.clean()
for value in sl:
    print(f"{value.name:35} {sl.count(value):>5}")

print()
print(f"{foods[-4].name} in sl?: ")
print(foods[-3] in sl)

print()
print(f"Index of {foods[-4].name}: ")
print(sl.index(foods[-2]))

print()
print(f"{foods[-4].name}: ")
print(sl.find(foods[-1]))

print()
print(f"Second item: ")
print(sl[1])

print()
print(f"First item: ")
print(sl.peek())

print()
print(f"Min value: ")
print(sl.min())

print()
print(f"Max value: ")
print(sl.max())

print()
print(f"Remove first value: ")
print(sl.remove_front())

print()
print(f"Remove {foods[-4].name}: ")
print(sl.remove(foods[-4]))

sl1 = Sorted_List()

sl2 = Sorted_List()

for value in range(10):
    sl1.insert(foods[value])

sl2.intersection(sl, sl1)

print()
for value in sl2:
    print(f"{value.name:35} {sl2.count(value):>5}")

print()
print("sl2 and sl3 are identical?: ")
print(sl1.is_identical(sl2))

sl3 = Sorted_List()

sl3.union(sl1, sl2)

print()
for value in sl3:
    print(f"{value.name:35} {sl3.count(value):>5}")