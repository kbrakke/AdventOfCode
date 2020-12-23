import os, math, re

infile = os.getcwd() + '/input/12/input.txt'

direction = 0
x = 0
y = 0
waypointX = 10
waypointY = 1
part2x = 0
part2y = 0


commandRegex = re.compile("([NSEWLRF])(\d+)")
for line in open(infile):
  match = commandRegex.match(line)
  if match:
    (command, amount) = match.groups()
    amount = int(amount)
    if command == "L":
      direction = direction + math.radians(amount)
      if amount == 0 or amount == 360:
        continue
      elif amount == 90:
        oldX = waypointX
        oldY = waypointY
        waypointX = -1 * oldY
        waypointY = oldX
      elif amount == 180:
        waypointX = -1 * waypointX
        waypointY = -1 * waypointY
      elif amount == 270:
        oldX = waypointX
        oldY = waypointY
        waypointX = oldY
        waypointY = -1 * oldX
    elif command == "R":
      direction = direction - math.radians(amount)
      if amount == 0 or amount == 360:
        continue
      elif amount == 90:
        oldX = waypointX
        oldY = waypointY
        waypointX = oldY
        waypointY = -1 * oldX
      elif amount == 180:
        waypointX = -1 * waypointX
        waypointY = -1 * waypointY
      elif amount == 270:
        oldX = waypointX
        oldY = waypointY
        waypointX = -1 * oldY
        waypointY = oldX
    elif command == "N":
      y += amount
      waypointY += amount
    elif command == "S":
      y -= amount
      waypointY -= amount
    elif command == "E":
      x += amount
      waypointX += amount
    elif command == "W":
      x -= amount
      waypointX -= amount
    elif command == "F":
      x += int(float(amount) * math.cos(direction))
      y += int(float(amount) * math.sin(direction))
      part2x += waypointX * amount
      part2y += waypointY * amount

print(str.format("Part 1 Final Position X: {} Y: {} Distance: {}", x, y, abs(x) + abs(y)))
print(str.format("Part 2 Final Position X: {} Y: {} Distance: {}", part2x, part2y, abs(part2x) + abs(part2y)))