send_queue = [[], []]
registers = [{'p': 0}, {'p': 1}]
program = []
position = [0, 0]
waiting = [False, False]
program1_sent_count = 0

def get_value(program, value):
    global registers
    if value.isalpha():
        return registers[program].get(value, 0)
    else:
        return int(value)

def next_step(program):
    global position
    position[program] += 1


def snd(program, x):
    global send_queue
    global program1_sent_count
    send_queue[program].append(get_value(program, x))
    if program == 1:
        program1_sent_count += 1
    next_step(program)

def set(program, register_name, value):
    global registers
    registers[program][register_name] = get_value(program, value)
    next_step(program)

def add(program, register_name, value):
    global registers
    current_value = registers[program].get(register_name, 0)
    registers[program][register_name] = get_value(program, value) + current_value
    next_step(program)

def mul(program, register_name, value):
    global registers
    current_value = registers[program].get(register_name, 0)
    registers[program][register_name] = get_value(program, value) * current_value
    next_step(program)

def mod(program, register_name, value):
    global registers
    current_value = registers[program].get(register_name, 0)
    registers[program][register_name] = current_value % get_value(program, value)
    next_step(program)

def rcv(program, x):
    global send_queue
    global waiting
    global registers
    message_queue = send_queue[1 - program]
    if len(message_queue) == 0:
        waiting[program] = True
    else:
        registers[program][x] = message_queue[0]
        send_queue[1 - program] = message_queue[1:]
        next_step(program)


def jgz(program, register, jump):
    global position
    if get_value(program, register) > 0:
        position[program] += get_value(program, jump)
    else:
        next_step(program)

ops = {
    'snd' : lambda program, x: snd(program, x[0]),
    'set' : lambda program, args: set(program, args[0], args[1]),
    'add' : lambda program, args: add(program, args[0], args[1]),
    'mul' : lambda program, args: mul(program, args[0], args[1]),
    'mod' : lambda program, args: mod(program, args[0], args[1]),
    'rcv' : lambda program, x: rcv(program, x[0]),
    'jgz' : lambda program, args: jgz(program, args[0], args[1])
}

for line in open('day18Input.txt'):
    program.append(line.split())

print(program)

while not (waiting[0] and waiting[1]):
    ops[program[position[0]][0]](0, program[position[0]][1:])
    ops[program[position[1]][0]](1, program[position[1]][1:])

print(program1_sent_count)