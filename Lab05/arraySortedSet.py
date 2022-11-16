"""
Author: Marshall Jones
File: setinterface.py

"""

# import statements
from arraySet import ArraySet
from arraySortedBag import ArraySortedBag

class ArraySortedSet(ArraySortedBag, ArraySet):
    """"""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        super().__init__(sourceCollection)


    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        if item not in self:
            super().add(item)
