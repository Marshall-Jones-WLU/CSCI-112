"""
Author: Marshall Jones
File: concordance.py

Creates a concordance on a file.
"""

from linkedBag import LinkedBag
from arraySortedSet import ArraySortedSet

def normalize(word):
    """Strips out punctuation and converts to uppercase."""
    word = word.upper()
    if len(word) > 2:
        if word[-1] == "\"":
            word = word[:-1]
        if word[-1] in (",", ".", "?", "!", ":", ";", ")", "]"):
            word = word[:-1]
        if word[0] in ("[", "(", "\""):
            word = word[1:]
    return word

def main():
    """Starting point for the application."""
    # Open the input file
    fileName = input("Enter the file name: ")
    file = open(fileName, 'r')

    # Input and normalize the words
    allWords = LinkedBag(map(normalize,
                             file.read().split()))
    # Display the concordance
    print("%25s %s" %("Word", "Frequency"))
    for word in ArraySortedSet(allWords):
        print("%25s %5d" % (word, allWords.count(word)))

if __name__ == "__main__":
    main()
