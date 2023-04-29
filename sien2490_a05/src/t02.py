"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-02-09"
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
# Imports
from Sorted_List_array import Sorted_List

lst = Sorted_List()

lst.insert(10)

lst.insert(20)

lst.insert(30)

lst.clean()

print()
print("Testing")
for value in lst:
    print(value)



print()
print("Testing")
print(20 in lst)

lst.insert(50)


print()
print("Testing")
print(lst.count(50))

print()
print("Testing")
print(lst.find(50))


print()
print("Testing")
print(lst[2])



print()
print("Testing")
print(lst.index(50))


lst2 = Sorted_List()

lst2.insert(100)

lst2.insert(1000)

lst3 = Sorted_List()

lst3.intersection(lst, lst2)

print()
print("Testing")
for value in lst3:
    print(value)


print()
print("Testing")
print(lst.is_identical(lst2))


print()
print("Testing")
print(lst2.max())

print()
print("Testing")
print(lst2.min())


print()
print("Testing")
print(lst.peek())


lst2.remove(100)

print()
print("Testing")
for value in lst2:
    print(value)


lst.remove_front()

print()
print("Testing")
for value in lst:
    print(value)


lst4 = Sorted_List()

lst4.insert(33)

lst4.insert(44)

lst4.insert(44)

lst4.remove_many(33)

print()
print("Testing")
for value in lst4:
    print(value)


lst4.insert(1000)

lst4.insert(1000)

target1, target2 = lst4.split()

print()
print("Testing")
for value in target1:
    print(value)

print()
print("Testing")
for value in target2:
    print(value)


target1.insert(10000)

target1.insert(1000000)

target3, target4 = target1.split_alt()

print()
print("Testing")
for value in target3:
    print(value)

print()
print("Testing")
for value in target4:
    print(value)

target3.insert(1000)

target3.insert(3000000)

target5, target6 = target3.split_key(20000)

print()
print("Testing")
for value in target5:
    print(value)

print()
print("Testing")
for value in target6:
    print(value)

target3.union(target5, target6)

print()
print("Testing")
for value in target3:
    print(value)    