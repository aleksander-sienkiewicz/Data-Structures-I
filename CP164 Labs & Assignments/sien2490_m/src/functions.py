"""
-------------------------------------------------------
Midterm Functions
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-02-12"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
# Constants
OPERATORS = ('*', '/', '+', '-')


def pq_triage(source, key):
    """
    -------------------------------------------------------
    Removes all values from source that have a priority
    less than key.
    Use: pq_triage(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a key value (?)
    Returns‌‌​​​‌‌‌​:
        None
    -------------------------------------------------------
    """
    i = 0
    while i<len(source):
        if source.peek()>key:
            source.remove()
        else:
            i+=1
    return

    # your code here


def purge(source, key):
    """
    -------------------------------------------------------
    Finds and removes all values in source that match key.
    Use: purge(source, key)
    -------------------------------------------------------
    Parameters:
        source - a List of values (List)
        key - a data element (?)
    Returns‌‌​​​‌‌‌​:
        None
    -------------------------------------------------------
    """
    i = 0
    
    while i<len(source):
        if source.peek()==key:
            source.remove(key)
        else:
            i+=1
    # your code here
    return

def eval_expression(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = eval_expression(string)
    -------------------------------------------------------
    Parameters:
        string - the space-separted postfix string to evaluate (str)
    Returns‌‌​​​‌‌‌​:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    s = Stack()
    OPERATIONS= ["+","-","*","/"]
    i=0
    while not string=="":
        for j in string:
            if j in OPERATIONS:
                s.push(j)
    while not string=="":
        for k in string:
            if k== " ":
                #take value from stack and make it the operator
                value=s.peek()
                k = value
                s.pop()
    answer=eval(string)
    return answer
