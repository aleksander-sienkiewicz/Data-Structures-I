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
file_variable=open("new_foods.txt","w")
fv=open("foods.txt","r")
foods=Food_utilities.read_foods(fv)
Food_utilities.write_foods(file_variable,foods)