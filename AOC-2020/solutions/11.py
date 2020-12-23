import os, math

infile = os.getcwd() + '/input/11/input.txt'

directions = ["N", "S", "E", "W", "NE", "SE", "NW", "SW"]

def directionalCheck(mode, row, col, seating):
  occupiedSeats = 0
  for direction in directions:
    #   0 1 2
    # 0 . ^ .
    # 1 . | .
    # 2 . S .
    if direction == "N":
      rowCheck = row - 1
      if rowCheck >= 0:
        seat = seating[rowCheck][col]
        while rowCheck > 0 and seat not in ["L", "#"]:
          rowCheck -= 1
          seat = seating[rowCheck][col]
        if seat == "#":
          if mode == "L":
            return "L"
          occupiedSeats += 1
    #   0 1 2
    # 0 . S .
    # 1 . | .
    # 2 . v .
    if direction == "S":
      rowCheck = row + 1
      if rowCheck < len(seating):
        seat = seating[rowCheck][col]
        while rowCheck < len(seating) - 1 and seat not in ["L", "#"]:
          rowCheck += 1
          seat = seating[rowCheck][col]
        if seat == "#":
          if mode == "L":
            return "L"
          occupiedSeats += 1
    #   0 1 2
    # 0 . . .
    # 1 S - >
    # 2 . . .
    if direction == "E":
      colCheck = col + 1
      if colCheck < len(seating[row]):
        seat = seating[row][colCheck]
        while colCheck < len(seating[row]) - 1 and seat not in ["L", "#"]:
          colCheck += 1
          seat = seating[row][colCheck]
        if seat == "#":
          if mode == "L":
            return "L"
          occupiedSeats += 1
    #   0 1 2
    # 0 . . .
    # 1 < - S
    # 2 . . .
    if direction == "W":
      colCheck = col - 1
      if colCheck >= 0:
        seat = seating[row][colCheck]
        while colCheck > 0 and seat not in ["L", "#"]:
          colCheck -= 1
          seat = seating[row][colCheck]
        if seat == "#":
          if mode == "L":
            return "L"
          occupiedSeats += 1
    #   0 1 2
    # 0 . . /
    # 1 . / .
    # 2 S . .
    if direction == "NE":
      rowCheck = row - 1
      colCheck = col + 1
      if colCheck < len(seating[row]) and rowCheck >= 0:
        seat = seating[rowCheck][colCheck]
        while colCheck < len(seating[row]) -1 and rowCheck > 0 and seat not in ["L", "#"]:
          colCheck += 1
          rowCheck -= 1
          seat = seating[rowCheck][colCheck]
        if seat == "#":
          if mode == "L":
            return "L"
          occupiedSeats += 1
    #   0 1 2
    # 0 \ . .
    # 1 . \ .
    # 2 . . S
    if direction == "NW":
      rowCheck = row - 1
      colCheck = col - 1
      if colCheck >= 0 and rowCheck >= 0:
        seat = seating[rowCheck][colCheck]
        while colCheck > 0 and rowCheck > 0 and seat not in ["L", "#"]:
          colCheck -= 1
          rowCheck -= 1
          seat = seating[rowCheck][colCheck]
        if seat == "#":
          if mode == "L":
            return "L"
          occupiedSeats += 1
    #   0 1 2
    # 0 S . .
    # 1 . \ .
    # 2 . . \
    if direction == "SE":
      rowCheck = row + 1
      colCheck = col + 1
      if colCheck < len(seating[row]) and rowCheck < len(seating):
        seat = seating[rowCheck][colCheck]
        while colCheck < len(seating[row]) - 1 and rowCheck < len(seating) - 1 and seat not in ["L", "#"]:
          colCheck += 1
          rowCheck += 1
          seat = seating[rowCheck][colCheck]
        if seat == "#":
          if mode == "L":
            return "L"
          occupiedSeats += 1
    #   0 1 2
    # 0 . . S
    # 1 . / .
    # 2 / . .
    if direction == "SW":
      rowCheck = row + 1
      colCheck = col - 1
      if colCheck >= 0 and rowCheck < len(seating):
        seat = seating[rowCheck][colCheck]
        while colCheck > 0 and rowCheck < len(seating) - 1 and seat not in ["L", "#"]:
          colCheck -= 1
          rowCheck += 1
          seat = seating[rowCheck][colCheck]
        if seat == "#":
          if mode == "L":
            return "L"
          occupiedSeats += 1
  if mode == "#":
    #print(str.format("Seat r{}c{} saw {} entries", row, col, occupiedSeats))
    if occupiedSeats >= 5:
      return "L"
  return "#"
  

def checkSeat(row, col, seating):
  symbol = seating[row][col]
  if symbol == ".":
    return "."
  if symbol == "L":
    for checkRow in range(row -1, row+2):
      for checkCol in range(col -1, col+2):
        #print(str.format("Checking row: {} col: {}", checkRow, checkCol))
        if checkRow < 0 or checkRow >= len(seating):
          continue
        elif checkCol < 0 or checkCol >= len(seating[row]):
          continue
        elif row == checkRow and col == checkCol:
          continue
        else:
          if seating[checkRow][checkCol] == "#":
            return "L"
    return "#"
  if symbol == "#":
    occupiedCount = 0
    for checkRow in range(row -1, row+2):
      for checkCol in range(col -1, col+2):
        #print(str.format("Checking row: {} col: {}", checkRow, checkCol))
        if checkRow < 0 or checkRow >= len(seating):
          continue
        elif checkCol < 0 or checkCol >= len(seating[row]):
          continue
        elif row == checkRow and col == checkCol:
          continue
        else:
          if seating[checkRow][checkCol] == "#":
            occupiedCount += 1
    if occupiedCount >= 4:
      return "L"
    else:
      return "#"

def expandedCheckSeat(row, col, seating):
  symbol = seating[row][col]
  if symbol == ".":
    return "."
  return directionalCheck(symbol, row, col, seating)

iterations = 0
def runLife(seating):
  newSeating  = []
  for row_idx in range(len(seating)):
    newSeatingRow = []
    for col_idx in range(len(seating[row_idx])):
      newSeatingRow.append(checkSeat(row_idx, col_idx, seating))
    newSeating.append(newSeatingRow)
  return newSeating

def expandedRunLife(seating):
  newSeating  = []
  for row_idx in range(len(seating)):
    newSeatingRow = []
    for col_idx in range(len(seating[row_idx])):
      newSeatingRow.append(expandedCheckSeat(row_idx, col_idx, seating))
    newSeating.append(newSeatingRow)
  return newSeating



seating = []
for line in open(infile):
  seating.append(list(line.rstrip()))

sameSeats = False
expandedSeating = seating
expandedSameSeats = False
while not sameSeats:
  newSeats = runLife(seating)
  if newSeats == seating:
    sameSeats = True
  seating = newSeats

filledSeats = 0
for row in seating:
  for col in row:
    if col == "#":
      filledSeats += 1

print("Part 1 Filled seats: ", filledSeats)

while not expandedSameSeats:
  newSeats = expandedRunLife(expandedSeating)
  if newSeats == expandedSeating:
    expandedSameSeats = True
  expandedSeating = newSeats

filledSeats = 0
for row in expandedSeating:
  for col in row:
    if col == "#":
      filledSeats += 1

print("Part 2 Filled seats: ", filledSeats)