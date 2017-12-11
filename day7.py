import re

class Node(object):
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = []
        if children is not None:
            for child in children:
                self.children.append(child)
    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_children(self):
        return self.children

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return "{0} ({1}) -> {2}".format(self.name, self.weight, self.children)

line_regex = re.compile(r"""([a-z]+) \((\d+)\)(?: -> )?(.*)""")
node_list = []
for line in open('day7Input.txt'):
    result = line_regex.match(line)
    if not result:
        print("Something went wrong")
        print(line)
    children = []
    if result.group(3):
        children = result.group(3).split(', ')

    node_list.append(Node(result.group(1), int(result.group(2)), children))

with_child = list(filter(lambda node: len(node.get_children()) > 0, node_list))
children_list = list(map(lambda node: node.get_children(), with_child))
children = set([child for children in children_list for child in children])

base = list(filter(lambda node : node.get_name() not in children, with_child))
bottom_node = base.pop()
current_node = bottom_node


print(bottom_node.get_name())


def find_node_by_name(name):
    for node in node_list:
        if node.get_name() == name:
            return node
    print("I can't find shit")


def get_child_weights(node):
    print("getting weights for node {} ({}) -> {}". format(node.get_name(), node.get_weight(), node.get_children()))
    child_weights = []
    for child_name in node.get_children():
        this_child_weight = get_child_weights(find_node_by_name(child_name))
        child_weights.append(tuple(this_child_weight, child_name))
    if len(set(child_weights)) > 1:

    return total_weight

print(get_child_weights(bottom_node))