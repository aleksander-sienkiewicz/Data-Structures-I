"""
-------------------------------------------------------
CP164 Spring 2021: Assignment 1
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 OC1
__updated__ = "2022-01-19"
-------------------------------------------------------
"""
# Constants
VOWELS = 'aeiouAEIOU'
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CIPHERTEXT = 'AVIBROWNZCEFGHJKLMPQSTUXYD'
ALPHA_SIZE = len(ALPHA)


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    i = 0

    while i < len(values):
        j = i + 1

        while j < len(values):
            # Remove copy of value at index i from remainder of list
            if values[j] == values[i]:
                values.pop(j)
            else:
                j += 1
        i += 1
    return

    '''
    ALTERNATE

    i = 0

    while i < len(values):
        j = 0

        while j < i and values[j] != values[i]:
            # Look for value in already cleaned part of list
            j += 1
        if j < i:
            values.pop(i)
    return
    '''
    '''
    ALTERNATE

    i = 0

    while i < len(values):

        if values[i] in values[:i]:
            # Look for value in already cleaned part of list
            # NOTE: values[:i] creates copy of part of list
            values.pop(i)
        else:
            i += 1
    return
    '''


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    out = ''

    for c in s:
        if c.lower() not in VOWELS:
            # Concatenates only non-vowels to the return string.
            out += c
    return out


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u = 0
    l = 0
    d = 0
    w = 0
    r = 0

    for line in fv:

        for c in line:
            if c.isalpha() and c.isupper():
                u += 1
            elif c.isalpha() and c.islower():
                l += 1
            elif c.isdigit():
                d += 1
            elif c.isspace():
                w += 1
            else:
                r += 1
    return u, l, d, w, r


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    if year % 400 == 0:
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
    else:
        leap_year = False
    return leap_year


def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome = True
    i = 0
    j = len(s) - 1

    while i < j and palindrome:

        if not s[i].isalpha():
            i += 1
        elif not s[j].isalpha():
            j -= 1
        elif s[i].lower() != s[j].lower():
            palindrome = False
        else:
            i += 1
            j -= 1
    return palindrome


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    md = 0
    n = len(a)
    i = 1

    while i < n:
        v = abs(a[i] - a[i - 1])

        if v > md:
            md = v
        i += 1
    return md


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    a must be unchanged.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
    Returns:
        b - the transposed matrix (2D list of int/float)
    -------------------------------------------------------
    """
    b = []
    rows = len(a)
    cols = len(a[0])

    for j in range(cols):
        row = []

        for i in range(rows):
            row.append(a[i][j])
        b.append(row)
    return b


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = a[0][0]
    large = small
    total = 0

    for row in a:
        for col in row:
            total += col

            if col < small:
                small = col
            elif col > large:
                large = col

    rows = len(a)
    cols = len(a[0])
    average = total / (rows * cols)
    return small, large, total, average


def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    if len(word) > 0:
        if word[0] in VOWELS:
            # word begins with a vowel.
            pl = word + "way"
        else:
            if word[0].isupper():
                word = word[0].lower() + word[1:]
                upper = True
            else:
                upper = False
            # Find all consonants in front of string.
            # Treat "y" as a vowel in this case.
            i = 1

            while word[i] not in (VOWELS + "y"):
                i += 1
            # Construct the pig latin version of word.
            # Last part [i:] + first part [:i] + "ay".
            pl = word[i:] + word[:i] + "ay"

            if upper:
                pl = pl[0].upper() + pl[1:]
    else:
        pl = ""
    return pl
