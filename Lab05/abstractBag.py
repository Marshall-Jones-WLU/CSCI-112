"""
Author: Marshall Jones
File: abstractBag.py
"""

# import statements
from abstractCollection import AbstractCollection

class AbstractBag(AbstractCollection):

    # Constructor
    def __init__(self, sourceCollection = None):
        super().__init__(sourceCollection)


    # Accessor methods
    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"
        
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise. Overridden in 
        sorted bags for improved efficiency."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True
