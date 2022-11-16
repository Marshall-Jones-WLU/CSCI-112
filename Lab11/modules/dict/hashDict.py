"""
File: hashDict.py

Marshall Jones

A hash-based dictionary.
"""

from .abstractDict import AbstractDict, Entry
from ..utils.node import Node
from ..utils.arrays import Array

class HashDict(AbstractDict):
    """Represents a hash-based dictionary."""

    DEFAULT_CAPACITY = 10
    MAX_LOAD_FACTOR = 0.5
    MIN_LOAD_FACTOR = 0.1

    def __init__(self, sourceKeys = None, sourceValues = None,
                 capacity = DEFAULT_CAPACITY):
        """Sets the initial state of self, which includes the
        contents of  source keys and source values, if they
        are present."""
        self._array = Array(capacity)
        self._foundEntry = self._priorEntry = None
        self._index = -1
        super().__init__(sourceKeys, sourceValues)

    # Exercise
    def __iter__(self):
        """Serves up the keys in the dictionary."""
        modCount = self.getModCount()
        for i in range(len(self._array)):
            probe = self._array[i]
            while probe != None:
                yield probe.data.key
                probe = probe.next
            
            if modCount != self.getModCount():
                raise AttributeError("Mutations not allowed in a for loop")
        

    # Exercise
    def __getitem__(self, key):
        """Precondition: the key is in the dictionary. Resizes
        when load factor is > MAX_LOAD_FACTOR
        Raises: a KeyError if the key is not in the dictionary.
        Returns the value associated with the key."""        
        if key in self:
            return self._foundEntry.data.value
        else:
            raise KeyError("Missing: " + str(key))

        if self.loadFactor() > self.MAX_LOAD_FACTOR:
            self._rehash(2)

    # Exercise
    def __setitem__(self, key, value):
        """If the key is not in the dictionary,
        adds the key and value to it.
        Othwerise, replaces the old value with the new
        value. Resizes when load factor is > MAX_LOAD_FACTOR"""
        if key in self:
            self._foundEntry.data.value = value
        else:
            newNode = Node(Entry(key, value), self._array[self._index])
            self._array[self._index] = newNode
            self._size += 1
        
        if self.loadFactor() > self.MAX_LOAD_FACTOR:
            self._rehash(2)

       
    def _rehash(self, resizeFactor):
        
        if int(len(self._array) * resizeFactor) >= HashDict.DEFAULT_CAPACITY:
            tempArray = self._array
            
            self._array = Array(int(len(self._array) * resizeFactor))
            self._size = 0
            
            for item in tempArray:
                probe = item
                while probe:
                    self[probe.data.key] = probe.data.value
                    probe=probe.next
        
    
    def _getEntry(self, key):
        """Helper method to obtain the entry rather than the value associated with a key."""
        if key in self:
            return self._foundEntry.data
        return None
        
    def loadFactor(self):
        """Returns the load factor of the current hash size."""
        return len(self) / len(self._array)


    # Exercise
    def pop(self, key, defaultValue = None):
        """Removes the key and returns the associated value if the
        key is in the dictionary, or returns the default value
        otherwise. Resizes when load factor is < MIN_LOAD_FACTOR"""
        if self._index == -1:
            return defaultValue
        
        if not key in self:
            return defaultValue
        else:
            value = self._foundEntry.data.value
            if self._priorEntry == None:
                self._array[self._index] = self._foundEntry.next
            else:
                self._priorEntry.next = self._foundEntry.next
        self._size -= 1
        if self.loadFactor() < self.MIN_LOAD_FACTOR:
            self._rehash(0.5)
        return value

    def clear(self):
        """Makes self become empty."""
        self.resetSizeAndModCount()
        self._array = Array(HashDict.DEFAULT_CAPACITY)
        self._foundEntry = self._priorEntry = None
        self._index = -1


    def __contains__(self, key):
        """Returns True if the key in in the dictionary
        or False otherwise."""
        # hashIndex = hash(key) % len(self._array)
        self._index = abs(hash(key)) % len(self._array)
        
        # self._foundEntry = self._array[hashIndex]
        self._foundEntry = self._array[self._index]
        self._priorEntry = None
        while self._foundEntry:
            if self._foundEntry.data.key == key:
                return True
            else:
                self._priorEntry = self._foundEntry
                self._foundEntry = self._foundEntry.next
                
        self._foundEntry = self._priorEntry = None
        
        return False

