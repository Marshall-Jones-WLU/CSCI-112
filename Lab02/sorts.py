"""
Author: Marshall Jones
File: sorts.py

Defines the selection sort and the quick sort.
"""
from tools import compare, getRandomList, show


def selectionSort(numbers, counter=None):    
    i = 0
    while i < len(numbers) - 1:
        minIndex = i
        j = i + 1
        while j < len(numbers):
            if numbers[j] < numbers[minIndex]:
                if counter:
                    counter["comparisons"] += 1
                minIndex = j
            j += 1
        if minIndex != i:
            if counter:
                    counter["swaps"] += 1
            numbers[i], numbers[minIndex] = numbers[minIndex], numbers[i]
        i += 1
    return numbers

def bubbleSort(numbers, counter=None):
    n = len(numbers)
    while n > 1:
        i = 1
        swapped = False
        while i < n:
            if numbers[i] < numbers[i - 1]:
                if counter:
                    counter["swaps"] += 1
                numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
                swapped = True
            i += 1
        if not swapped:
            return numbers
        n -= 1
    return numbers

def quickSort(numbers, counter=None):
    def quicksortHelper(numbers, left, right):
        if left < right:
            pivotLocation = partition(numbers, left, right)
            quicksortHelper(numbers, left, pivotLocation - 1)
            quicksortHelper(numbers, pivotLocation + 1, right)

    def partition(numbers, left, right):
        # Find the pivot and exchange it with the last item
        middle = (left + right) // 2
        pivot = numbers[middle]
        numbers[middle] = numbers[right]
        numbers[right] = pivot
        # Set boundary point to first position
        boundary = left
        # Move items less than pivot to the left
        for index in range(left, right):
            if numbers[index] < pivot:
                if counter:
                    counter["swaps"] += 1
                numbers[index], numbers[boundary] = numbers[boundary], numbers[index]
                boundary += 1
        # Exchange the pivot item and the boundary item
        if counter:
                    counter["swaps"] += 1
        numbers[right], numbers[boundary] = numbers[boundary], numbers[right]
        return boundary

    quicksortHelper(numbers, 0, len(numbers)-1)
    return numbers
 
def mergeSort(numbers, counter=None):
    # numbers <- list being sorted
    # copyBuffer temporary space needed during merge
    copyBuffer = []
    for i in range(len(numbers)):
        copyBuffer.append(0)

    def merge(numbers, copyBuffer, low, middle, high):
        # Initialize i1 and i2 to the first items in each sublist
        i1 = low
        i2 = middle + 1
        # Interleave items from the sublists into the
        # copyBuffer in such a way that order is maintained.
        for i in range(low, high + 1):
            if counter:
                counter["comparisons"] += 1
                if i1 > middle:
                    copyBuffer[i] = numbers[i2] # First sublist exhausted
                    i2 += 1
                elif i2 > high:
                    copyBuffer[i] = numbers[i1]
                    i1 += 1
                elif numbers[i1] < numbers[i2]:
                    if counter:
                        counter["swaps"] += 1
                    copyBuffer[i] = numbers[i1]
                    i1 += 1
                else:
                    if counter:
                        counter["swaps"] += 1
                    copyBuffer[i] = numbers[i2]
                    i2 += 1
        for i in range(low, high+1):
            numbers[i] = copyBuffer[i]

    def mergeSortHelper(numbers, copyBuffer, low, high):
        # low, high <- bounds of sublist
        # middle <- midpoint of sublist
        if low < high:
            middle = (low + high) // 2
            mergeSortHelper(numbers, copyBuffer, low, middle)
            mergeSortHelper(numbers, copyBuffer, middle+1, high)
            merge(numbers, copyBuffer, low, middle, high)

    mergeSortHelper(numbers, copyBuffer, 0, len(numbers)-1)
    return numbers


def main():
    # Tests first a random input, then a sorted input
    for testType in ["Random", "Sorted"]:
        
        # Displays if random or sorted
        print(testType.title().center(25 + (12 * (3)) + 1, "=") + "\n")
        
        # Uses HOF to determine the testSet
        if testType == "Random":
            testSet = getRandomList
            
        else:
            testSet = lambda x: list(range(x))
            
        # Displays all three metrics as described for this lab
        for test in ["time", "swaps", "comparisons"]:
            # Invokes compare for all sorts
            
            compare(["Selection", "Bubble", "Quick", "Merge", ],
                [selectionSort, bubbleSort, quickSort, mergeSort],
                [10,100,1000,10000],
                dataSet=testSet,
                counter={"comparisons" : 0, "swaps" : 0},
                compareType=test)
        
        print()

if __name__ == "__main__":
    main()
    #show(10, bubbleSort, getRandomList)
    #show(10, selectionSort, getRandomList)
    #show(10, quickSort, getRandomList)
    #show(10, mergeSort, getRandomList)
    #compare(["Selection", "Bubble"], [selectionSort, bubbleSort], [10,20,30], dataSet=getRandomList, counter={"swaps" : 0, "comparisons" : 0})
    #compare(["Quick", "Merge"], [quickSort, mergeSort], [10,20,30], dataSet=getRandomList, counter={"swaps" : 0, "comparisons" : 0})