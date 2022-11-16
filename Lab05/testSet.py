"""
File: testset.py
Author: YOUR NAME GOES HERE
A tester program for set implementations.
"""

from arraySet import ArraySet
from linkedSet import LinkedSet
from arraySortedSet import ArraySortedSet

def test(setType):
    """Expects a set type as an argument and runs some tests
    on objects of that type."""
    lyst = [2013, 61, 1973, 1973]
    print("The list of items added is:", lyst)
    s1 = setType(lyst)
    print("Length, expect 3:", len(s1))
    print("Expect the set's string:", s1)
    print("2013 in s1, expect True:", 2013 in s1)
    print("2012 in s1, expect False:", 2012 in s1)
    print("Expect the items on separate lines:")
    for item in s1:
        print(item)
    s1.clear()
    print("Clearing, expect {}:", s1)
    s1.add(25)
    s1.remove(25)
    print("Add and remove 25, expect {}:", s1)
    s1 = setType(lyst)
    s2 = setType(s1)
    print("Clone with ==, expect True:", s1 == s2)
    print("Clone with is, expect False:", s1 is s2)
    s1.clear()
    print("Removed each, expect {}:", s1)
    print("Expect crash with KeyError:")
    s1.remove(99)

def testSetSpecific(setType):
    """Expects a set type as an argument and runs some tests
    on objects of that type with the |, &, and - operators."""
    s1 = setType([2013, 61, 1973, 1973])
    s2 = setType([61, 44, 2013])
    print("s1:", s1, "s2:", s2)
    print("s1 | s2:", s1 | s2)
    print("s1 & s2:", s1 & s2)
    print("s1 - s2:", s1 - s2)
    print("s2 - s1:", s2 - s1)

def main():
    """Starting point for the application."""
    # test(ArraySet) #working
    # test(LinkedSet) #working
    # test(ArraySortedSet) #working

    # testSetSpecific(ArraySet) #working
    # testSetSpecific(LinkedSet) #working
    # testSetSpecific(ArraySortedSet) #working

if __name__ == "__main__":
    main()
