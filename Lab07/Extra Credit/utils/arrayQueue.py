"""
File: arrayQueue.py
Author: YOUR NAME GOES HERE
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
        pass

    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        # Same as an iterator for an arrayBag, only using modulo inside self._items access
        #  to wrap the cursor around the end of the array
        pass

    
    def peek(self):
        """Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty."""
        return None

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass
        
    

    def resize(self, sizeFactor):
        # Only shrink if we're not too small
        pass
        
    
    def add(self, item):
        """Inserts item at rear of the queue."""
        pass       

    def pop(self):
        """Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if queue is empty.
        Postcondition: the front item is removed from the queue."""
        return None

        
         
