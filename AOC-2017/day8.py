import re

ops = {
    '==': lambda x, y: x == y,
    '>': lambda x, y: x > y,
    '<': lambda x, y: x < y,
    '>=': lambda x, y: x >= y,
    '<=': lambda x, y: x <= y,
    '!=': lambda x, y: x != y,
    'inc': lambda x, y: x + y,
    'dec': lambda x, y: x - y
}

registers = {}
line_regex = re.compile(r"""([a-z]+) (inc|dec) ([-0-9]+) if ([a-z]+) (==|>|<|>=|<=|!=) ([-0-9]+)""")
max_value = 0

for line in open('day8Input.txt'):
    operation = line_regex.match(line)
    register = operation.group(1)
    op = operation.group(2)
    value = int(operation.group(3))
    check_regester = operation.group(4)
    check_op = operation.group(5)
    check_value = int(operation.group(6))

    current_check_register_value = registers.get(check_regester, 0)
    if ops[check_op](current_check_register_value, check_value):
        current_register_value = registers.get(register, 0)
        new_value = ops[op](current_register_value, value)
        if new_value > max_value:
            max_value = new_value
        registers[register] = new_value

print(max(registers.values()))
print(max_value)

def is_prime(num):
    for i in range (2, int(num/2)):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

for i in range(101, 140):
    print(str(i) + " "+is_prime(i))




