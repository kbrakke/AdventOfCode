last_sound = 0
registers = {}
program = []
position = 0

def get_value(value):
    global registers
    if value.isalpha():
        return registers.get(value, 0)
    else:
        return int(value)

def next_step():
    global position
    position += 1


def set_last_sound(x):
    global last_sound
    last_sound = get_value(x)
    next_step()

def set(register_name, value):
    global registers
    registers[register_name] = get_value(value)
    next_step()

def add(register_name, value):
    global registers
    current_value = registers.get(register_name, 0)
    registers[register_name] = get_value(value) + current_value
    next_step()

def mul(register_name, value):
    global registers
    current_value = registers.get(register_name, 0)
    registers[register_name] = get_value(value) * current_value
    next_step()

def mod(register_name, value):
    global registers
    current_value = registers.get(register_name, 0)
    registers[register_name] = current_value % get_value(value)
    next_step()

def rcv(x):
    global last_sound
    if get_value(x) != 0:
        print(last_sound)
        exit()
    next_step()

def jgz(register, jump):
    global position
    if get_value(register) > 0:
        position += get_value(jump)
    else:
        next_step()

ops = {
    'snd' : lambda x: set_last_sound(x[0]),
    'set' : lambda args: set(args[0], args[1]),
    'add' : lambda args: add(args[0], args[1]),
    'mul' : lambda args: mul(args[0], args[1]),
    'mod' : lambda args: mod(args[0], args[1]),
    'rcv' : lambda x: rcv(x[0]),
    'jgz' : lambda args: jgz(args[0], args[1])
}

for line in open('day18Input.txt'):
    program.append(line.split())

print(program)

while position >= 0 and position < len(program):
    print("Registers: {}".format(registers))
    print("Executing: {}".format(program[position]))
    ops[program[position][0]](program[position][1:])