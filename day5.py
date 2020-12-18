from os import startfile
import sys
import math

def openFile():
    return open(sys.argv[1], "r")

def challenge1():
    """Get largest seat id
    """
    file = openFile()
    byLine = file.readlines()
    maxId = 0
    for line in byLine:
        id = decodeSeat(line.replace("\n", ""))
        if id > maxId:
            maxId = id
    print(maxId)
    file.close()

def decodeSeat(binaryCode: str) -> int:
    rowCode = binaryCode[:-3]
    columnCode = binaryCode[-3:]
    rowNumber = binaryDecode(rowCode, "F", "B", 127)
    columnNumber = binaryDecode(columnCode, "L", "R", 7)
    id = rowNumber * 8 + columnNumber
    return id

def binaryDecode(code: str, lowerHalf: str, upperHalf: str, total: int) -> int:
    start = 0
    end = total
    for char in code:
        if char == lowerHalf:
            end -= math.ceil((end - start) / 2)
        elif char == upperHalf:
            start += math.ceil((end - start) / 2)
        else:
            print("Unknown char " + char)
    return start


def challenge2():
    """Find missing seat with existing next and last seat.
    """
    file = openFile()
    byLine = file.readlines()
    seats = {}
    smallestId = sys.maxsize
    largestId = 0
    for line in byLine:
        id = decodeSeat(line.replace("\n", ""))
        seats[id] = id
        if id > largestId:
            largestId = id
        if id < smallestId:
            smallestId = id
    file.close()

    for seat in range(smallestId, largestId):
        if seats.get(seat, None) is None and \
           seats.get(seat - 1, None) is not None and \
           seats.get(seat + 1, None) is not None:
           print(seat)


challenge1()
challenge2()