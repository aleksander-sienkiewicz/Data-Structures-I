"""
-------------------------------------------------------
[program testing]
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
import Food_utilities
line="Orange Chicken|1|False|800"
string=Food_utilities.read_food(line)
print(string)