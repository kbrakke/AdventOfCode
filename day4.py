__author__ = 'Kris'
import re

def noRepeatedStrings(match):
    for i in range(len(match)):
        for j in range(len(match)):
            if i != j:
                if match[i] == match[j]:
                    return False
    return True

def stringToDict(string):
    stringDict = {}
    for char in string:
        if stringDict.has_key(char):
            stringDict[char] += 1
        else:
            stringDict[char] = 1
    return stringDict
def noAnagrams(stringList):
    listOfStringDicts = []
    for i in range(len(stringList)):
        listOfStringDicts.append(stringToDict(stringList[i]))
    for i in range(len(listOfStringDicts)):
        for j in range(len(listOfStringDicts)):
            if i != j:
                if listOfStringDicts[i] == listOfStringDicts[j]:
                    return False
    return True

validCharactersRegex = re.compile(r"""([a-z]+)[ |$]""")

numNoMatch = 0
numNoAnagram = 0
for line in open('day4Input.txt'):
    groups = line.split()
    if groups:
        if noRepeatedStrings(groups):
            numNoMatch += 1
        if noAnagrams(groups):
            numNoAnagram +=1


print numNoMatch
print numNoAnagram