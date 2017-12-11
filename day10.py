import functools

jumps = [187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216]
#ascii_jumps = "187,254,0,81,169,219,1,190,19,102,255,56,46,32,2,216"
ascii_jumps = ""
part_2_jumps = [ord(char) for char in ascii_jumps]
part_2_jumps = part_2_jumps + [17, 31, 73, 47, 23]
#part_2_jumps = [17, 31, 73, 47, 23]
knot_list = list(range(0, 256))
index = 0
skip = 0


def reverse_sublist(input_list, index, end):
    if end < index:
        end_length = len(input_list) - index
        sublist = list(reversed(input_list[index:] + input_list[:end]))
        return sublist[end_length:] + input_list[end:index] + sublist[:end_length]
    elif (end == index) and (jump != 0):
        sublist = list(reversed(input_list[index:] + input_list[:end]))
        return sublist[-index:] + sublist[:-index]
    else:
        return input_list[ :index] + list(reversed(input_list[index:end])) + input_list[end:]

for jump in jumps:
    end = (index + jump) % len(knot_list)
    knot_list = reverse_sublist(knot_list, index, end)
    index = (index + jump + skip) % len(knot_list)
    skip += 1

print(knot_list[0] * knot_list[1])

index = 0
jump = 0
knot_list = list(range(256))
for round in range(64):
    for jump in part_2_jumps:
        end = (index + jump) % len(knot_list)
        knot_list = reverse_sublist(knot_list, index, end)
        index = (index + jump + skip) % len(knot_list)
        skip += 1

xor_list = []
for i in range(0, int(len(knot_list)/16)):
    values = knot_list[i * 16 : (i+1) * 16]
    xor_value = functools.reduce(lambda x, y: x ^ y, values)
    xor_list.append(xor_value)

return_str = ""
for hex_value in xor_list:
    return_str += hex(hex_value)[2:].zfill(2)
print(return_str)

