"""
Author: YOUR NAME GOES HERE
File: testbag.py
A tester program for bag implementations.
"""

from arrayBag import ArrayBag
from linkedBag import LinkedBag
from arraySortedBag import ArraySortedBag
from linkedSortedBag import LinkedSortedBag
from abstractBag import AbstractBag

def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973]
    print("The list of items added is:", lyst)
    b1 = bagType(lyst)
    print("Length, expect 3:", len(b1))
    print("Expect the bag's string:", b1)
    print("2013 in bag, expect True:", 2013 in b1)
    print("2012 in bag, expect False:", 2012 in b1)
    print("Expect the items on separate lines:")
    for item in b1:
        print(item)
    b1.clear()
    print("Bag cleared, expect {}:", b1)
    b1.add(25)
    b1.remove(25)
    print("Add and remove 25, expect {}:", b1)
    b1 = bagType(lyst)
    b2 = bagType(b1)
    print("Equal to a clone, expect True:", b1 == b2)
    print("Identical to a clone, expect False:", b1 is b2)
    print("Concatenate with a clone, expect two of each item:", b1 + b2)
    for item in lyst:
        b1.remove(item)
    print("Remove each item, expect {}:", b1)
    print("Crash with index error, or length of " + \
          str(ArrayBag.DEFAULT_CAPACITY * 3))
    for item in range(ArrayBag.DEFAULT_CAPACITY * 3):
        b1.add(item)
    print(len(b1))

def testResize():
    """Tests the resizing of an array-based bag,
    when space is wasted."""
    bag = ArrayBag(range(100))
    print("Added 100 items, length of bag =", len(bag))
    print("Length of array =", len(bag._items))
    for item in range(76):
        bag.remove(item)
    print("Removed 76 items, length of bag =", len(bag))
    print("Length of array =", len(bag._items))
    for item in range(76, 100):
        bag.remove(item)
    print("Removed remaining items, length of bag =", len(bag))
    print("Length of array =", len(bag._items))

def testIter(bagType):
    """Tests the catching of mutation errors in the iterator."""
    print("Testing the iterator to detect mutations:")
    bag = bagType(range(10))
    print("Expect all items on separate lines:")
    for item in bag:
        print(item)
    print("Expect an exception on add within a loop:")
    for item in bag:
        bag.add(100)
##    print("Expect an exception on remove within a loop:")
##    for item in bag:
##        bag.remove(3)
##    print("Expect an exception on clear within a loop:")
##    for item in bag:
##        bag.clear()
    
    
def main():
    """STarting point for the application."""
    # testResize()
    # test(ArrayBag) #working
    # test(LinkedBag) #working
    # test(ArraySortedBag) #working
    # test(LinkedSortedBag) #working

    # testIter(ArrayBag)
    # testIter(LinkedBag)
    # testIter(ArraySortedBag)

if __name__ == "__main__":
    main()
