__author__ = 'Kris'

inputFile = open('day5Input.txt')
numArrayPart1 = []
numArrayPart2 = []
for num in inputFile:
    numArrayPart1.append(int(num))
    numArrayPart2.append(int(num))

i = 0
count = 0
while (i >= 0) and (i < len(numArrayPart1)):
    count += 1
    numArrayPart1[i] = numArrayPart1[i] + 1
    i += numArrayPart1[i] - 1

print count

i = 0
count = 0
while (i >= 0) and (i < len(numArrayPart2)):
    count += 1
    jump = numArrayPart2[i]
    if jump >= 3:
        numArrayPart2[i] = jump - 1
    else:
        numArrayPart2[i] = jump + 1
    i += jump

print count