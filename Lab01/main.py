import random
import time

def randomNumbers(n):
   result = []
   
   while len(result) < n:
      num = random.randint(0,n-1)
      
      found = False
      
      for x in range(len(result)):
         if result[x] == num:
            found = True
            break
      
      if not found:
         result.append(num)
   
   return result

def randomIndexes(n):
   result = [-1 for x in range(n)]
   
   for num in range(n):
      index = random.randint(0,n-1)
      
      while result[index] != -1:
         index = random.randint(0,n-1)
      
      result[index] = num
   
   return result

def randomShuffle(n):
   result = [x for x in range(n)]

   for i in result:
      num = random.randint(i,n-1)
      a = result[i] # create a temporary variable for the swap
      result[i] = result[num]
      result[num] = a

   return result

# Displays a comparison in RUNTIME between two functions used to create
#  a random list. Tests sizes 10, 100, 1000, and 10000. May take a long
#  time to finish.
def main():
   
   print()
   
   # Print the header for the table of runtimes
   print("{:>25s}{:>12s}{:>12s}\n".format("Numbers", "Indexes", "Shuffle"))
   
   # Testing set
   for size in [10,100,1000,10000]:
      
      # Print the lefthand label of the table
      print(" Size: {:>5d} ".format(size), end="", flush=True)
      
      
      # Test each function
      for function in [randomNumbers, randomIndexes, randomShuffle]:
            
         # When did we start the test      
         startTime = time.time()
         
         function(size)
         
         # When did we end the test
         endTime = time.time()
         
         # Display in nice formatting the difference in seconds between starting
         #  and ending the test.
         print("{:>12.4f}".format(endTime - startTime), end="", flush=True)
         
      
      print()
   
   print()
      

# Use this function instead of main() to see the list created by your function.
#  Change the line at the bottom of this file to use showList instead of main() to
#  use.
#  Example use: showList(10, randomIndexes)
def showList(n, function):
   
   print()
   
   print(function(n))
      
   print()
   



if __name__ == "__main__":
   main()
   # showList(10, randomShuffle)
