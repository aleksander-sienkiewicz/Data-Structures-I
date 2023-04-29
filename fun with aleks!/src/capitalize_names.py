"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-02-14"
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
    
name = input("Enter your full name: ")
while name != "":
    (name[0]).capitalize()
    for i in range(name):
        if name[i].islower() and (name[i-1]==" " or name[i-1]=="-"):
            name[i]=name[i].capitalize()
    