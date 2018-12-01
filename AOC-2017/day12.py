import re
in_group = set()
groups = []

pipes = {}
programs_regex = re.compile(r"""(\d+) <-> (.*)""")

for line in open('day12Input.txt'):
    matches = programs_regex.match(line)
    pipes[matches.group(1)] = matches.group(2).split(', ')

def find_group(inital_pipe):
    talk_to_pipe = set()
    pipes_to_add = [inital_pipe]
    while len(pipes_to_add) > 0:
        talk_to_pipe.update(pipes_to_add)
        list_of_children = [pipes[pipe] for pipe in pipes_to_add]
        pipes_to_add = set([child for child_list in list_of_children for child in child_list]).difference(talk_to_pipe)
    return talk_to_pipe


zero_group = find_group('0')
in_group.update(zero_group)
groups.append(zero_group)

print(len(zero_group))

while len(in_group) < len(pipes.keys()):
    remaining_pipes = set(pipes.keys()).difference(in_group)
    new_group = find_group(remaining_pipes.pop())
    in_group.update(new_group)
    groups.append(new_group)

print(len(groups))