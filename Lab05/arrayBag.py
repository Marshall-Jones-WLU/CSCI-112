"""
Author: Marshall Jones
File: arraybag.py
"""

# import statements
from arrays import Array
from abstractBag import AbstractBag

class ArrayBag(AbstractBag):
    """An array-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        self._items = Array(ArrayBag.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)
        

    # Mutator methods
    def clear(self): # code for LinkedBag is different
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayBag.DEFAULT_CAPACITY) 
    
    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        if len(self) == len(self._items):
            self.resize(2)
        
        self._items[len(self)] = item
        self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the index of the target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1 # finds the index of the target item to be removed
        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # Decrement logical size
        self._size -= 1
        # Check array memory here and decrease it if necessary
        if len(self) <= len(self._items)/4:
            self.resize(.5)
        
    def resize(self, sizeFactor):
        """Copies over the values in self._items into a new array resized 
        by the sizeFactor parameter"""
        newSize = int(len(self) * sizeFactor) # establish the new size
        if newSize < ArrayBag.DEFAULT_CAPACITY:
            newSize = ArrayBag.DEFAULT_CAPACITY
        
        tempArray = Array(newSize) # create a new empty array

        for i in range(self._size):
            # add items from previous array to the resized array
            tempArray[i] = self._items[i]
        
        self._items = tempArray