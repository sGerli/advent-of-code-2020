import sys
import re

def openFile():
    return open(sys.argv[1], "r")

def challenge1():
    """How many bags can eventually contain a shiny gold bag
    """
    file = openFile()
    byLine = file.readlines()
    count = 0
    rules = {}
    for line in byLine:
        name, rule = decodeRule(line.replace("\n", ""))
        rules[name] = rule
    find = "shiny gold"

    for rule in rules:
        if find in rules[rule]:
            count += 1
        else:
            count += 1 if recursiveSearch(rules, rule, find) else 0
    print(count)
    file.close()

def recursiveSearch(rules: dict, currentItem: str, find: str) -> bool:
    if find in rules[currentItem]:
        return True
    else:
        for rule in rules[currentItem]:
            if recursiveSearch(rules, rule, find):
                return True
    return False

def decodeRule(rule: str) -> tuple[str, dict]:
    RULE_REGEX = "^(.*) (?:bag|bags) contain (.*).$"
    CONTAINS_ITEM_REGEX = "^\s*(\d) (.*) (?:bag|bags)?\s*$"

    match = re.match(RULE_REGEX, rule)
    ruleItem = match.group(1)
    containsItems = match.group(2).split(", ")
    containsItemsRules = {}
    for item in containsItems:
        itemMatch = re.match(CONTAINS_ITEM_REGEX, item)
        if itemMatch:
            containsItemsRules[itemMatch.group(2)] = itemMatch.group(1)
    return (ruleItem, containsItemsRules)


def challenge2():
    """How many bags a shiny gold must contain
    """
    file = openFile()
    byLine = file.readlines()
    count = 0
    rules = {}
    for line in byLine:
        name, rule = decodeRule(line.replace("\n", ""))
        rules[name] = rule
    find = "shiny gold"

    print(recursiveCount(rules, find))
    file.close()

def recursiveCount(rules: dict, currentRule: str):
    count = 0
    for rule in rules[currentRule]:
        ruleCount = int(rules[currentRule][rule])
        recursiveBagNumber = recursiveCount(rules, rule)
        count += ruleCount + (ruleCount * recursiveBagNumber)
    return count


challenge2()