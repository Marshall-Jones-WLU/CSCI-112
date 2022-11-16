"""
Author: Marshall Jones
File: linkedSortedbag.py
"""

# import statements
from node import Node
from linkedBag import LinkedBag

class LinkedSortedBag(LinkedBag):
    """A link-based bag implementation."""

    # Constructor
    def __init__(self, sourceCollection = None):
        super().__init__(sourceCollection)


    # Accessor methods
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise. This method 
        overrides the equality method in 
        abstractBag for improved efficiency"""
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
    def add(self, item):
        """Adds item to self."""
        # check first node for None or a larger value than item
        if self._items == None or self._items.data > item:
            super().add()
            
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