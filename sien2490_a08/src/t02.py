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
from Letter import Letter
from functions import do_comparisons, comparison_total

DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst1 = BST()
bst2 = BST()
bst3 = BST()

for i in DATA1:
    letter = Letter(i)
    bst1.insert(letter)

for i in DATA2:
    letter = Letter(i)
    bst2.insert(letter)

for i in DATA3:
    letter = Letter(i)
    bst3.insert(letter)

file= open('gibbon.txt', 'rt')
do_comparisons(file, bst1)
total = comparison_total(bst1)
file.close()
print("-------------------------------")
print(f"Comparing by order: {DATA1}")
print(f"Total Comparisons:  {total:,}")


file= open('gibbon.txt', 'rt')

do_comparisons(file, bst2)
total = comparison_total(bst2)
file.close()

print("-------------------------------")
print(f"Comparing by order: {DATA2}")
print(f"Total Comparisons:  {total:,}")

file= open('gibbon.txt', 'rt')
do_comparisons(file, bst3)
total = comparison_total(bst3)
file.close()

print("-------------------------------")
print(f"Comparing by order: {DATA3}")
print(f"Total Comparisons:  {total:,}")