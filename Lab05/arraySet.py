"""
Author: Marshall Jones
File: setinterface.py

"""

# import statements
from abstractSet import AbstractSet
from arrayBag import ArrayBag

class ArraySet(AbstractSet, ArrayBag):
    """"""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        ArrayBag.__init__(self, sourceCollection)


    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        ArrayBag.clear(self)

    def add(self, item):
        """Adds item to self."""
        if item not in self:
            ArrayBag.add(self, item)

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        postcondition: item is removed from self."""
        ArrayBag.remove(self, item)