"""
Author: Marshall Jones
File: arraySortedbag.py
"""

# import statements
from arrayBag import ArrayBag

class ArraySortedBag(ArrayBag):
    """An array-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        super().__init__(sourceCollection)


    # Accessor methods
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise. This method 
        overrides the equality method in 
        abstractBag for improved efficiency"""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in range(len(self)):
            if self._items[item] != other._items[item]:
                return False
        return True
    
    def __contains__(self, item):
        """Returns True if item is in the bag, and False Otherwise.
        It uses a binary search method since the bag is sorted"""
        left = 0
        right = len(self) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if self._items[midpoint] == item:
                return True
            elif self._items[midpoint] > item:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return False


    # Mutator methods
    def add(self, item):
        """Adds item to self."""
        # if the array is empty or if the new item is larger than the item in the last position:
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            super().add(item)

        else: # Search for the first item >= new item
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            # create an empty slot for the new item
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i-1]
            # insert the new item and update the size
            self._items[targetIndex] = item
            self._size += 1
        
