__author__ = 'Kris'

def calculateSum(coordinateMap, x, y):
    return coordinateMap.get((x+1, y+1), 0) + \
           coordinateMap.get((x  , y+1), 0) + \
           coordinateMap.get((x-1, y+1), 0) + \
           coordinateMap.get((x+1, y-1), 0) + \
           coordinateMap.get((x+1, y  ), 0) + \
           coordinateMap.get((x-1, y-1), 0) + \
           coordinateMap.get((x-1, y  ), 0) + \
           coordinateMap.get((x  , y-1), 0)

targetNumber = 368078

coordX = 0
coordY = 0
currentNumber = 1

numIncreases = 1
lastIncreased = 'y'
totalIncreases = 0
addOrSubtract = 'add'
coordinateMap = {(0, 0): 1}
finalNumber = 0
while currentNumber < targetNumber:
    currentNumber += 1
    if lastIncreased == 'y':
        if addOrSubtract == 'add':
            coordX += 1
        else:
            coordX -= 1
    else:
        if addOrSubtract == 'add':
            coordY += 1
        else:
            coordY -= 1
    totalIncreases += 1

    summedNumber = calculateSum(coordinateMap, coordX, coordY)
    coordinateMap[(coordX, coordY)] = summedNumber
    if (summedNumber > targetNumber) and (finalNumber == 0):
        finalNumber = summedNumber

    if totalIncreases == numIncreases:
        if lastIncreased == 'y':
            lastIncreased = 'x'
        else:
            lastIncreased = 'y'
    if totalIncreases == 2*numIncreases:
        if lastIncreased == 'y':
            lastIncreased = 'x'
        else:
            lastIncreased = 'y'
        if addOrSubtract == 'add':
            addOrSubtract = 'subtract'
        else:
            addOrSubtract = 'add'
        numIncreases += 1
        totalIncreases = 0

print currentNumber
print coordX
print coordY
print finalNumber