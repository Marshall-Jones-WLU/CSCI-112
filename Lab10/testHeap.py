"""
File: testHeap.py
Marshall Jones
"""


from utils.linkedHeap import LinkedHeap
from utils.arrayHeap import ArrayHeap
import random


def main(heapType):
   lyst = list(range(1, 31))
   random.shuffle(lyst)
   
   
   hp = heapType()
   
   print("Adding items to heap, inspect for heap-ness:")
   for item in lyst:
      print("adding", item)
      hp.add(item)
      print(hp)
      print()
   
   print("Heap size, expect 30:", len(hp))
   
   print("Expect items in order:", end=" ")
   while not hp.isEmpty():
      print(hp.pop(), end=" ")
   print()
   
   print("Heap size, expect 0:", len(hp))
   
if __name__ == '__main__':
   # main(ArrayHeap)
   main(LinkedHeap)