import random

def randomFill(wordsearch):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for row in range(0, 12):
        for col in range(0, 12):
            if wordsearch[row][col] == "-":
                randomLetter = random.choice(LETTERS)
                wordsearch[row][col] = randomLetter

def displayWordsearch(wordsearch):
    print(" _________________________")
    print("|                         |")
    for row in range(0, 12):
        line="| "
        for col in range(0, 12):
            line = line + wordsearch[row][col] + " "
        line = line + "|"
        print(line)
    print("|_________________________|")

def addWord(word, wordsearch):
    row = random.randint(0, 11)
    col = 0
    for i in range(0, len(word)):
        wordsearch[row][col+i] = word[i]

wordsearch = []

for row in range(0, 12):
    wordsearch.append([])
    for col in range(0, 12):
        wordsearch[row].append("-")

addWord("PYTHON", wordsearch)

randomFill(wordsearch)

displayWordsearch(wordsearch)