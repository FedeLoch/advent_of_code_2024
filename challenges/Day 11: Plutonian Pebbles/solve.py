input_path = 'challenges/Day 11: Plutonian Pebbles/input'

line = list(map(int, open(input_path).readline().rstrip().split(' ')))

def blink(_line):
    __line = []
    for i in range(len(_line)):
        elem, _str = _line[i], str(_line[i])
        if elem == 0: __line.append(1); continue
        if len(_str) % 2 == 0:
            left, right = _str[:len(_str)//2], _str[len(_str)//2:]
            __line.append(int(left)); __line.append(int(right)); continue
        __line.append(elem * 2024)
    return __line

for i in range(25):
    line = blink(line)

part_1 = len(line)
print(f'Part 1: {part_1}')
