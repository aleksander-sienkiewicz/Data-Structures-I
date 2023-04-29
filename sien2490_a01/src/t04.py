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
from functions import is_leap_year
yr=int(input("Enter your year: "))
leapYR=is_leap_year(yr)
if leapYR:
    print(f"{yr} is a leap year!")
else:
    print(f"{yr} is not a leap year")