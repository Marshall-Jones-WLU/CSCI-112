"""
File: abstractDict.py

Marshall Jones

Common data and method implementations for dictionaries.
"""
from ..utils.abstractCollection import AbstractCollection

class AbstractDict(AbstractCollection):
    """Represents an abstract dictionary."""

    def __init__(self, keys = None, values = None):
        """Initialize the collection."""
        super().__init__(None)
        
        if keys:
            valueIter = iter(values)
            for key in keys:
                self[key] = next(valueIter)

    def __str__(self):
        return " {" + ", ".join(map(lambda entry: str(entry.key) + \
               ": " + str(entry.value), self.entries())) + "}"

    # Exercise
    def get(self, key, defaultValue = None):
        """Returns the associated value if the key is in the
        dictionary, or returns the default value otherwise."""
        if key in self.keys():
            return self[key]
        else:
            return defaultValue

    # Exercise   
    def add(self, entry):
        """Adds the values contained in an Entry parameter to the current dictionary."""
        self[entry.key] = entry.value
        
    # Exercise
    def keys(self):
        """Returns an iterator on the list of keys in the dictionary."""
        return iter(self)

    # Exercise
    def values(self):
        """Returns an iterator on the list of values in the dictionary."""
        return map(lambda key: self[key], self)

    # Exercise
    def entries(self):
        """Returns a iterator on the list of entries in the dictionary."""
        return map(lambda key: Entry(key, self[key]), self)

    def __add__(self, other):
        """Returns a dictionary containing the entries of self and
        otherDict.  When keys are equal, the value in otherDict replaces
        the value in self."""
        clone = type(self)(self.keys(), self.values())
        for item in other.entries():
            clone.add(item)
        return clone

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other:
            return True
        if type(self) != type(other):
            return False
        else:
            for key in self:
                if self[key] != other[key]:
                    return False

    def _getEntry(self, key):
        """Helper method to obtain the entry rather than the value associated with a key."""
        raise NotImplementedError("Abstract class method invoked!")
    
class Entry(object):
    """Represents a dictionary entry.  Supports comparisons by key."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

    def __eq__(self, other):
        if type(self) != type(other): return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other): return False
        return self.key < other.key

    def __le__(self, other):
        if type(self) != type(other): return False
        return self.key <= other.key

    def __hash__(self):
        return hash(self.key)
