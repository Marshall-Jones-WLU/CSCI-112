"""
File: testList.py
Author: Marshall Jones
A tester program for list implementations.
"""
from utils.linkedList import LinkedList
from utils.arrayList import ArrayList


def testList(listType):
    print("CREATING THE LIST")
    lyst = listType()
    print("Length, expect 0:", len(lyst))
    print("Empty, expect True", lyst.isEmpty())
    print("Appending integers 1-10")
    for i in range(10):
        lyst.append(i+1)
    print("Items (first to last):",lyst)

    print("\nCOMMENCE TESTING")
    print("Popping element at index 0:", lyst.pop(0))
    print("Expect list without 1:", lyst)
    
    lyst2 = listType(lyst)
    print("Cloned list:", lyst2)
    print("Popping cloned list from the back:",end=" ")
    # while len(lyst2) > 0:
    for i in range(len(lyst2)):
        print(lyst2.pop(), end=" ")
    print("\nExpect empty cloned list:", lyst2)

    for i in range(3,8):
        lyst.remove(i)
    print("Removed 3-7 from list, expect [2, 8, 9, 10]:", lyst)

    lyst.add(11)
    print("Added 11 to end of list:", lyst)

    lyst.insert(0, 99)
    print("\nInserted 99 at beginning, expect [99, 2, 8, 9, 10, 11]:", lyst)
    lyst.insert(3, 69)
    print("Inserted 69 at index 3, expect [99, 2, 8, 69, 9, 10, 11]:", lyst)
    lyst.insert(len(lyst), 39)
    print("Inserted 39 at end, expect [99, 2, 8, 69, 9, 10, 11, 39]:", lyst)
    lyst.insert(-15, -15)
    print("Insert attempted at negative index, expect [-15, 99, 2, 8, 69, 9, 10, 11, 39]:", lyst)
    lyst.insert(15, 15)
    print("Insert attempted at index beyond edge of list, expect [-15, 99, 2, 8, 69, 9, 10, 11, 39, 15]:", lyst)

    print("\nChecking index of item '99' in lyst, expect 1:", lyst.index(99))

    # lyst.replace(1, 1) # method currently unsupported
    lyst[1] = 1
    print("Replaced 99 with 1:", lyst)

    print("Popping second half of list:", end=" ")
    for i in range(len(lyst)//2):
        print(lyst.pop(), end=" ")
    
    print("\nLooping through list and printing remaining items:", end=" ")
    for i in range(len(lyst)):
        print(lyst[i], end=" ")
    print("\n")

    try:
        # Code that should crash, such as accessing an index out
        # of bounds or modifying inside a for-loop
        print("Attempting to access item at index 10, expect program to crash")
        print(lyst[10])
    except:
        print("Program successfully crashed")


def testListIterator(listType):
    # Create the list
    print("\nCREATING THE LIST")
    lyst = listType()
    print("Adding integers 1-10 to new list")
    for i in range(10):
        lyst.append(i+1)
    print("Items (first to last):",lyst)

    # Initiate the list iterator
    listIterator = lyst.listIterator()
    print("\nLIST ITERATOR INITIATED")

    # Begin testing
    print("\nCOMMENCE TESTING")
    print("Forward traversal: ", end = "")
    listIterator.first()
    while listIterator.hasNext():
        print(listIterator.next(), end = " ")
    
    print("\nBackward traversal: ", end = "")
    listIterator.last()
    while listIterator.hasPrevious():
        print(listIterator.previous(), end = " ")
    
    print("\nInserting 10 before 2: ", end = "")
    listIterator.first()
    for j in range(2):
        listIterator.next()
    listIterator.insert(10)
    print(lyst)

    print("Removing 2: ", end = "")
    listIterator.first()
    for j in range(3):
        listIterator.next()
    listIterator.remove()
    print(lyst)

    print("Replacing 5 with 99:", end="")
    listIterator.first()
    for j in range(5):
        listIterator.next()
    listIterator.replace(99)
    print(lyst)

    print("Removing all items")
    listIterator.first()
    while listIterator.hasNext():
        listIterator.next()
        listIterator.remove()
    print("Length:", len(lyst))


if __name__ == "__main__":
    # testList(ArrayList)
    testList(LinkedList)

    # testListIterator(ArrayList)
    # testListIterator(LinkedList)