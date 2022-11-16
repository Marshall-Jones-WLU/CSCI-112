"""
Author: Marshall Jones
File: abstractCollection.py
"""

class AbstractCollection(object):

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)


    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def count(self, target):
        """Counts the amount of targets currently contained in self."""
        counter = 0
        for nextTarget in self:
            if nextTarget == target:
                counter += 1
        return counter
    
    def __len__(self):
        """Returns the number of items in self."""
        return self._size

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result