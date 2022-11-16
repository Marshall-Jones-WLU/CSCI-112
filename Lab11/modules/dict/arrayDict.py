"""
File: arraydict.py

Marshall Jones

An array-based dictionary.
"""

from .abstractDict import AbstractDict, Entry

class ArrayDict(AbstractDict):
    """Represents an array-based dictionary."""

    def __init__(self, keys = None, values = None):
        """Initializes the collection."""
        self._items = list()
        super().__init__(keys, values)

    def __iter__(self):
        """Serves up the keys in the dictionary."""
        cursor = 0
        modCount = self.getModCount()
        while cursor < len(self):
            yield self._items[cursor].key
            if modCount != self.getModCount():
                raise AttributeError("Mutations not allowed in a for loop")
            cursor += 1    

    def __getitem__(self, key):
        """Precondition: the key is in the dictionary.
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""
        index = self._index(key)
        if index == -1: raise KeyError("Missing: " + str(key))
        return self._items[index].value

    def __setitem__(self, key, value):
        """If the key is not in the dictionary,
        adds the key and value to it.
        Othwerise, replaces the old value with the new
        value."""
        index = self._index(key)
        if index == -1:
            self._items.append(Entry(key, value))
            self._size += 1
            self._modCount += 1
        else:
            self._items[index].value = value


    def pop(self, key, defaultValue = None):
        """Removes the key and returns the associated value if the
        key in in the dictionary, or returns the default value
        otherwise."""
        index = self._index(key)
        if index == -1:
            return defaultValue
        self._size -= 1
        
        return self._items.pop(index).value

    def _getEntry(self, key):        
        """Helper method to obtain the entry rather than the value associated with a key."""
        index = self._index(key)
        if index == -1:
            return None
        else:
            return self._items[index]

    def _index(self, key):
        """Helper method for key search."""
        index = 0
        for entry in self._items:
            if entry.key == key:
                return index
            index += 1
        return -1
