
import time
from tools import compare, show

def nQueensFancy(n=8, showTotal=False):
   # Set up the board with all the queens in row 0, total solutions found is 0
   total = 0
   board = [0 for x in range(n)]
   
   # Start with the left queen
   currentQueen = 0

   # Use an infinite loop and exit based on the total parameter
   while True:
      # Check if the board is currently safe
      if safeQueen(board, currentQueen):

         # If the current queen is the last queen
         if currentQueen == len(board) - 1:

            # If calculating a total, increase the total by one and move the current queen down
            if showTotal:
               total += 1
               board[currentQueen] += 1
            
            # otherwise, return the board as we've found a solution
            else:
               return board
         
         # If the current queen is not the last queen, move the current queen down
         else:
            currentQueen += 1
      
      # If the current queen is not safe...
      else:

         # Move the current queen down
         board[currentQueen] += 1
      
      # While the current queen is off the edge of the board...
      while board[currentQueen] == len(board):

         # If the current queen is the first queen, we've run out of possibilities and return the total
         if currentQueen == 0:
            return total
         
         # Otherwise...
         else:
            # Reset the current queen to the first row
            board[currentQueen] = 0

            # Move back one queen
            currentQueen -= 1

            # Move the new queen down one row
            board[currentQueen] += 1


def nQueensBrute(n=8, showTotal=False):
   # Set up the board with all the queens in row 0, total solutions found is 0
   total = 0
   board = [0 for x in range(n)]
   
   # Start with the left queen
   currentQueen = 0
   
   # Use an infinite loop and exit based on the total parameter
   while True:
      # Check if the board is currently safe
      if safeBoard(board):
         
         # Are we going for a total or single solution?
         if showTotal:
            total += 1
         
         # Return the board if only one solution is necessary
         else:
            return board
         
      # Otherwise, try to start with the left queen and try to move the queen down
      currentQueen = 0      
      board[currentQueen] += 1
      
      # While the queen we currently look at is beyond the edge of the board
      while board[currentQueen] == len(board):
         
         # Reset the current queen
         board[currentQueen] = 0
         
         # Move to the next queen
         currentQueen += 1
         
         # If we have run out of queens, then we've run out of possibilities
         if currentQueen >= len(board):
            return total
         
         # Move the current queen down one
         board[currentQueen] += 1
      

def showBoard(board):
   
   if board == None:
      return
   
   # Print the top border
   print("----" * len(board) + "-")
   
   # Iterate through the board and print Q if we have a queen there
   for row in range(len(board)):
      print("| ", end="")
      for col in range(len(board)):
         if board[col] == row:
            print("Q | ", end="")
         else:
            print("  | ", end="")
      
      # Print a line between the queens
      print()
      print("----" * len(board) + "-")


def safeQueen(board, currentQueen):

   # Check to make sure the current queen is safe from the queens already on the board
   for col in range(currentQueen):
      if checkVertical(board[col], board[currentQueen]) or checkDiagonal(board[col], col, board[currentQueen], currentQueen):
         return False

   return True

      

def safeBoard(board):
   # Check all queens to be safe, return false if not safe
   
   for colQ1 in range(len(board)):
      for colQ2 in range(colQ1+1,len(board)):
         if checkVertical(board[colQ1], board[colQ2]) or checkDiagonal(board[colQ1], colQ1, board[colQ2], colQ2):
            return False
         
   return True


   
def checkVertical(rowQ1, rowQ2):
   # Return if two queens on horizontal
   return rowQ1 == rowQ2

def checkDiagonal(rowQ1, colQ1, rowQ2, colQ2):
   # return if two queens on diagonal
   diffRow = abs(rowQ1 - rowQ2)
   diffCol = abs(colQ1 - colQ2)
   
   return diffRow == diffCol
   
   
   
   # Displays a comparison in RUNTIME between two functions used to create
   #  a random list.
   
def main():
   compare(["Brute", "Fancy"],
      [lambda x : nQueensBrute(x, True), lambda x : nQueensFancy(x, True)],
      [4,5,6,7,8,9])
   



if __name__ == '__main__':

   # Compare runtimes for increasing sizes of N for finding all possible solutions
   main()
   
   # Show how many solutions there are
   #show(5, lambda x : nQueensBrute(x, True))
   #show(5, lambda x : nQueensFancy(x, True))
   # or
   #print(nQueensFancy(5, True))
   
   # Show the first board found
   #showBoard(nQueensBrute(5))
   #showBoard(nQueensFancy(8))
