import re

print("Advent of code day 4")


def validByr(byr):
    try:
        return int(byr) <= 2002 and int(byr) >= 1920
    except e:
        return False


def validIyr(iyr):
    try:
        return int(iyr) <= 2020 and int(iyr) >= 2010
    except e:
        return False


def validEyr(eyr):
    try:
        return (int(eyr) <= 2030 and int(eyr) >= 2020)
    except e:
        return False


def validHgt(hgt):
    heightRegex = re.compile('(\d+)(cm|in)')
    heightMatch = heightRegex.search(hgt)
    if heightMatch:
        (num, unit) = heightMatch.group(1, 2)
        if unit == "cm":
            return (int(num) >= 150 and int(num) <= 193)
        elif unit == "in":
            return (int(num) >= 59 and int(num) <= 76)
    else:
        return False


def validHcl(hcl):
    hairColorRegex = re.compile('#[0-9a-f]{6}')
    hairColorMatch = hairColorRegex.search(hcl)
    if hairColorMatch:
        return True
    return False


def validEcl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validPid(pid):
    if len(pid) > 9:
        return False
    pidRegex = re.compile('[0-9]{9}')
    pidMatch = pidRegex.search(pid)
    if pidMatch:
        return True
    return False


def validCid(cid):
    return True


passportValidators = {
    'byr': validByr,
    'iyr': validIyr,
    'eyr': validEyr,
    'hgt': validHgt,
    'hcl': validHcl,
    'ecl': validEcl,
    'pid': validPid,
    'cid': validCid
}


def isValid(passport):
    print(passport)
    sortedKeys = sorted(passport.keys())
    if len(sortedKeys) < 7:
        return False
    if sortedKeys == requiredFields or sortedKeys == sorted(requiredFields + optionalFields):
        for key in sortedKeys:
            if not passportValidators[key](passport[key]):
                print("invalid: ", key)
                return False
        return True
    else:
        return False


requiredFields = sorted(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])
optionalFields = ['cid']
passports = []
newPassport = {}
for line in open('/home/kbrakke/personal/AdventOfCode/AOC-2020/input/04/04-input.txt'):
    if line.rstrip() == "":
        passports.append(newPassport)
        newPassport = {}
    else:
        entries = line.rstrip().split(' ')
        for entry in entries:
            splitEntry = entry.split(':')
            newPassport[splitEntry[0]] = splitEntry[1]
passports.append(newPassport)

valid = 0
for passport in passports:
    if isValid(passport):
        valid += 1

print("Valid Passports: ", valid)
