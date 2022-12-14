"""
File: linkedbst.py
Author: Marshall Jones
"""

from utils.abstractcollection import AbstractCollection
from utils.bstnode import BSTNode
from math import log
from utils.linkedstack import LinkedStack
from utils.linkedqueue import LinkedQueue

class LinkedBST(AbstractCollection):
    """An link-based binary search tree implementation."""

    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._root = None
        AbstractCollection.__init__(self, sourceCollection)
        
    # Accessor methods
    def __str__(self):
        """Returns a string representation with the tree rotated
        90 degrees counterclockwise."""
        def recurse(node, level):
            s = ""
            if node != None:
                s += recurse(node.right, level + 1)
                s += "| " * level
                s += str(node.data) + "\n"
                s += recurse(node.left, level + 1)
            return s
        return recurse(self._root, 0)

    def __iter__(self):
        """Supports a preorder traversal on a view of self."""
        return self.preorder()
    
    def preorder(self):
        """Supports a preorder traversal on a view of self."""
        stack = LinkedStack()
        probe = self._root
        stack.push(probe)
        while not stack.isEmpty():
            if probe != None:
                probe = stack.pop()
                yield probe.data

            if probe.right != None:
                stack.push(probe.right)
            
            if probe.left != None:
                stack.push(probe.left)


    # def preorder(self):
    #     """Supports a preorder traversal on a view of self."""
    #     lyst = list()
    #     def recurse(node):
    #         if node != None:
    #             lyst.append(node.data)
    #             recurse(node.left)
    #             recurse(node.right)
    #     recurse(self._root)
    #     return iter(lyst)
    
    def inorder(self):
        """Supports an inorder traversal on a view of self."""
        stack = LinkedStack()
        probe = self._root
        while True:
            if probe != None:
                stack.push(probe)
                probe = probe.left
            elif not stack.isEmpty():
                probe = stack.pop()
                yield probe.data
                probe = probe.right
            else:
                break

    # def inorder(self):
    #     """Supports an inorder traversal on a view of self."""
    #     lyst = list()
    #     def recurse(node):
    #         if node != None:
    #             recurse(node.left)
    #             lyst.append(node.data)
    #             recurse(node.right)
    #     recurse(self._root)
    #     return iter(lyst)

    def postorder(self):
        """Supports a postorder traversal on a view of self."""
        lyst = list()
        def recurse(node):
            if node != None:
                recurse(node.left)
                recurse(node.right)
                lyst.append(node.data) # check this to make sure it's correct
        recurse(self._root)
        return iter(lyst)

    def levelorder(self):
        """Supports a levelorder traversal on a view of self."""
        lyst = list()
        q = LinkedQueue()
        q.add(self._root)
        while not q.isEmpty():
            root = q.pop()
            lyst.append(root.data)
            if root.left != None: q.add(root.left)
            if root.right != None: q.add(root.right)
        return iter(lyst)

    def __contains__(self, item):
        """Returns True if target is found or False otherwise."""
        return self.find(item) != None

    def find(self, item):
        """If item matches an item in self, returns the
        matched item, or None otherwise."""
        def recurse(node):
            if node is None:
                return None
            elif  item == node.data:
                return node.data
            elif item < node.data:
                return recurse(node.left)
            else:
                return recurse(node.right)
        return recurse(self._root)

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._root = None
        self.resetSizeAndModCount()

    def add(self, item):
        """Adds item to the tree."""

        # Helper function to search for item's position 
        def recurse(node):
            # New item is less, go left until spot is found
            if item < node.data:
                if node.left == None:
                    node.left = BSTNode(item)
                else:
                    recurse(node.left)
            # New item is greater or equal, 
            # go right until spot is found
            elif node.right == None:
                node.right = BSTNode(item)
            else:
                recurse(node.right)
            # End of recurse

        # Tree is empty, so new item goes at the root
        if self.isEmpty():
            self._root = BSTNode(item)
        # Otherwise, search for the item's spot
        else:
            recurse(self._root)
        self._size += 1
        self.incModCount()

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item is not in self.
        postcondition: item is removed from self."""
        if not item in self:
            raise KeyError("Item not in tree.""")

        # Helper function to adjust placement of an item
        def liftMaxInLeftSubtreeToTop(top):
            # Replace top's datum with the maximum datum in the left subtree
            # Pre:  top has a left child
            # Post: the maximum node in top's left subtree
            #       has been removed
            # Post: top.data = maximum value in top's left subtree
            parent = top
            currentNode = top.left
            while not currentNode.right == None:
                parent = currentNode
                currentNode = currentNode.right
            top.data = currentNode.data
            if parent == top:
                top.left = currentNode.left
            else:
                parent.right = currentNode.left

        # Begin main part of the method
        if self.isEmpty(): return None
        
        # Attempt to locate the node containing the item
        itemRemoved = None
        preRoot = BSTNode(None)
        preRoot.left = self._root
        parent = preRoot
        direction = 'L'
        currentNode = self._root
        while not currentNode == None:
            if currentNode.data == item:
                itemRemoved = currentNode.data
                break
            parent = currentNode
            if currentNode.data > item:
                direction = 'L'
                currentNode = currentNode.left
            else:
                direction = 'R'
                currentNode = currentNode.right
                
        # Return None if the item is absent
        if itemRemoved == None: return None
        
        # The item is present, so remove its node

        # Case 1: The node has a left and a right child
        #         Replace the node's value with the maximum value in the
        #         left subtree
        #         Delete the maximium node in the left subtree
        if not currentNode.left == None \
           and not currentNode.right == None:
            liftMaxInLeftSubtreeToTop(currentNode)
        else:
            
        # Case 2: The node has no left child
            if currentNode.left == None:
                newChild = currentNode.right
                
        # Case 3: The node has no right child
            else:
                newChild = currentNode.left
                
        # Case 2 & 3: Tie the parent to the new child
            if direction == 'L':
                parent.left = newChild
            else:
                parent.right = newChild
            
        # All cases: Reset the root (if it hasn't changed no harm done)
        #            Decrement the collection's size counter
        #            Return the item
        self._size -= 1
        self.incModCount()
        if self.isEmpty():
            self._root = None
        else:
            self._root = preRoot.left
        return itemRemoved

    def replace(self, item, newItem):
        """Precondition: item == newItem.
        Raises: KeyError if item != newItem.
        If item is in self, replaces it with newItem and
        returns the old item, or returns None otherwise."""
        if item != newItem: raise KeyError("Items must be equal")
        probe = self._root
        while probe != None:
            if probe.data == item:
                oldData = probe.data
                probe.data = newItem
                return oldData
            elif probe.data > item:
                probe = probe.left
            else:
                probe = probe.right
        return None

    def height(self):
        """Returns the height of the tree (the length of the longest path
        from the root to a leaf node).
        When len(t) < 2, t.height() == 0."""
        def recurse(node):
            if node == None: return 0
            else: return 1 + max(recurse(node.left), recurse(node.right))

        height = recurse(self._root)
        if not self.isEmpty(): height -= 1
        return height


    def isBalanced(self):
        """Returns True if the tree is balaned or False otherwise.
        t is balanced if t.height() < 2 * log2(len(t) + 1) - 1."""
        if self.height() < (2 * log(len(self) + 1, 2) - 1): return True
        else: return False

    def rebalance(self):
        """Rebalances the tree."""
        lyst = list()
        for item in self.inorder(): lyst.append(item)
        self.clear()

        def rebuild(lyst):
            if len(lyst) > 0:
                middle = len(lyst)//2
                self.add(lyst.pop(middle))
                leftLyst = list(lyst[0:middle-1])
                rightLyst = list(lyst[middle:len(lyst)])
                rebuild(leftLyst)
                rebuild(rightLyst)
            else: return
        
        rebuild(lyst)
