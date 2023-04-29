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
from functions import max_diff

str = input("Enter values seperated by a comma: ").split(",")
values = []
for i in str:
    values.append(int(i))

difference = max_diff(values)

print(f"The Biggest Difference Is: {difference}")