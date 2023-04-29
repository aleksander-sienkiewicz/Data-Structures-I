"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-03-18"
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
from BST_linked import BST

bst= BST()
array = [1,2,3,4]

for i in array:
    bst.insert(i)

print(bst.is_valid())

print(bst.is_balanced())

bst1 = BST()

for i in [1, 2, 3, 4]:
    bst1.insert(i)

print(bst.is_identical(bst1))

print()
print(bst.min())

print()
print(bst.leaf_count())

print()
print(bst.one_child_count())

print()
print(bst.two_child_count())

print()
print(bst.inorder())

print()
print(bst.preorder())

print()
print(bst.postorder())

print()
print(bst.levelorder())

print()
print(bst.remove(2))

print()
for i in bst:
    print(i)