import sys
import re

def openFile():
    return open(sys.argv[1], "r")


def challenge1():
    file = openFile()
    byLine = file.readlines()
    byLine += [""]
    currentQuestionaire = {}
    sum = 0
    for line in byLine:
        if not line or line == "\n":
            # Empty string
            sum += len(currentQuestionaire)
            currentQuestionaire = {}
            continue
        line = line.replace("\n", "")
        for char in line:
            currentQuestionaire[char] = char

    print(sum)
            
    file.close()

def challenge2():
    file = openFile()
    byLine = file.readlines()
    byLine += [""]
    currentQuestionaire = {}
    questionaireCount = 0
    sum = 0
    for line in byLine:
        if not line or line == "\n":
            # Empty string
            for item in currentQuestionaire:
                if currentQuestionaire[item] == questionaireCount:
                    sum += 1
            currentQuestionaire = {}
            questionaireCount = 0
            continue
        line = line.replace("\n", "")
        questionaireCount += 1
        for char in line:
            currentQuestionaire[char] = currentQuestionaire.get(char, 0) + 1

    print(sum)
            
    file.close()



challenge2()