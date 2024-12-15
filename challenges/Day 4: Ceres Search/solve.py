input_path = 'challenges/Day 4: Ceres Search/input'
from utils import dict_from_file, coords
_dict = dict_from_file(input_path)

part_1, word = 0, 'XMAS'

def match_from(coor, row, col):
    word_found = ''
    for i in range(len(word)):
       _r, _c = row + (i * coor[0]), col + (i * coor[1])
       if _r < 0 or _r >= len(_dict) or _c < 0 or _c >= len(_dict[0]): return False
       word_found += _dict[_r][_c]
    
    return word_found == word

matchs = lambda row, col: len(list(filter(lambda coor: match_from(coor, row, col), coords)))

for row in range(len(_dict)): 
    for col in range(len(_dict[row])):
        if _dict[row][col] == word[0]: part_1 += matchs(row, col)

print('Part 1: ', part_1)