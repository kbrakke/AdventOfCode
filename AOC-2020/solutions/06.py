import os

inputdir = os.getcwd() + '/AOC-2020/input/06/06-input.txt'

answers = []
answersCount = 0
questionSet = set()
answerSets = []
partTwoCount = 0
for line in open(inputdir):
  cleanLine = line.rstrip()
  if cleanLine == "":
    answers.append(questionSet)
    answersCount += len(questionSet)
    finalUnion = set.intersection(*answerSets)
    partTwoCount += len(finalUnion)
    questionSet = set()
    answerSets = []
  else:
    singleSet = set()
    for char in list(cleanLine):
      questionSet.add(char)
      singleSet.add(char)
    answerSets.append(singleSet)
answers.append(questionSet)
answersCount += len(questionSet)
finalUnion = set.intersection(*answerSets)
partTwoCount += len(finalUnion)

print("Number of answers: ", answersCount)
print("Part 2: ",partTwoCount)