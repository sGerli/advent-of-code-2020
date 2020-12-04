import sys
import re

def openFile():
    return open(sys.argv[1], "r")

def challenge1():
    """
    How many passwords are valid according to their policies?
    """
    file = openFile()
    byLine = file.readlines()
    pattern = "^(\d*)-(\d*) ([a-z]): ([a-z]*)$"
    valid = 0
    for line in byLine:
        match = re.search(pattern, line)
        lowerBound = int(match.group(1))
        upperBound = int(match.group(2))
        letter = match.group(3)
        password = match.group(4)
        count = len(re.findall(letter, password))
        if count >= lowerBound and count <= upperBound:
            valid += 1
    print(valid)
    file.close()

def challenge2():
    """
    Exactly one of these positions must contain the given letter.
    How many passwords are valid according to their policies?
    """
    file = openFile()
    byLine = file.readlines()
    pattern = "^(\d*)-(\d*) ([a-z]): ([a-z]*)$"
    valid = 0
    for line in byLine:
        match = re.search(pattern, line)
        pos1 = int(match.group(1)) - 1
        pos2 = int(match.group(2)) - 1
        letter = match.group(3)
        password = match.group(4)
        if (password[pos1] == letter or password[pos2] == letter) and \
             not (password[pos1] == letter and password[pos2] == letter):
            valid += 1
    print(valid)
    file.close()


challenge1()
challenge2()