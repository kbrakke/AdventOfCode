string = open('day9Input.txt').readline()
#string = "{{<a!>},{<a!>},{<a!>},{<ab>}}"
#string = "{{<!!>},{<!!>},{<!!>},{<!!>}}"

mode = 'normal'
previous_mode = ''
group_depth = 0
total_score = 0
garbage_count = 0
for char in string:
    if mode == 'ignore':
        mode = previous_mode
    elif mode == 'garbage':
        if char == '!':
            previous_mode = mode
            mode = 'ignore'
        elif char == '>':
            mode = 'normal'
        else:
            garbage_count += 1
    elif mode == 'normal':
        if char == '{':
            group_depth += 1
        elif char == '!':
            previous_mode = mode
            mode = 'ignore'
        elif char == '<':
            previous_mode = mode
            mode = 'garbage'
        elif char == '}':
            total_score += group_depth
            group_depth -= 1

print(total_score)
print(garbage_count)