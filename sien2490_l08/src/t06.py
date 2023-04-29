"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-03-12"
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
from morse import DATA1, fill_code_bst, decode_morse

j = BST()
fill_code_bst(j, DATA1)
txt = "-.. ..-- .-.. .-.."

print(decode_morse(j, txt))