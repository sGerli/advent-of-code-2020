import sys
from functools import reduce

def openFile():
    return open(sys.argv[1], "r")

def relativeX(x: int, matrix: list[list[str]]):
    xLen = len(matrix[0]) - 1
    return x % xLen

def slopeCheck(xChange: int, yChange: int, matrix: list[list[str]]):
    x = 0
    y = 0

    treeEncounters = 0

    while y < len(matrix):
        if matrix[y][relativeX(x, matrix)] == "#":
            treeEncounters += 1
        x += xChange
        y += yChange
    return treeEncounters

def challenge1():
    """
    Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
    """
    file = openFile()
    byLine = file.readlines()
    matrix = list(map(lambda x: [char for char in x], byLine))
        
    print(slopeCheck(3, 1, matrix))
    file.close()

def challenge2():
    """
    What do you get if you multiply together the number of trees encountered on each of the listed slopes?
    """
    file = openFile()
    byLine = file.readlines()
    matrix = list(map(lambda x: [char for char in x], byLine))
    slopes = []
    slopes += [slopeCheck(1, 1, matrix)]
    slopes += [slopeCheck(3, 1, matrix)]
    slopes += [slopeCheck(5, 1, matrix)]
    slopes += [slopeCheck(7, 1, matrix)]
    slopes += [slopeCheck(1, 2, matrix)]

    print(reduce(lambda a, b: a * b, slopes, 1))
    file.close()



challenge1()
challenge2()