"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-01-12"
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
from functions import matrix_transpose
a = [[0, 2, 4, 6, 8], [1, 3, 5, 7, 9]]
b = matrix_transpose(a)
print(f'Matrix Is: {a} ')
print(f'Transposed Matrix Is: {b}')