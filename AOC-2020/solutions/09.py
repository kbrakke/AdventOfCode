import os,itertools

preamble = 25
window = 25

def isValid(num, checkList):
  for pair in itertools.permutations(checkList, 2):
    if pair[0] + pair[1] == num:
      return True
  return False
infile = os.getcwd() + '/input/09/input.txt'
numbers = []
for line in open(infile):
  numbers.append(int(line.rstrip()))

invalidNumber = 0
for i in range(len(numbers)):
  if i < preamble:
    pass
  elif isValid(numbers[i], numbers[i-window:i]):
    pass
  else:
    invalidNumber = numbers[i]
    print(str.format("Number {} is invalid", numbers[i]))
    break

endPos = 2
for i in range(len(numbers)):
  if(endPos > len(numbers)):
    print("Something is wrong, looking past the dataset")
  while sum(numbers[i:endPos]) < invalidNumber:
    endPos += 1
  if sum(numbers[i:endPos]) == invalidNumber:
    print(numbers[i:endPos])
    print(str.format("Found list, solution {}", min(numbers[i:endPos]) + max(numbers[i:endPos])))
    break
