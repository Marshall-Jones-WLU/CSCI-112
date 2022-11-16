"""
Author: Marshall Jones
File: abstractSet.py
"""

class AbstractSet(object):

    # Constructor
    def __init__(self, sourceCollection = None):
        pass

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1
    
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other): return False
        if len(self) != len(other): return False

        # otherIter = iter(other)

        for item in self:
            if not item in other:
            # if item != next(otherIter):
                return False
        return True

    
    # Set-specific methods
    def __or__(self, other):
        """Returns the union of self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return "{" + ", ".join(map(str, result)) + "}"

    def __and__(self, other):
        """Returns the intersection of self and other."""
        result = type(self)(self)
        result.clear()
        for item in self:
            if item in other:
                result.add(item)
        return "{" + ", ".join(map(str, result)) + "}"

    def __sub__(self, other):
        """Returns the difference of self and other."""
        result = type(self)(self)
        result.clear()
        # print(self)
        # print(other)
        for item in self:
            # print(item)
            if not item in other:
                result.add(item)
        return "{" + ", ".join(map(str, result)) + "}"