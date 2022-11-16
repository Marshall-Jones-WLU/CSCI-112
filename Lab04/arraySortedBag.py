"""
Author: Marshall Jones
File: arraySortedbag.py
"""

from arrays import Array

class ArraySortedBag(object):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
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

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArraySortedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
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
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY) 

    def add(self, item):
        """Adds item to self."""
        # Check array memory here and increase it if necessary
        if len(self) == len(self._items):
            self.resize(2)
        
        # if the array is empty or if the new item is larger than the item in the last position:
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            self._items[len(self)] = item
            self._size += 1
        else:
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            # create an empty slot for the new item
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i-1]
            # insert the new item and update the size
            self._items[targetIndex] = item
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
            targetIndex += 1
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
        if newSize < ArraySortedBag.DEFAULT_CAPACITY:
            newSize = ArraySortedBag.DEFAULT_CAPACITY
        
        tempArray = Array(newSize) # create a new empty array

        for i in range(self._size):
            # add items from previous array to the resized array
            tempArray[i] = self._items[i]
        
        self._items = tempArray