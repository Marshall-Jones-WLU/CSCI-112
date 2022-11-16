                
                
from ..math.infinity import *
                
                

class PathEntry(object):
   def __init__(self, vertex, distance = INFINITY, path = None, included = False):
      """For use in Dijkstra's algorithm"""
      self.vertex = vertex
      self.distance = distance
      self.path = path
      self.included = included
   
   def __eq__(self, other):
      if self is other:
         return True
      if type(self) != type(other):
         return False
      
      return self.vertex == other.vertex
   
   def __lt__(self, other):
      if self.distance == INFINITY and other.distance == INFINITY:
         return self.vertex.getLabel() < other.vertex.getLabel()
      return lessThanWithInfinity(self.distance, other.distance)
   
   def __gt__(self, other):
      return not self < other


   def __str__(self):
      return str(self.vertex.getLabel()) + ", " + str(self.distance) + ", " + str(self.path) + ", " + str(self.included)

                