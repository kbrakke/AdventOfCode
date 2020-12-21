class instruction:
  def __init__(self, op, arg):
    self.op = op
    self.arg = arg

  def getOp(self):
    return self.op

  def getArg(self):
    return self.arg

  def __str__(self):
    return str.format("{} {}", self.op, self.arg)

class processor:
  def __init__(self, instructions):
    self.instructions = instructions
    self.acc = 0
    self.position = 0
    self.ops = {
      'nop': self.execNop,
      'acc': self.execAcc,
      'jmp': self.execJmp
    }
  def excecuteStep(self):
    op = self.instructions[self.position]
    self.ops[op.getOp()](op.getArg())

  def execNop(self, value):
    self.position += 1

  def execAcc(self, value):
    self.position += 1
    self.acc += value

  def execJmp(self, value):
    self.position += value

  def getAcc(self):
    return self.acc

  def getPosition(self):
    return self.position


