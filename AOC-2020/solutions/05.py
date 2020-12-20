import os
print("Advent of code day 5")


def parsePass(boardingPass):
    rowString = boardingPass[:7]
    columnString = boardingPass[7:]
    rowRange = range(128)
    columnRange = range(8)
    row = 0
    column = 0
    for char in list(rowString):
        if char == 'F':
            rowRange = rowRange[:int(len(rowRange)/2)]
        elif char == 'B':
            rowRange = rowRange[int(len(rowRange)/2):]
        else:
            print('Unknown {char} in row string')
    row = rowRange[0]
    for char in list(columnString):
        if char == 'L':
            columnRange = columnRange[:int(len(columnRange)/2)]
        elif char == 'R':
            columnRange = columnRange[int(len(columnRange)/2):]
        else:
            print('Unknown {char} in column string')
    column = columnRange[0]
    return (row, column)


maxPass = 0
takenSeats = []
allSeats = []
for row in range(1, 127):
    for col in range(8):
        allSeats.append(row*8 + col)
inputdir = os.getcwd() + '/AOC-2020/input/05/05-input.txt'
for line in open(inputdir):
    (row, col) = parsePass(line.rstrip())
    num = row * 8 + col
    takenSeats.append(num)
    if num > maxPass:
        maxPass = num

for seat in allSeats:
    if seat not in takenSeats:
        if seat + 1 in takenSeats and seat-1 in takenSeats:
            print("Possible Seat: ", seat)

print("Seat ID: ", maxPass)
