import os, math, re

infile = os.getcwd() + '/input/13/test.txt'
lines = []
for line in open(infile):
  lines.append(line.rstrip())

time = int(lines[0])
routes = lines[1].split(',')

minWait = 1000000000000
bus_num = 0
for route in routes:
  if route == "x":
    continue
  else:
    routeNum = int(route)
    numRoutes  = int(time / routeNum)
    wait = routeNum * (numRoutes +1) - time 
    if wait < minWait:
      minWait = wait
      bus_num = routeNum

print(str.format("Min wait {}, route {}, multiplied {}", minWait, bus_num, minWait * bus_num))

def checkNum(num, timeAndOffsets):
  for (offset, time) in timeAndOffsets:
    if (num + offset) % time != 0:
      return False
  return True

numRoutes =  []
for route in routes:
  if route != "x":
    numRoutes.append(int(route))
num = max(numRoutes)
timeAndOffsets = []
for i in range(len(routes)):
  if not routes[i] == "x":
    timeAndOffsets.append((i, int(routes[i])))
found = False
print(timeAndOffsets)

while not found:
  num += 1
  if num % 100000 == 0:
    print(str.format("Checked {} numbers", num))
  found = checkNum(num, timeAndOffsets)

print(str.format("Found the number {}", num))
