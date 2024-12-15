input_path = 'challenges/Day 3: Mull It Over/input'
from functools import reduce; import re

pattern = r"mul\(\d{1,3},\d{1,3}\)"
pattern_with_do_s = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
part_1, part_2, must = 0, 0, True
with open(input_path) as f:
    for line in f:
        for match in re.findall(pattern_with_do_s, line[:-1]):
            if match == 'do()': must = True; continue
            if match == 'don\'t()': must = False; continue
            if must: part_2 += reduce(lambda x, y: x * y, list(map(int, match[4:-1].split(','))))
        for match in re.findall(pattern, line[:-1]): part_1 += reduce(lambda x, y: x * y, list(map(int, match[4:-1].split(','))))
            
print('Part 1: ', part_1)
print('Part 2: ', part_2)