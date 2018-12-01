
jumps = 369
#jumps = 3
buffer = [0]
position = 0

for i in range(1,2018):
    position = (position + jumps) % len(buffer)
    position += 1
    buffer.insert(position, i)

i = buffer.index(2017) +1
print(buffer[i])

value_after_0 = 0
position = 0
for i in range(1,50000001):
    position = (position + jumps) % i
    if position == 0:
        value_after_0 = i
    position += 1

print(value_after_0)

