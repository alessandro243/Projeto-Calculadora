import re
NUM_OR_DOT = re.compile(r'^[0-9.]$')
NUM = re.compile(r'^[0-9]$')

def isNumoDot(string: str):
    return bool(NUM_OR_DOT.search(string))

def isNum(string: str):
    return bool(NUM.search(string))

def isEmpty(string: str):
    return len(string) == 0

def isValid(string: str):
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        return False
    return valid

print('xl' in 'xvuiolp')
