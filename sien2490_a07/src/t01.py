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
from List_linked import List

file = open("foods.txt", "rt")

foods = read_foods(file)

file.close()

lst = List()

for value in foods:
    lst.append(value)

print("Printing first item: ")
print(lst[0])

lst.prepend(foods[8])

print()
print("Printing first item: ")
print(lst[0])


for value in lst:
    print(f"{value.name:35} {lst.count(value):>5}")

lst.clean()

print()
print("Printing count: ")
for value in lst:
    print(f"{value.name:35} {lst.count(value):>5}")

lst1 = List()

lst2 = List()

for i in range(10):
    lst1.append(foods[i])

lst1.combine(lst, lst2)

print()
for value in lst2:
    print(f"{value.name:35} {lst2.count(value):>5}")


for i in range(23, 30):
    lst.append(foods[i])

lst1.intersection(lst, lst2)

print()
for i in lst1:
    print(f"{i.name:35} {lst2.count(i):>5}")


print()
print("lst1 and lst2 identical?: ")
print(lst.is_identical(lst2))

print()
print("Printing removed value: ")
print(lst.remove_front())


print()
for i in lst2:
    print(f"{i.name:35} {lst2.count(i):>5}")


lst2.remove_many(foods[0])

print()
for i in lst2:
    print(f"{i.name:35} {lst2.count(i):>5}")

target1, target2 = lst2.split()

print()
for i in target1:
    print(f"{i.name:35} {target1.count(i):>5}")

print()
for i in target2:
    print(f"{i.name:35} {target2.count(i):>5}")

target3, target4 = target1.split_alt()

print()
for i in target3:
    print(f"{i.name:35} {target3.count(i):>5}")

print()
for i in target4:
    print(f"{i.name:35} {target4.count(i):>5}")

lst2.union(target3, target4)

print()
for i in lst2:
    print(f"{i.name:35} {lst2.count(i):>5}")