import sys
import math

def openFile():
    return open(sys.argv[1], "r")


def challenge1():
    file = openFile()
    byLine = file.readlines()
    file.close()
    byLine = list(map(lambda x: int(x), byLine))
    print(checkNumbers(byLine, 25, 25))

def checkNumbers(numList: list[int], preamble: int, lookback: int):
    numbersToCheck = len(numList) - preamble

    for i in range(numbersToCheck):
        realIndex = preamble + i
        num = numList[realIndex]
        lookbackList = numList[realIndex - lookback : realIndex]
        foundItem = False
        for item in lookbackList:
            compliment = num - item
            if compliment in lookbackList:
                foundItem = True
                break
        if foundItem == False:
            return num
    return None
            

def challenge2():
    file = openFile()
    byLine = file.readlines()
    file.close()
    byLine = list(map(lambda x: int(x), byLine))
    sumNumber = 50047984
    for i in range(len(byLine)):
        y = i
        smallest = largest = currentSum = byLine[i]
        while currentSum < sumNumber and y < len(byLine) - 1:
            y += 1
            currentSum += byLine[y]
            if byLine[y] < smallest:
                smallest = byLine[y]
            if byLine[y] > largest:
                largest = byLine[y]
        if currentSum == sumNumber:
            print(smallest + largest)
            break


challenge2()