from functools import reduce

print("Advent of code day 3")
movements = [(1, 1), (3, 1), (5,1), (7,1), (1,2)]

slope = []
totalTreesHit = []
for line in open('/home/kbrakke/personal/AdventOfCode/AOC-2020/input/03/03-input.txt'):
  slope.append(list(line.rstrip()))
for movement in movements:
  location = (0, 0) # x, y
  treesHit = 0
  openSpaces = 0
  print("Movement: Right {:d}, down {:d}".format(movement[0], movement[1]))
  while location[1] < len(slope):
    space = slope[location[1]][location[0]]
    if space == '.':
      openSpaces += 1
    elif space == '#':
      treesHit += 1
    location = ((location[0] + movement [0]) % len(slope[0]), location[1] + movement[1])

  print("Trees hit: ", treesHit)
  totalTreesHit.append(treesHit)
print("Total Trees Hit: ", totalTreesHit)
result = reduce((lambda x, y: x * y), totalTreesHit)
print("Final Number: ", result)
