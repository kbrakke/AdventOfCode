import re

print("Advent of Code Day 2")
lineRegex = re.compile('(\d+)-(\d+) ([a-zA-Z]): (\w+)')
correct = 0
correct2 = 0
for line in open('/home/kbrakke/personal/AdventOfCode/AOC-2020/input/02/02-input.txt'):
  lineMatch = lineRegex.search(line)
  (first, alterante, character, password) = lineMatch.group(1,2,3,4)
  if int(alterante) >= password.count(character) >= int(first):
    correct += 1
  if (password[int(first)-1] == character) ^ (password[int(alterante)-1] == character):
    correct2 += 1
print("Correct passwords: ", correct)
print("Part 2 correct passwords: ", correct2)