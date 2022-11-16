"""
Author: Marshall Jones
File: setinterface.py

"""

# import statements
from abstractSet import AbstractSet
from linkedBag import LinkedBag

class LinkedSet(AbstractSet, LinkedBag):
    """"""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        LinkedBag.__init__(self, sourceCollection)
        
    
    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        # LinkedBag.__iter__(self) # this line wouldn't run
        # super(LinkedBag, self).__iter__() # neither would this one
        cursor = self._items
        while cursor != None:
            yield cursor.data
            cursor = cursor.next


    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        LinkedBag.clear(self)

    def add(self, item):
        """Adds item to self."""
        if item not in self:
            LinkedBag.add(self, item)

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        postcondition: item is removed from self."""
        LinkedBag.remove(self, item)