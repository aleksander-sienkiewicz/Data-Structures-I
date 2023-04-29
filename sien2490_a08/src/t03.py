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
from functions import do_comparisons, letter_table

# Takes a long time to compute
DATA= "ETAOINSHRDLUCMPFYWGBVKJXZQ"
bst= BST()

for i in DATA:
    letter = Letter(i)
    bst.insert(letter)

file= open('gibbon.txt', 'rt')
do_comparisons(file, bst)
file.close()
letter_table(bst)