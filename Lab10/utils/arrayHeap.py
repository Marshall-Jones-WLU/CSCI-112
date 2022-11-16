"""
File: arrayHeap.py
Marshall Jones
"""

from .arrayList import ArrayList
from .abstractHeap import AbstractHeap


class ArrayHeap(AbstractHeap):
   """An array-based implementation of a heap."""
   
   DEFAULT_SIZE = 10
   
   def __init__(self, sourceCollection = None):
      """Initialization of a heap."""
      self._heap = ArrayList()      
      super().__init__(sourceCollection)

   # Accessor Methods
   def _getRoot(self):
      """Should return the way to access the root based on an implementation."""
      return 0
   
   def _getParent(self, index):
      """Returns access to the parent from the index or node."""
      # raise error if index is root node?
      return (index - 1) / 2
   
   def _getLeftChild(self, index):
      """Returns access to the left child from the index or node."""
      # raise error if no child?
      return index * 2 + 1
   
   def _getRightChild(self, index):      
      """Returns access to the right child from the index or node."""
      # raise error if no child?
      return index * 2 + 2

   def _getData(self, index):
      """Returns the data from the index or node."""
      return self._heap[index]

   def _insideTree(self, node):
      """Returns True if the index or node is within the tree."""
      if node < len(self): return True
      else: return False


   # Mutator Methods
   
   def add(self, item):
      """Adds item to the end of the array and then walks it up to the top,
         stopping when parent is less than the new item"""
         
      self._size += 1
      self._heap.append(item)
      curPos = len(self._heap) - 1
      
      while curPos > 0:
         parent = (curPos - 1) // 2
         parentItem = self._heap[parent]
         if parentItem <= item:
            break
 
         else:
            self._heap[curPos] = self._heap[parent]
            self._heap[parent] = item
            curPos = parent
   
   def pop(self):
      """Swaps the top element with the last element, then walks the top
         element down until both children are larger than the current node."""
      if self.isEmpty():
         raise KeyError("The heap is empty.")
         
      self._size -= 1
      topItem = self._heap[0]
      bottomItem = self._heap.pop(len(self._heap) - 1)
      
      if len(self._heap) == 0:
         return bottomItem
             
      self._heap[0] = bottomItem
      lastIndex = len(self._heap) - 1
      curPos = 0
   
      while True:
         leftChild = curPos * 2 + 1
         rightChild = curPos * 2 + 2
         
         if leftChild > lastIndex:
            break
         
         if rightChild > lastIndex:
            maxChild = leftChild
            
         else:
            leftItem  = self._heap[leftChild]
            rightItem = self._heap[rightChild]
            if leftItem < rightItem:
               maxChild = leftChild
               
            else:
               maxChild = rightChild
               
         maxItem = self._heap[maxChild]
         
         if bottomItem <= maxItem:
            break
         
         else:
            self._heap[curPos] = self._heap[maxChild]
            self._heap[maxChild] = bottomItem
            curPos = maxChild
            
      return topItem
   
   
   # def __str__(self):
      # s = super().__str__()
      # return s
   #    """Returns a string representation with the tree rotated
   #       90 degrees counterclockwise."""
   #    def recurse(index, level):
   #       s = ""
   #       if index < len(self):
   #          s += recurse(index * 2 + 2, level + 1)
   #          s += "| " * level
   #          s += str(self._heap[index]) + "\n"
   #          s += recurse(index * 2 + 1, level + 1)
   #       return s
   #    return recurse(0, 0)
   



