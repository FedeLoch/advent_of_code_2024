input_path = 'challenges/Day 2: Red-Nosed Reports/input'

def all_is_in(list, dir):
    for i in range(1, len(list)):
        if list[i-1] == list[i] or(list[i-1] - list[i]) not in dir: return False
    return True

is_safe = lambda list: all_is_in(list, range(-3, 1)) or all_is_in(list, range(0, 4))

part_1 = 0
with open(input_path) as f:
    for line in f: part_1 += 1 if is_safe(list(map(int, line[:-1].split(' ')))) else 0

print('Part 1: ', part_1)
print('Part 2: ', part_2)