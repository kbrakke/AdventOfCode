
move_array = open('day11Input.txt').readline().split(',')
#move_array = "se,sw,se,sw,sw".split(',')
move_dict = {'n' : 0, 's' : 0, 'ne' : 0, 'nw' : 0, 'se' : 0, 'sw' : 0}
opposite_dict = {'n' : 's', 's' : 'n', 'ne' : 'sw', 'nw' : 'se', 'se' : 'nw', 'sw' : 'ne'}
max_distance = 0

def condensed_add(move, dictionary):
    if dictionary[opposite_dict[move]] > 0:
        dictionary[opposite_dict[move]] -= 1
    else:
        dictionary[move] += 1

def get_distance(dictionary):
    distance = 0
    if dictionary['s'] > 0:
        distance += dictionary['s']
        if dictionary['nw'] > 0:
            distance += dictionary['nw'] + dictionary['sw']
            if dictionary['nw'] > dictionary['sw']:
                distance -= dictionary['sw']
            else:
                distance -= dictionary['nw']
        elif dictionary['ne'] > 0:
            distance += dictionary['ne'] + dictionary['se']
            if dictionary['ne'] > dictionary['se']:
                distance -= dictionary['se']
            else:
                distance -= dictionary['ne']
        else:
            distance += dictionary['se'] + dictionary['sw']
            if dictionary['se'] > dictionary['sw']:
                distance -= dictionary['sw']
            else:
                distance -= dictionary['se']
    else:
        distance += dictionary['n']
        if dictionary['sw'] > 0:
            distance += dictionary['nw'] + dictionary['sw']
            if dictionary['nw'] > dictionary['sw']:
                distance -= dictionary['sw']
            else:
                distance -= dictionary['nw']
        elif dictionary['se'] > 0:
            distance += dictionary['ne'] + dictionary['se']
            if dictionary['ne'] > dictionary['se']:
                distance -= dictionary['se']
            else:
                distance -= dictionary['ne']
        else:
            distance += dictionary['ne'] + dictionary['nw']
            if dictionary['ne'] > dictionary['nw']:
                distance -= dictionary['nw']
            else:
                distance -= dictionary['ne']
    return distance


for move in move_array:
    condensed_add(move, move_dict)
    distance = get_distance(move_dict)
    if distance > max_distance:
        max_distance = distance

print(get_distance(move_dict))
print(max_distance)