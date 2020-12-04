import sys

def openFile():
    return open(sys.argv[1], "r")

def challenge1():
    """
    Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
    """
    file = openFile()
    byLine = file.readlines()
    for lineI in range(len(byLine)):
        for lineX in range(len(byLine)):
            if lineI == lineX:
                continue
            if int(byLine[lineI]) + int(byLine[lineX]) == 2020:
                print(int(byLine[lineI]) * int(byLine[lineX]))
    file.close()

def challenge2():
    """
    Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.
    """
    file = openFile()
    byLine = file.readlines()
    for lineI in range(len(byLine)):
        for lineX in range(len(byLine)):
            for lineY in range(len(byLine)):
                if lineI == lineX or lineI == lineY or lineX == lineY:
                    continue
                if int(byLine[lineI]) + int(byLine[lineX]) + int(byLine[lineY]) == 2020:
                    print(int(byLine[lineI]) * int(byLine[lineX]) * int(byLine[lineY]))
    file.close()


challenge1()
challenge2()