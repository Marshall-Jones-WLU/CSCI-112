"""
File: arrayPriorityQueue.py
Author: Marshall Jones
"""

from .node import Node
from .arrayQueue import ArrayQueue

class ArrayPriorityQueue(ArrayQueue):
    """A link-based priority queue implementation."""


    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        super().__init__(sourceCollection)


    def add(self, item):
        
        """Adds item to its proper place in the queue."""
        # Check array memory here and increase it if necessary
        if len(self) == len(self._items):
            self.resize(2)
        
        if self.isEmpty() or item >= self._rear:
            # New item goes to rear
            super().add(item)
        else:
            # find the index of the first item >= new item
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            # open up a slot for the item to go into
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i-1]
            # insert the new item and update the size
            self._items[targetIndex] = item
            self._size += 1
            
            
