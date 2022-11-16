"""
Author: Liz Matthews
File: tools.py

"""

import random
import time

def getRandomList(n):
    """Returns a list of unique random numbers in the
    range 0..n-1"""
    items = list(range(n))
    random.shuffle(items)
    return items

def compare(titleList, functionList, sizeList,
            dataSet=lambda x: x, counter=None, compareType="time"):
   """Runs a comparison test between the functions in functionList."""
   
   print()
   
   # Print a header indicating what value is being compared
   print(compareType.title().center(25 + (12 * (len(titleList) - 1)) + 1, "-") + "\n")
   
   # Print the header for the table of runtimes
   headerString = "{:>25s}" + "{:>12s}" * (len(titleList) - 1) + "\n"
   
   print(headerString.format(*titleList))
   
   # Testing set
   for size in sizeList:
      
      
      # Print the lefthand label of the table
      print(" Size: {:>5d} ".format(size), end="", flush=True)
      
      
      # Test each function
      for function in functionList:
         
         # Create the data set
         data = dataSet(size)
            
         # When did we start the test      
         startTime = time.time()
         
         # Detect a counter variable
         if counter:            
            # Reset the counter
            for key in counter.keys():
               counter[key] = 0
               
            function(data, counter)
            
         else:
            function(data)
         
         # When did we end the test
         endTime = time.time()
         
         # Display in nice formatting the compare type
         
         if compareType == "time":
            value = endTime - startTime
            print("{:>12.4f}".format(value), end="", flush=True)
            
         elif compareType in counter.keys():
            value = counter[compareType]
            print("{:>12d}".format(value), end="", flush=True)
         
         else:
            print("ERROR: Unknown compare type " + compareType)         
            return
         
         
      
      print()
   
   print()
   
   
def show(n, function, dataSet=lambda x: x):
   """Shows the data returned by function."""
   print()
   
   data = dataSet(n)
   
   print(function(data))
      
   print()