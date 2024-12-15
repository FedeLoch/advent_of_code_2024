input_path = 'challenges/Day 2: Red-Nosed Reports/input'

def all_is_in(list, dir):
    for i in range(1, len(list)):
        if list[i-1] == list[i] or(list[i-1] - list[i]) not in dir: return False
    return True

is_safe = lambda list: all_is_in(list, range(-3, 1)) or all_is_in(list, range(0, 4))

def is_safe_with_tolerance(list):
    for i in range(len(list)):
        l2 = list.copy(); l2.pop(i)
        if is_safe(l2): return True
    
    return False

part_1, part_2 = 0, 0
with open(input_path) as f:
    for line in f:
        lvls = list(map(int, line[:-1].split(' ')))
        part_1 += 1 if is_safe(lvls) else 0; part_2 +=1 if is_safe_with_tolerance(lvls) else 0

print('Part 1: ', part_1)
print('Part 2: ', part_2)