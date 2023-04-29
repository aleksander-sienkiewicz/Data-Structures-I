"""
-------------------------------------------------------
Assignment 3 Functions
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-01-30"
-------------------------------------------------------
"""
# imports
from Stack_array import Stack


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    (iterative algorithm)
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

    while not source1.is_empty() and not source2.is_empty():
        target.push(source1.pop())
        target.push(source2.pop())

    # Only one (at most) of the next two loops will execute.
    while not source1.is_empty():
        target.push(source1.pop())

    while not source2.is_empty():
        target.push(source2.pop())
    return target


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
    temp = []

    while not source.is_empty():
        temp.append(source.pop())

    while len(temp) > 0:
        source.push(temp.pop(0))
    return


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, spaces, digits and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    # Clean up the string
    temp = ""

    for c in string:
        if c.isalpha():
            temp = temp + c.lower()

    n = len(temp)
    # Get the midpoint of the cleaned up string
    mid = n // 2
    i = 0
    s = Stack()

    while i < mid:
        # Copy the first half of the string onto the stack.
        s.push(temp[i])
        i += 1

    if n % 2 == 0:
        # String is even in length - move to next character
        i = mid
    else:
        # String is odd in length - skip over middle character
        i = mid + 1

    while palindrome and i < n:
        # Walk through the last half of the string, comparing it to the stack
        # contents
        if temp[i] != s.pop():
            palindrome = False
        else:
            i += 1
    return palindrome


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
    n = len(opstring)
    m = len(values_in)
    stack = Stack()  # The processing stack.
    values_out = []
    i = 0
    j = 0

    # Process until one of two inputs is empty.
    while values_out is not None and i < n:
        if opstring[i] == 'S'and j < m:
            # Perform a push if values_in data still available.
            stack.push(values_in[j])
            j += 1
        elif opstring[i] == 'X' and not stack.is_empty():
            # Pop data if available and add to the output list.
            values_out.append(stack.pop())
        else:
            # Error - no input data or stack data to act on.
            values_out = None
        # Move to the next operator and value
        i += 1

    if j < m:
        # Error - opstring is exhausted but data remains.
        values_out = None
    return values_out
