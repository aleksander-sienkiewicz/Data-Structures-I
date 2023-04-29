"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-02-06"
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
#Binary dearch(split into half reapeating)    
def _binary_search(self, element):
    """
    -------------------------------------------------------
    Searches for the first occurrence of element in the sorted list.
    Private helper method - used only by other ADT methods.
    Use: i = self._binary_search(key)
    -------------------------------------------------------
    Parameters:
        element - a data element to search for (?)
    Returns:
        i - the index of the first occurrence of the element in
            the list, -1 if the element is not found. (int)
    -------------------------------------------------------
    """
    # Index of beginning of subarray to search.
    low = 0
    # Index of end of subarray to search.
    high = self._count - 1

    while low < high:
        # Find the middle of the current subarray.
        # (avoids overflow on large values vs (low + high)//2
        mid = (high - low) // 2 + low

        if element > self._values[mid] :
            # Search the right subarray.
            low = mid + 1
        else:
            # Default: search the left subarray.
            high = mid

    # Deferred test for equality.
    if low == high and self._values[low] == element:
        i = low
    else:
        i = -1
    return i

#insert into sorted list->must find last occurence of a given value 
def insert(self, value):
    """
    -------------------------------------------------------
    Inserts value at the proper place in the sorted list.
    Must be a stable insertion, i.e. consecutive insertions
    of the same value must keep their order preserved.
    Use: sl.insert(value)
    -------------------------------------------------------
    Parameters:
        value - a data element (?)
    Returns:
        None
    -------------------------------------------------------
    """
    # Index of beginning of subarray to search.
    low = 0
    # Index of end of subarray to search.
    high = len(self._values) - 1

    while low <= high:
        # Find the middle of the current subarray.
        # (avoids overflow on large values vs (low + high)//2
        mid = (high - low) // 2 + low

        if self._values[mid] > value:
            # search the left subarray.
            high = mid - 1
        else:
            # Default: search the right subarray.
            low = mid + 1
    self._values.insert(low, value)
    return