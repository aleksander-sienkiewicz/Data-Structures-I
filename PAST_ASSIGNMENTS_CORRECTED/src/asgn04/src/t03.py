"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-02-09"
-------------------------------------------------------
"""
# Imports
from Queue_array import Queue
from functions import queue_split_alt

# Constants
SIZE = 12
SEP = "-" * 40


def test_queue_split_alt():
    # Imports

    from queues import queue_split_alt

    # Constants
    A1 = [1, 0, 2, 3, 4]

    print("Testing 'queue_combine'")
    print()

    source = Queue()

    for v in A1:
        source.insert(v)

    print("Contents of source:")

    for v in source:
        print(v, end=", ")
    print()
    print(SEP)
    print("split_alt")
    print()
    target1, target2 = queue_split_alt(source)

    print("Contents of target1:")

    for v in target1:
        print(v, end=", ")
    print()
    print()

    print("Contents of target2:")

    for v in target2:
        print(v, end=", ")
    print()
    print()

    print("Testing 'Queue.split_alt'")
    print()

    source = Queue()

    for v in A1:
        source.insert(v)

    print("Contents of source:")

    for v in source:
        print(v, end=", ")
    print()
    print(SEP)
    print("split_alt")
    print()
    target1, target2 = source.split_alt()

    print("Contents of target:")

    print("Contents of target1:")

    for v in target1:
        print(v, end=", ")
    print()
    print()

    print("Contents of target2:")

    for v in target2:
        print(v, end=", ")
    print()
    print()
    print("Done")
    print()


test_queue_split_alt()
