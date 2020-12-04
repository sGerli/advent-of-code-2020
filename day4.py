import sys
import re

def openFile():
    return open(sys.argv[1], "r")

def isPassportValid(passport, fields: list[str]):
    for field in fields:
        if passport.get(field, None) is None:
            return False
    return True

def challenge1():
    """
    Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
    """
    FIELDS = {
        "byr", 
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid"
        }
    file = openFile()
    byLine = file.readlines()
    byLine += [""]
    passports = []
    currentPassport = {}
    valid = 0
    for line in byLine:
        if not line or line == "\n":
            # Empty string
            passports += [currentPassport]
            valid += 1 if isPassportValid(currentPassport, FIELDS) else 0
            currentPassport = {}
            continue
        line = line.replace("\n", " ")
        for pair in line.split(" "):
            if not pair:
                continue
            pair = pair.split(":")
            currentPassport[pair[0].lower()] = pair[1]

    print(valid)
            
    file.close()


def isPassportValidWithValidators(passport, fields: list[str]):
    for field in fields:
        value = passport.get(field, None)
        if value is None or not fields[field](value):
            return False
    return True

def challenge2():
    """
    Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
    """
    FIELDS = {
        "byr": lambda x: x.isdigit() and int(x) >= 1920 and int(x) <= 2002, 
        "iyr": lambda x: x.isdigit() and int(x) >= 2010 and int(x) <= 2020,
        "eyr": lambda x: x.isdigit() and int(x) >= 2020 and int(x) <= 2030,
        "hgt": lambda x: (re.search("^[0-9]+in$", x) and int(x[:-2]) >= 59 and int(x[:-2]) <= 76) or (re.search("^[0-9]+cm$", x) and int(x[:-2]) >= 150 and int(x[:-2]) <= 193),
        "hcl": lambda x: re.search("^#[a-f0-9]{6}$", x),
        "ecl": lambda x: x == "amb" or x == "blu" or x == "brn" or x == "gry" or x == "grn" or x == "hzl" or x == "oth",
        "pid": lambda x: x.isdigit() and len(x) == 9
        }
    file = openFile()
    byLine = file.readlines()
    byLine += [""]
    passports = []
    currentPassport = {}
    valid = 0
    for line in byLine:
        if not line or line == "\n":
            # Empty string
            passports += [currentPassport]
            valid += 1 if isPassportValidWithValidators(currentPassport, FIELDS) else 0
            currentPassport = {}
            continue
        line = line.replace("\n", " ")
        for pair in line.split(" "):
            if not pair:
                continue
            pair = pair.split(":")
            currentPassport[pair[0].lower()] = pair[1]

    print(valid)
            
    file.close()

challenge1()
challenge2()