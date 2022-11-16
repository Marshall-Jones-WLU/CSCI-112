"""
File: arrayQueue.py
Author: Marshall Jones
"""

from .arrays import Array
from .abstractCollection import AbstractCollection

class ArrayQueue(AbstractCollection):
    """An array-based queue implementation."""

    # Simulates a circlular queue within an array

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._front = self._rear = 1
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        super().__init__(sourceCollection)

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        # Same as an iterator for an arrayBag, only using modulo inside self._items access
        #  to wrap the cursor around the end of the array
        if self._front < self._rear:
            cursor = 0
            while cursor < len(self):
                yield self._items[cursor+self._front]
                cursor += 1
        else:
            cursor = 0
            while cursor < len(self):
                yield self._items[(cursor + self._front) % len(self._items)]
                cursor += 1
                

    
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        if self.isEmpty():
            raise ValueError("Attempt to peek at empty queue")
        return self._items[self._front]


    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArrayQueue.DEFAULT_CAPACITY)
        

    def resize(self, sizeFactor):
        """Copies over the values in self._items into a new array queue resized 
        by the sizeFactor parameter. Minimum size == DEFAULT_CAPACITY"""
        newSize = int(len(self._items) * sizeFactor) # establish the new size
        if newSize < ArrayQueue.DEFAULT_CAPACITY:
            newSize = ArrayQueue.DEFAULT_CAPACITY
            return
        
        tempArray = Array(newSize) # create a new empty array

        for i in range(self._size):
            # add items from previous array to the resized array
            tempArray[i] = self._items[i]
        
        self._items = tempArray
        self._front = 0
        self._rear = self._size - 1
        
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        # Check array memory here and increase it if necessary
        if len(self) == len(self._items):
            self.resize(2)
        
        if self.isEmpty():
            self._front = self._rear = 0
        else:
            self._rear += 1
            self._rear %= len(self._items)
        
        self._items[self._rear] = item
        self._size += 1
        # print("Rear:",self._items[self._rear])

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        # Check precondition here
        data = self._items[self._front]
        self._size -= 1
        if self.isEmpty():
            self._front = self._rear = -1
        else:
            self._front += 1
            self._front %= len(self._items)
        
        # Resize here if necessary
        if self._size <= len(self._items)//4:
            self.resize(.5)

        # print("Rear:",self._items[self._rear])
        return data
        

        
         
