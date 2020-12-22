import os, math

infile = os.getcwd() + '/input/10/input.txt'
numbers = [0]
for line in open(infile):
  numbers.append(int(line))

numbers.append(max(numbers) + 3)
numbers.sort()
offByOneCount = 0
offByThreeCount = 0
nonEssentialClusters = []
nonEssentialCluster = []
for i in range(len(numbers)-1):
  diff = numbers[i+1] - numbers[i]
  if diff == 0 or diff > 3:
    print(str.format("Something is weird lower number {} higher number {}", numbers[i], numbers[i + 1]))
  if diff == 1:
    offByOneCount += 1
    if numbers[i] == 0:
      continue
    elif numbers[i] - numbers[i-1] == 1:
      nonEssentialCluster.append(numbers[i])
  elif diff == 3:
    nonEssentialClusters.append(nonEssentialCluster)
    nonEssentialCluster = []
    offByThreeCount += 1
  else:
    offByTwoCount += 1
print(str.format("Multiplying {} and {} to get {}", offByOneCount, offByThreeCount, offByOneCount * offByThreeCount))
print(nonEssentialClusters)
combos = 1
for cluster in nonEssentialClusters:
  if len(cluster) < 3:
    combos = combos * 2**len(cluster)
  elif len(cluster) >= 3:
    combos = combos * (2**len(cluster) - 1)
print(combos)