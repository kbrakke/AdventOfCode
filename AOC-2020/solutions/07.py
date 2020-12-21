import os, re

def checkForChild(colorList, bag):
  children = bag.getChildren()
  if len(children) == 0:
    return False
  else:
    for child in children:
      if child[0] in colorList:
        return True
  return False


def recursiveColorList(colorList, bagList, bagSet):
  if len(colorList) == 0:
    return 0
  combinedColorList = []
  filteredBagList = [ bag for bag in bagList if checkForChild(colorList, bag) ]
  for bag in filteredBagList:
    bagSet.add(bag)
  combinedColorList = [ bag.color for bag in filteredBagList ]
  return len(combinedColorList) + recursiveColorList(combinedColorList, bagList, bagSet)

def initColorList(color, bagList, bagSet):
  filteredBagList = [ bag for bag in bagList if checkForChild([color], bag) ]
  for bag in filteredBagList:
    bagSet.add(bag)
  colorList = [ bag.color for bag in filteredBagList ]
  parentCount = recursiveColorList(colorList, bagList, bagSet)
  return (len(filteredBagList) + parentCount)

def findBag(color):
  return [bag for bag in bagRules if bag.color.find(color) >= 0][0]

def countChild(bag):
  if len(bag.getChildren()) == 0:
    return 0
  count = 0
  for child in bag.children:
    count += int(child[1])
    count += int(child[1]) * countChild(findBag(child[0]))
  return count


class bag:
  def __init__(self, color, children):
    self.color = color
    #(color, number)
    self.children = children
  def getColor(self):
    return self.color
  def getChildren(self):
    return self.children
  def __str__(self):
    return str.format("Color: {}\nChildren: {}\n\n", self.color, self.children)

inputdir = os.getcwd() + '/input/07/input.txt'
goalColor = "shiny gold"
parentRegex = re.compile("(\w+ \w+) bags contain (.*).")
childRegex = re.compile("(\d+) (\w+ \w+) bag")
bagRules = []
for line in open(inputdir):
  parentMatch = parentRegex.search(line)
  if parentMatch:
    childrenStrings = parentMatch.group(2).split(", ")
    children = []
    for child in childrenStrings:
      childMatch = childRegex.search(child)
      if childMatch:
        children.append((childMatch.group(2), childMatch.group(1)))
    bagRules.append(bag(parentMatch.group(1), children))
bagSet = set()
initColorList(goalColor, bagRules, bagSet)
print("Count: ", len(bagSet))
shinyGoldBag = findBag(goalColor)
count = countChild(shinyGoldBag)
print("Total nesting: ", count)


