"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-01-24"
-------------------------------------------------------
"""

#Constants
MIRROR="m"
CHARS="abc"
# Imports
from pickle import TRUE, FALSE
from Stack_array import Stack
def is_mirror(string):
    """
    determine if string is a mirror
    must use abc characters only and m character as the middle
    """
    mirror = True 
    stack=Stack()
    n=len(string)
    count=0
    
    while mirror and count<n and string[count]!=MIRROR:
        
        if string[count] in CHARS:
            stack.push(string[count])
            count+=1
        else:
            mirror=False 
    
    if mirror:
        #skip mirror character
        count+=1
        
        while mirror and count<n and not stack.is_empty():
            c=stack.pop()
            if string[count]!=c:
                mirror=False
            else:
                count+=1
        #check final condition
        if not (stack.is_empty()and count ==n):
            mirror=False 
    return mirror
string="abcmcba"
b=is_mirror(string)
print(string)
print(b)
    