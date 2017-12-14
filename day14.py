import functools

test_input = "flqrgnkx"
input_string = "hwlqcszp"

hash_list = []
binary_list = []

def reverse_sublist(input_list, index, jump):
    end = (index + jump) % len(input_list)
    if end < index:
        end_length = len(input_list) - index
        sublist = list(reversed(input_list[index:] + input_list[:end]))
        return sublist[end_length:] + input_list[end:index] + sublist[:end_length]
    elif (end == index) and (jump != 0):
        sublist = list(reversed(input_list[index:] + input_list[:end]))
        return sublist[-index:] + sublist[:-index]
    else:
        return input_list[ :index] + list(reversed(input_list[index:end])) + input_list[end:]


def get_knot_hash(input_string):
    jumps = [ord(char) for char in input_string] + [17, 31, 73, 47, 23]
    index = 0
    skip = 0
    knot_list = list(range(0, 256))
    for round in range(64):
        for jump in jumps:
            knot_list = reverse_sublist(knot_list, index, jump)
            index = (index + jump + skip) % len(knot_list)
            skip += 1

    xor_list = []
    for i in range(0, int(len(knot_list) / 16)):
        values = knot_list[i * 16: (i + 1) * 16]
        xor_value = functools.reduce(lambda x, y: x ^ y, values)
        xor_list.append(xor_value)

    return_str = ""
    for hex_value in xor_list:
        return_str += hex(hex_value)[2:].zfill(2)
    return return_str

for i in range(128):
    hash_list.append(get_knot_hash("{}-{}".format(input_string, i)))

scale = 16
num_of_bits = 128
used = 0
for hash in hash_list:
    binary = bin(int(hash, scale))[2:].zfill(num_of_bits)
    binary_list.append(binary)
    used += len([i for i in str(binary) if i == '1'])

print(used)

points_in_groups = set()
groups = []
max_range = range(128)
def generate_adjcent(point):
    points = []
    (x, y) = point
    for i in [-1, 0, 1]:
        points.append((x + i, y))
        points.append((x, y + i))
        points.append((x + i, y + i))
    points = [valid_point for valid_point in points if (valid_point[0] in max_range) and (valid_point[1] in max_range) and valid_point is not point]
    return points


def add_point_and_adjcent(point, current_group):
    if point not in points_in_groups:
        points_in_groups.update(point)
    current_group.update(point)

def next_point(point):
    (x, y) = point
    y += 1
    if y > 127:
        x += 1
        y = 0
    return (x, y)


point = (0,0)
while len(points_in_groups) > used:
    current_group = set()


    groups.append(current_group)

print(len(groups))