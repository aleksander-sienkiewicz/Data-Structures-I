"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-03-26"
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
from math import log, floor
from List_linked import List



class Sorts:
    """
    -------------------------------------------------------
    Defines a number of linked sort operations.
    Uses class attribute 'swaps' to determine how many times 
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  # Tracks swaps performed.

    # The Sorts

    @staticmethod
    def selection_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Selection Sort algorithm.
        Finds maximum value each pass.
        Use: selection_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (List)
        Returns:
            None
        -------------------------------------------------------
        """
        notSorted= a._front
        a._front= None
        #
        while notSorted is not None:
            maxprev= None
            maxnode= notSorted
            previous= notSorted
            current= maxnode._next

            while current is not None:
                
                if current._value> maxnode._value:
                    maxprev= previous
                    maxnode= current
                previous= current
                #
                current= current._next
            Sorts.swaps+= 1

            if maxprev is None:
                notSorted= maxnode._next
            else:
                maxprev._next= maxnode._next
            #
            maxnode._next= a._front
            a._front= maxnode
            
        return()

    @staticmethod
    def bubble_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Bubble Sort algorithm.
        Use: bubble_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        complete= False
        last= None

        while not complete:
            complete= True
            previous= None
            current= a._front
            swapped= a._front

            while current is not last and current._next is not None:

                if current._value> current._next._value:
                    complete= False
                    Sorts.swaps+= 1
                    a._swap(previous, current)
                    swapped= current
                    if previous is None:
                        previous= a._front
                    else:
                        previous= previous._next
                else:
                    previous= current
                    current= current._next
            last= swapped
        return

    @staticmethod
    def comb_sort(a):
        """
        -------------------------------------------------------
        Sorts an List using the Comb Sort algorithm.
        Use: comb_sort(a)
        -------------------------------------------------------
        Parameters:
          a - a linked list of comparable elements (?)
        Returns:
          None
        -------------------------------------------------------
        """
        n= len(a)

        if n> 0:
            gap= n
            complete= False

            while gap> 1 or not complete:
                complete= True
                previous= None
                current= a._front
                gap= int(gap / 1.3)

                if gap< 1:
                    gap= 1

                i= 0
                prevfar= current
                far= current._next
                #
                while i< gap- 1 and far is not None:
                    prevfar= far
                    far= far._next
                    i+= 1

                while current is not None and far is not None:
                    if current._value> far._value:
                        Sorts.swaps+= 1
                        a._swap(previous, prevfar)
                        complete= False
                    prevfar= far
                    far= far._next
                    previous= current
                    current= current._next
                    
        return()

    @staticmethod
    def insertion_sort(a):
        """
        -------------------------------------------------------
        Sorts a linked list using the Insertion Sort algorithm.
        Use: insertion_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (?)
        Returns:
            None
        -------------------------------------------------------
        """
        # Split the list into the sorted (_front) and unsorted parts.
        unsorted = a._front
        a._front = None

        # Go through each node in the unsorted list and insert it into the
        # proper position in the sorted list.
        while unsorted is not None:
            # Isolate the first node of the unsorted list.
            node = unsorted
            unsorted = unsorted._next
            # Find the proper place for the new node in the sorted so far list.
            # (Very similar to priorityQueue insertion.)
            previous = None
            current = a._front

            while current is not None and current._value < node._value:
                previous = current
                current = current._next

            # Insert node into the proper place in the sorted list.
            Sorts.swaps += 1

            if previous is None:
                node._next = a._front
                a._front = node
            else:
                node._next = current
                previous._next = node
        return

    @staticmethod
    def merge_sort(a):
        if a._count >= 2:
            # Split the list only if there are at least two elements.
            # Generate the left and right lists.
            left, right = Sorts._merge_split(a)
            # Sort the left list.
            Sorts.merge_sort(left)
            # Sort the right list.
            Sorts.merge_sort(right)
            # Merge the left and right lists back into a.
            Sorts._merge(a, left, right)
        return

    @staticmethod
    def _merge_split(source):
        # Split the list by count.
        count = source._count // 2
        curr = source._front

        for _ in range(count - 1):
            curr = curr._next

        # Define the left list.
        left = List()
        left._front = source._front
        left._rear = curr
        left._count = count
        # Define the right list.
        right = List()
        right._front = curr._next
        right._rear = source._rear
        right._count = source._count - count
        # Break the link between the two lists.
        left._rear._next = None
        # Empty the source list.
        source.clear()
        return left, right

    @staticmethod
    def _merge(target, left, right):
        # Traverse left and right appending larger value to rear of target.
        while left._front is not None and right._front is not None:

            if left._front._value <= right._front._value:
                target._move_front_to_rear(left)
            else:
                target._move_front_to_rear(right)

        # Append the remaining list - O(1) operation.
        if left._front is not None:
            target._append_list(left)
        elif right._front is not None:
            target._append_list(right)
        return

    @staticmethod
    def quick_sort(a):
        if a._front is not None:
            # Partition the list into three with respect to pivot value.
            lesser, equals, greater = Sorts._partition(a)
            Sorts.quick_sort(lesser)
            Sorts.quick_sort(greater)
            # Put all three lists back together in order.
            if lesser._front is not None:
                a._append_list(lesser)
            a._append_list(equals)
            if greater._front is not None:
                a._append_list(greater)
        return

    @staticmethod
    def _partition(source):
        lesser = List()
        greater = List()
        equals = List()
        pivot = source._front
        # Move this first node to the equals list.
        equals._move_front_to_rear(source)

        while source._front is not None:
            # Process the remaining nodes with respect to the pivot node.
            if pivot._value > source._front._value:
                lesser._move_front_to_rear(source)
            elif pivot._value < source._front._value:
                greater._move_front_to_rear(source)
            else:
                equals._move_front_to_rear(source)
        return lesser, equals, greater

    @staticmethod
    def to_array(a):
        """
        -------------------------------------------------------
        Copies list values to a Python list.
        Use: values = to_array(a)
        -------------------------------------------------------
        Parameters:
            a - a linked list of comparable elements (?)
        Returns:
            returns
            values - the contents of a in a Python list.= (list of ?)
        -------------------------------------------------------
        """
        values = []
        cur = a._front

        while cur is not None:
            values.append(cur._value)
            cur = cur._next
        return(values)

    @staticmethod
    def sort_test(a):
        """
        -------------------------------------------------------
        Determines whether a linked list is is_sorted or not.
        Use: sort_test(a)
        -------------------------------------------------------
        Parameters:
          a - a linked list of comparable elements (?)
        Returns:
          returns:
          is_sorted - True if contents of a are sorted, False otherwise.
        -------------------------------------------------------
        """
        is_sorted = True
        cur = a._front

        while is_sorted and cur is not None and \
                cur._next is not None:

            if cur._value <= cur._next._value:
                cur = cur._next
            else:
                is_sorted = False
        return(is_sorted)
    
    #assignment #10
    @staticmethod
    def radix_sort(a):
        """
        -------------------------------------------------------
        Performs a base 10 radix sort.
        Use: radix_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a List of base 10 integers (List)
        Returns:
            None
        -------------------------------------------------------
        """
        
        
        if len(a)> 0:
            maxDigit= floor(log(max(a),10)+ 1)
            bucket= []
            #
            for _ in range(10):
                bucket.append(List())
                #
            for i in range(maxDigit):
                while not a.is_empty():
                    currentDigit= a._front._value%((10 ** i)*10)//(10 ** i)
                    bucket[currentDigit]._move_front_to_rear(a)
                    #
                for j in bucket:
                    if not j.is_empty():
                        a._append_list(j)
                        
                        
        return()