"""
-------------------------------------------------------
Array versions of various sorts.
-------------------------------------------------------
Author: Aleksander Sienkiewicz
ID:     210222490
Email:  sien2490@mylaurier.ca
__updated__ = "2022-04-06"
-------------------------------------------------------
"""


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of array-based sort operations.
    -------------------------------------------------------
    """
    # The Sorts

    @staticmethod
    def radix_string_sort(strings):
        """
        -------------------------------------------------------
        Performs a string radix sort.
        Use: Sorts.radix_string_sort(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns‌​‌​‌‌​‌​:
            None
        -------------------------------------------------------
        """

        # your code here
        prev_count=0
        count=0           
        new_list=[]
        for i in strings:
                for j in i:
                    count+=1
                    if count>prev_count:
                        maxlen=count
                        prev_count=count
                        new_list.append(i)
        strings=new_list
        return

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    @staticmethod
    def is_sorted_alpha(strings):
        """
        -------------------------------------------------------
        Determines whether an array is sorted or not.
        Use: srtd = Sorts.is_sorted(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns‌​‌​‌‌​‌​:
            srtd - True if contents of strings are sorted,
                False otherwise (boolean)
       -------------------------------------------------------
        """
        srtd = True
        n = len(strings)
        i = 0

        while srtd and i < n - 1:

            if strings[i].lower() <= strings[i + 1].lower():
                i += 1
            else:
                srtd = False
        return srtd
