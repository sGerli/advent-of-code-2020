import sys
import copy

def openFile():
    return open(sys.argv[1], "r")

def challenge1():
    """Accumulator value before repeating instruction
    """
    file = openFile()
    lines = file.readlines()
    file.close()

    # Prepare
    lines = list(map(lambda x: x.replace("\n", "").split(" ") , lines))

    ip = 0
    accumulator = 0

    executed = {}

    while True:
        instruction = lines[ip]
        
        if ip in executed:
            print(accumulator)
            break
        
        executed[ip] = True

        if instruction[0] == "acc":
            accumulator += int(instruction[1])
            ip += 1
        elif instruction[0] == "jmp":
            ip += int(instruction[1])
        elif instruction[0] == "nop":
            ip += 1
        else:
            print("Unknown instruction [" + ip + "] " + instruction[0])


def challenge2():
    """Change 1 instruction to remove loop
    """
    file = openFile()
    lines = file.readlines()
    file.close()

    # Prepare
    lines = [*map(lambda x: x.replace("\n", "").split(" ") , lines)]

    for line in range(len(lines)):
        newCode = copy.deepcopy(lines)
        if lines[line][0] == "nop":
            newCode[line][0] = "jmp"
        elif lines[line][0] == "jmp":
            newCode[line][0] = "nop"
        
        if lines[line][0] == "nop" or lines[line][0] == "jmp":
            try:
                print(executeCode(newCode))
            except Exception as e:
                pass

    

def executeCode(code: list):
    ip = 0
    accumulator = 0

    executed = {}

    while True:
        if ip == len(code):
            return accumulator
        elif ip > len(code):
            raise Exception("ip out of bounds")
        elif ip in executed:
            raise Exception("looped")

        instruction = code[ip]
        
        executed[ip] = True

        if instruction[0] == "acc":
            accumulator += int(instruction[1])
            ip += 1
        elif instruction[0] == "jmp":
            ip += int(instruction[1])
        elif instruction[0] == "nop":
            ip += 1
        else:
            print("Unknown instruction [" + ip + "] " + instruction[0])

challenge1()
challenge2()