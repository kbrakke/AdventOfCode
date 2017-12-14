layer_dict = {}

for line in open('day13Input.txt'):
    layer = line.split(": ")
    layer_dict[int(layer[0])] = int(layer[1])

def calculate_severity(delay, stealth = True):
    severity = 0
    for key in layer_dict.keys():
        layer_cycle = layer_dict[key]
        if ((delay + key) % ((layer_cycle - 1) * 2)) == 0:
            if key == 0 and stealth:
                return 1
            severity += key * layer_cycle
    return severity


current_severity = calculate_severity(0, False)
print(current_severity)
start_time = 1
while current_severity > 0:
    current_severity = calculate_severity(start_time)
    start_time += 1

print(start_time - 1)