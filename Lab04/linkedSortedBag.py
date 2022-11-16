"""
Author: Marshall Jones
File: linkedSortedbag.py
"""

from node import Node

class LinkedSortedBag(object):
    """A link-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = None
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
        """-Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self._items
        while not cursor is None:
            yield cursor.data
            cursor = cursor.next

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = LinkedSortedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        # preliminary equality checks
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        # traverse the linked structures and check for equality of individual nodes
        probe = self._items
        probeOther = other._items
        while probe.next != None:
            if probe.data != probeOther.data:
                return False
            probe = probe.next
            probeOther = probeOther.next
        return True


    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = None

    def add(self, item):
        """Adds item to self."""
        # check first node for None or a larger value than item
        if self._items == None or self._items.data > item:
            self._items = Node(item, self._items)
            self._size += 1
        else:
            # traverse through the container as long as the item is greater than the next node
            probe = self._items
            while probe.next != None:
                if item > probe.next.data:
                    probe = probe.next
                else:
                    break # item slot has been found
            probe.next = Node(item, probe.next)
            self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the node containing the target item
        # probe will point to the target node, and trailer
        # will point to the one before it, if it exists
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        # Unhook the node to be deleted, either the first one or one
        # thereafter
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        # Decrement logical size
        self._size -= 1
        
