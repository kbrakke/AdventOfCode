
program_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
test_program_list = ['a', 'b', 'c', 'd', 'e']

dances = []
seen_dances = set()

seen_dances.add("".join(program_list))
dances.append("".join(program_list))

steps = open('day16Input.txt').readline().split(',')
test_steps = ['s1', 'x3/4', 'pe/b']

def spin(list, number):
    return list[-number:] + list[:-number]

def exchange(list, a, b):
    list[a], list[b] = list[b], list[a]
    return list

def partner(list, a, b):
    index_a, index_b = list.index(a), list.index(b)
    return exchange(list, index_a, index_b)


def dance(list, ops):
    for op in ops:
        if op[0] == 's':
            list = spin(list, int(op[1:]))
        elif op[0] == 'x':
            args = op[1:].split('/')
            list = exchange(list, int(args[0]), int(args[1]))
        elif op[0] == 'p':
            args = op[1:].split('/')
            list = partner(list, args[0], args[1])
    return list

current_dance = dance(program_list, steps)
print("".join(current_dance))
while "".join(current_dance) not in seen_dances:
    seen_dances.add("".join(current_dance))
    dances.append("".join(current_dance))
    current_dance = dance(current_dance, steps)

print("".join(dances[(1000000000 % len(dances))]))



