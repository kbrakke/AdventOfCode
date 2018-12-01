__author__ = 'Kris'

checkSumSub = 0
checkSumDiv = 0
for line in open('day2Input.txt'):
    lowest = 10000000
    highest = 0
    numArray = line.split()
    for i in range(len(numArray)):
        number = int(numArray[i])
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
        for j in range(i+1,len(numArray)):
            firstInt = int(numArray[i])
            secondInt = int(numArray[j])
            if (firstInt % secondInt) == 0:
                checkSumDiv += firstInt/secondInt
            elif (secondInt % firstInt) == 0:
                checkSumDiv += secondInt/firstInt
    checkSumSub += highest - lowest

print checkSumSub
print checkSumDiv