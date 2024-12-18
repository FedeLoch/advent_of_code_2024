input_path = 'challenges/Day 6: Guard Gallivant/input0'

from utils import dict_from_file, DIR
guard, _dict = dict_from_file(input_path)

print('guard: ', guard)
for row in _dict:
    print(row)