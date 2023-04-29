"""
-------------------------------------------------------
a01 functions
-------------------------------------------------------
Author:  Aleksander Sienkiewicz
ID:      210222490
Email:   sien2490@mylaurier.ca
__updated__ = "2022-01-12"
-------------------------------------------------------
"""
# Imports
from pickle import TRUE, FALSE

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
    #t01
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
    list=[]
    i=0
    while i <len(values):
        if values[i]not in list:
            list.append(values[i])
        else:
            values.pop(i)
            i-=1
        i+=1
        
    return 
#t02
VOWELS=["a","e","i","o","u"]
def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    word=""
    for i in s:
        if i.lower()not in VOWELS:
            word+=i
    return word
#t03
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
    u,l,d,w,r=0,0,0,0,0
    
    for line in fv:
        for c in line:
            if c.isspace():
                w+=1
            elif c.isupper():
                u+=1
            elif c.islower():
                l   +=1
            elif c.isdigit():
                d+=1
            else:
                r+=1
    return(u,l,d,w,r)
#t04
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
    y = year
    if y %4==0:
        if y %100==0:
            if y % 400==0:
                leapYR=True
            else:
                leapYR=False
        else:
            leapYR=True
    else:
        leapYR=False
        
    return leapYR
#t05
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
    i=0
    s=s.lower()
    pal=True
    while i<len(s) and pal==True:
        if s[i]!=s[(i+1)*-1]:
            pal=False 
        i+=1
        
    return pal
#t06
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
    high=0
    for i in range((len(a)-1)):
        value=abs(a[i]-a[i+1])
        if value>high:
            high=value
    return high
#t07
def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b=[]
    for i in range(len(a[0])):
        list=[]
        for j in range(len(a)):
            list.append(a[j][i])
        b.append(i)

    return b
#t08
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
    small=a[0][0]
    large=a[0][0]
    total=0
    average=0
    for i in a:
        for val in i:
            if val<small:
                small = val
            elif val > large:
                large = val
            total+= val
            average+=1
    average = total/average
    return (small, large, total, average)
#t09
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
    pl = ''
    if word[0].lower() in VOWELS == True:
        pl = word+'way'
    else:
        capitalize=False
        notComplete=True
        index=0
        word1=''
        if word[0].isupper():
            capitalize=True
        while index<len(word) and notComplete==True:
            if word[index] in VOWELS==True:
                notComplete=False
            else:
                word1+=word[index].lower()
                index+=1
        pl=word[index:]+word1+'ay'
        if capitalize == True:
            pl=pl.capitalize()
        
    return pl
