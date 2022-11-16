from .abstractCollection import AbstractCollection

class AbstractHeap(AbstractCollection):
   """An abstract approach to __str__ for binary tree shapes"""
   def __init__(self, sourceCollection):      
      super().__init__(sourceCollection)
   
   
   def add(self, item):
      """To be implemented in an implementation."""
      raise NotImplementedError("Abstract class method invoked.")
   
   def pop(self):
      """To be implemented in an implementation."""
      raise NotImplementedError("Abstract class method invoked.")
   
   
   def __str__(self):
      """Returns a string representation with the tree rotated
         90 degrees counterclockwise."""
      def recurse(index, level):
         s = ""
         if self._insideTree(index):
            s += recurse(self._getRightChild(index), level + 1)
            s += "| " * level
            s += str(self._getData(index)) + "\n"
            s += recurse(self._getLeftChild(index), level + 1)
         return s
      return recurse(self._getRoot(), 0)
