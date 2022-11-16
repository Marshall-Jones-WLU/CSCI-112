from utils.linkedStack import LinkedStack
from utils.arrayQueue import ArrayQueue
from utils.linkedQueue import LinkedQueue
from utils.grid import Grid

def getMazeFromFile():
    name = input("Enter name of maze: ")
    fileObj = open(name, "r")

    firstLine = list(map(int, fileObj.readline().strip().split()))
    rows = firstLine[0]
    cols = firstLine[1]

    maze = Grid(rows, cols, "*")
    
    for row in range(rows):
        line = fileObj.readline().strip()

        col = 0
        for ch in line:
            maze[row][col] = ch
            col += 1
    
    fileObj.close()
    
    return maze

def findStartPos(maze):
    for row in range(maze.getHeight()):
        for col in range(maze.getWidth()):
            if maze[row][col] == "S":
                return(row, col)

    return(-1, -1)

def getOut(maze, choiceStorage, showProcess=False):

    choices = choiceStorage()
    choices.add(findStartPos(maze))

    while not choices.isEmpty():
        c = choices.pop()
        if maze[c[0]][c[1]] == "G":
            return True
        else:
            maze[c[0]][c[1]] = "."

            if showProcess:
                print(maze)
                if input("Press enter to continue, q to skip to the end: ") == "q":
                    showProcess = False

            for newRow, newCol in [(c[0]+1, c[1]),
                                   (c[0]-1, c[1]),
                                   (c[0], c[1]+1),
                                   (c[0], c[1]-1)]:
                if newRow >= 0 and newRow < maze.getHeight() and \
                   newCol >= 0 and newCol < maze.getWidth() and \
                   maze[newRow][newCol] not in ".*":
                    choices.add((newRow, newCol))
    
    return False


def LStack():
    maze = getMazeFromFile()
    print(maze)
    

    success = getOut(maze, LinkedStack, True)
    if success:
        print("Maze solved using LinkedStack!")
        print(maze)
    else:
        print("No way out of this maze.")

def ArrayQ():
    maze = getMazeFromFile()
    print(maze)
    

    success = getOut(maze, ArrayQueue, True)
    if success:
        print("Maze solved using ArrayQueue!")
        print(maze)
    else:
        print("No way out of this maze.")

def LinkedQ():
    maze = getMazeFromFile()
    print(maze)
    

    success = getOut(maze, LinkedQueue, True)
    if success:
        print("Maze solved using LinkedQueue!")
        print(maze)
    else:
        print("No way out of this maze.")


if __name__ == "__main__":
    # LStack()
    # ArrayQ()
    LinkedQ()
