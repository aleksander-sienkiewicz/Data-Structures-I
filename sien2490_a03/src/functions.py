"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-01-25"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from pickle import FALSE, NONE

#t01
def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    counter = 1
    while not source1.is_empty() or not source2.is_empty():
        
        if source1.is_empty() or counter % 2 == 0 and not source2.is_empty():
            j = source2.pop()
            target.push(j)
        
        else:
            j = source1.pop()
            target.push(j)
        
        counter += 1
    
    return target

#t02 done in Stack_array

#t03

def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    list=[]
    while not source.is_empty:
        stat=source.pop()
        list.insert(0,stat)
    for i in range(len(list)-1,-1,-1):
        stat=list.pop(i)
        source.push(stat)
        return

#t04 done in Stack_array
#t05
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stack = Stack()
    palindrome = True
    reverse = len(string) - 1
    k1 = 0
    k2 = True
    while k1 < len(string) and reverse > 0 and palindrome:
        if string[k1].isalpha() and k2:
            stack.push(string[k1].lower())
        elif string[reverse].isalpha() and k2:
            reverse += 1
        else:
            k2 = True
        if reverse < len(string):
            if string[reverse].isalpha():
                if not stack.is_empty():
                    if string[reverse].lower() != stack.pop():
                        palindrome = False
            elif string[k1].isalpha():
                k2 = False
                k1 -= 1
        reverse -= 1
        k1 += 1
                
    return(palindrome)
#t06
def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    stack=Stack()
    i=0
    values_i=0
    values_out=[]
    contin=True
    while contin and values_i <=len(values_in) and i<len(opstring):
        if opstring[i]=="S"and values_i<len(values_in):
            stack.push(values_in[values_i])
            values_i+=1
        elif opstring[i] == "X":
            if stack.is_empty()==True:
                contin=False
                values_out=None
            else:
                values_out.append(stack.pop())
        i+=1
    if stack.is_empty==False:
        values_out=None
    elif i <len(opstring)-1:
        values_out=None
    elif values_i< len(values_in)-1:
        values_out=None
    return values_out

def new_route(opstring, value_in):
    stack = Stack()#create the stack for our operations / u know this
    i = 0# index value// will be cumulative throughout while loop
    values_i = 0 #values of the index at iteration
    values_out=[]#open list to work with, all removed values go in here
    contin = True# is it continuous? is so == true
    
    While contin and i<len(opstring) and values_i <= len(values_in):
        if opstring[i]=="S" and values_i < len(values_in):
            stack.push(values_in[values_i])
            values_i+=1
        elif opstring[i]=="X"
            if stack.is_empty()==True:
                contin=False
                values_out=None
        
                
    






