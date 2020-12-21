import os, re, sys
sys.path.insert(0, '/home/kbrakke/AdventOfCode/AOC-2020/util')
from computer import processor, instruction

def flipInstruction(instructions, pos):
  oldInstruction = instructions[pos]
  if oldInstruction.getOp() == "nop":
    if oldInstruction.getArg() == 0:
      return False
    else:
      print(str.format("Flipped {} {} to {} {}", oldInstruction.getOp(), oldInstruction.getArg(), 'jmp', oldInstruction.getArg()))
      instructions[pos] = instruction('jmp', oldInstruction.getArg())
      return True
  elif oldInstruction.getOp() == 'jmp':
    print(str.format("Flipped {} {} to {} {}", oldInstruction.getOp(), oldInstruction.getArg(), 'nop', oldInstruction.getArg()))
    instructions[pos] = instruction('nop', oldInstruction.getArg())
    return True
  else:
    return False

infile = os.getcwd() + '/input/08/input.txt'
instructionRegex = re.compile("(\w{3}) ([+-]\d+)")
instructionsList = []
possibleInstructionLists = []
for line in open(infile):
  instructionMatch = instructionRegex.search(line)
  if instructionMatch:
    instructionsList.append(instruction(instructionMatch.group(1), int(instructionMatch.group(2))))

aoc_pc = processor(instructionsList)
reachedPositions = []
while True:
  position = aoc_pc.getPosition()
  if position >= len(instructionsList):
    break
  if position in reachedPositions:
    print(str.format("Executing step {} again.", position))
    print(str.format("Accumultaor value {}", aoc_pc.getAcc()))
    break
  else:
    reachedPositions.append(position)
    aoc_pc.excecuteStep()

reachedPositions.reverse()
finished = False
for updatePositions in reachedPositions:
  if finished:
    break
  print("Testing instructions while flipping position ", updatePositions)
  if flipInstruction(instructionsList, updatePositions):
    currProcessor = processor(instructionsList)
    reachedPositions = []
    while True:
      position = currProcessor.getPosition()
      if position >= len(instructionsList):
        print("Finished execution")
        finished = True
        print(str.format("Final values {}", currProcessor.getAcc()))
        break
      if position in reachedPositions:
        flipInstruction(instructionsList, updatePositions)
        break
      else:
        reachedPositions.append(position)
        currProcessor.excecuteStep()



