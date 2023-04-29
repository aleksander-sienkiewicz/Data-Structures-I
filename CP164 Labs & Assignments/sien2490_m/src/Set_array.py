"""
-------------------------------------------------------
Set_array.py
Array version of the Set ADT.
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-02-12"
-------------------------------------------------------
The PyDev module 'test_Set.py' contains a few sample tests for some of the Set
methods. The method 'print_set' is a testing method that shows you the complete
contents of a Set object in human-readable form and can also be used for testing.
-------------------------------------------------------
"""
# pylint: disable=protected-access

from copy import deepcopy


class Set:
    """
    -------------------------------------------------------
    Data structure that contains a set of unique values,
        i.e. no values are repeated in a Set.
    Values stored in fixed-length Python list like in the Circular Queue.
        Do not use Python list methods that change the length of the list:
            append, insert, remove, pop, extend, delete
    Empty slots contain None.
    -------------------------------------------------------
    Examples of Set attributes:
        _values = [None, None, None, None], _capacity = 4, _count = 0, _first = 0
        _values = [1, None, 9, None],       _capacity = 4, _count = 2, _first = 1
        _values = [1, None, 9, 3],          _capacity = 4, _count = 3, _first = 1
        _values = [1, 4, None, 3],          _capacity = 4, _count = 3, _first = 2
        _values = [1, 4, 9, 3],             _capacity = 4, _count = 4, _first = None
    -------------------------------------------------------
    """
    # Default maximum size when capacity parameter is not provided
    DEFAULT_SIZE = 10

    def __init__(self, capacity=DEFAULT_SIZE):
        """
        -------------------------------------------------------
        Initializes an empty Set.
        Use: target = Set(capacity)
        Use: target = Set()  # uses DEFAULT_SIZE
        -------------------------------------------------------
        Parameters:
            capacity - maximum size of the set (int > 0)
        Returns‌‌​​​‌‌‌​:
            a new Set object (Set)
        -------------------------------------------------------
        """
        # Maximum capacity of Python list to store data.
        self._capacity = capacity
        # Python list that stores data - initialized to list of None.
        self._values = [None] * self._capacity
        # First available index for adding values - if None, Set is full.
        self._first = 0
        # Number of unique values in Set. Cannot exceed _capacity.
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty. In an empty set, all slots
        in _values contain None.
        Use: empty = source.is_empty()
        -------------------------------------------------------
        Returns‌‌​​​‌‌‌​:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """

        # your code here
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if source is full. In a full set, no slot
        in _values is None.
        Use: full = source.is_full()
        -------------------------------------------------------
        Returns‌‌​​​‌‌‌​:
            True if source is full, False otherwise.
        -------------------------------------------------------
        """

        # your code here
        return self._count == self._capacity


    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of non-None values in the set.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌‌​​​‌‌‌​:
            the number of values in the set.
        -------------------------------------------------------
        """

        # your code here
        return self._count

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the occurrence of key in the set. Skips over None entries.
        (Private helper method - used only by other ADT methods.)
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns‌‌​​​‌‌‌​:
            i - the index of key in the set, -1 if key is not found (int)
        -------------------------------------------------------
        """
        n = len(self._values)
        i = 0

        while i < n and self._values[i] != key:
            i += 1

        if i == n:
            i = -1
        return i
        # your code here


    def _set_first(self):
        """
        -------------------------------------------------------
        Sets the value of _first, the index of the first location of None
        in _values.
        (Private helper method - used only by other ADT methods.)
        Use: self._set_first()
        -------------------------------------------------------
        Returns‌‌​​​‌‌‌​:
            None
        -------------------------------------------------------
        """
        i=0
        while i !=-1:
            if self._values[i]==None:
                self._first== self._values[i]
                i=-1
            else:
                i+=1
        return
        # your code here

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds value to the set at index _first.
        Use: inserted = source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns‌‌​​​‌‌‌​:
            inserted - True if value was added to source, False otherwise.
                value is added only if value is unique in the set (boolean)
        -------------------------------------------------------
        """
        assert self._first is not None, "Cannot add to a full set"
        inserted=False
        if not value in self._values:
            self._values.append(value)
            inserted=True
        return inserted
        # your code here

    def delete(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in the set that matches key.
        Updates _first.
        Use: value = source.delete(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns‌‌​​​‌‌‌​:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        for i in self._values:
            if i == key:
                value=deepcopy(self._values[i])
                self._values.remove(i)
        return value
        # your code here

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in the set that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns‌‌​​​‌‌‌​:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """ 
        i = self._linear_search(key)

        if i > -1:
            value = deepcopy(self._values[i])
        else:
            value = None
        return value
        # your code here

    def __contains__(self, key):
        """
        -------------------------------------------------------
        Determines if the set contains a value matching key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns‌‌​​​‌‌‌​:
            True if the set contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        i = self._linear_search(key)
        return i > -1

    def maximum(self):
        """
        -------------------------------------------------------
        Returns a copy of the maximum value in the set.
        Use: value = source.maximum()
        -------------------------------------------------------
        Returns‌‌​​​‌‌‌​:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert self._count > 0, "Cannot find maximum of an empty set"

        # your code here
    
        value = deepcopy(self._values[-1])
        return value
    
    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current Set with copies of values that appear
        in both source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based set (Set)
            source2 - an array-based set (Set)
        Returns‌‌​​​‌‌‌​:
            None
        -------------------------------------------------------
        Examples:
            intersection({1,2,3}, {3,2,1}) is {1,2,3}
            intersection({1,2,3}, {4,5,6}) is {}
            intersection({1,2,3,4,5,6}, {0,2,4,6,8}) is {2,4,6}
        -------------------------------------------------------
        """
        assert self._count == 0, "Target Set must be empty"

        # your code here
        i = 0
        j = 0

        while i < len(source1._values) and j < len(source2._values):

            if source1._values[i] < source2._values[j]:
                # Skip the value in source1
                i += 1
            elif source1._values[i] > source2._values[j]:
                # Skip the value in source2
                j += 1
            else:
                # Values are the same - add the value if target is empty
                # or have not already added the value
                if len(self._values) == 0 or self._values[-1] != source1._values[i]:
                    self._values.append(deepcopy(source1._values[i]))
                i += 1
                j += 1
    """
    -------------------------------------------------------
    DO NOT CHANGE THE CODE BELOW THIS LINE
    -------------------------------------------------------
    """

    def print_set(self):
        """
        -------------------------------------------------------
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Prints the contents of a Set in human readable format.
        Use: source.print_set()
        -------------------------------------------------------
        Returns‌‌​​​‌‌‌​:
            None
        -------------------------------------------------------
        """
        print(f"_values:   {self._values}")
        print(f"_capacity: {self._capacity:2d}")
        print(f"_count:    {self._count:2d}")
        print(f"_first:     {self._first:2d}")
        print("----------")
        return

    def __iter__(self):
        """
        -------------------------------------------------------
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the set
        from left to right.
        Use: for v in source:
        -------------------------------------------------------
        Returns‌‌​​​‌‌‌​:
            value - the next value in the set (?)
        -------------------------------------------------------
        """
        for value in self._values:
            if value is not None:
                yield value
