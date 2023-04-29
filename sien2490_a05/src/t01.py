"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-02-07"
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
from List_array import List
# Imports
from Food import Food
from Food_utilities import read_food, read_foods
from utilities import array_to_list


# create list

file = open("foods.txt", "rt")
foods = read_foods(file)
file.close()
lst = List()
array_to_list(lst, foods)

#add new item to list (testing append)
nuggies = Food("McNuggets", 1, False, 230)

lst.append(nuggies)
print("Append test")
for value in lst:
    print(f'{value.name} = {lst.count(value)}')


# Test clean
lst.clean()

print()
print("Clean test")
for value in lst:
    print(f'{value.name} = {lst.count(value)}')


#Test combine

temp = [
    read_food("test1|2|False|1000"),
    read_food("test2|4|True|1000")
]


lst1 = List()
lst1.append(temp[0])
lst1.append(temp[1])
lst2 = List()

lst2.combine(lst, lst1)

print()
print("test combine")
for value in lst2:
    print(f"{value.name}")


print()
print("test getitem")
print(lst2[10])


# Test intersection
lst1.append(temp[0])

lst1.append(temp[1])

lst3 = List()

lst3.intersection(lst1, lst2)

print()
print("test intersection")
for value in lst3:
    print(f"{value.name}")


# Test is_identical 
print()
print("test compare")
print(lst3.is_identical(lst2))


# Test prepend

lst3.prepend(temp[0])

print()
print("test prepend")
for value in lst3:
    print(f"{value.name}")


# Test remove front
lst3.remove_front()

print()
print("test remove front")
for value in lst2:
    print(f"{value.name}")


# Test remove many 
lst2.append(temp[0])

lst2.remove_many(temp[0])

print()
print("test remove")
for value in lst2:
    print(f"{value.name}")


# Test split

target1, target2 = lst2.split()

print()
print("test split")
for value in target1:
    print(f"{value.name}")

print()
print("test split")
for value in target2:
    print(f"{value.name}")


# Test split alt
target3, target4 = target1.split_alt()

print()
print("Test alt")
for value in target3:
    print(f"{value.name}")

print()
print("test alt")
for value in target4:
    print(f"{value.name}")


# Test union
lst1.union(target3, target4)

print()
print("Testing union")
for value in lst1:
    print(f"{value.name}")