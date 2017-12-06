initial_databanks = [4,1,15,12,0,9,9,5,5,8,7,3,14,5,12,3]
seen_arraginments = set()
seen_arraginments.add(str(initial_databanks))

def find_max_index(list):
    max = 0
    for i in range(len(list)):
        if list[i] > list[max]:
            max = i
    return max

def distribute_blocks(index, databanks):
    blocks = databanks[index]
    databanks[index] = 0
    index += 1
    while blocks > 0:
        databanks[index % len(databanks)] += 1
        blocks -= 1
        index += 1
    return databanks

count = 0
seen_before = False
seen_arraginment = ""
new_databanks = distribute_blocks(find_max_index(initial_databanks), initial_databanks)
count += 1
if str(new_databanks) in seen_arraginments:
    seen_before = True
else:
    seen_arraginments.add(str(new_databanks))

while not seen_before:
    new_databanks = distribute_blocks(find_max_index(initial_databanks), initial_databanks)
    count += 1
    if str(new_databanks) in seen_arraginments:
        seen_before = True
        seen_arraginment = str(new_databanks)
    else:
        seen_arraginments.add(str(new_databanks))

loop_size = 0
loop_complete = False
new_databanks = distribute_blocks(find_max_index(initial_databanks), initial_databanks)
loop_size += 1
if str(new_databanks) == seen_arraginment:
    loop_complete = True

while not loop_complete:
    new_databanks = distribute_blocks(find_max_index(initial_databanks), initial_databanks)
    loop_size += 1
    if str(new_databanks) == seen_arraginment:
        loop_complete = True

print(count)
print(loop_size)