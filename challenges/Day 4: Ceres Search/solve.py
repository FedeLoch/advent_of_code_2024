input_path = 'challenges/Day 4: Ceres Search/input'
from utils import dict_from_file, coords
_dict = dict_from_file(input_path)

part_1, part_2, word, MS, SM = 0, 0, 'XMAS', 'MS', 'SM'

is_valid = lambda _r, _c: False if _r < 0 or _r >= len(_dict) or _c < 0 or _c >= len(_dict[0]) else True

def match_from(coor, row, col):
    word_found = ''
    for i in range(len(word)):
       _r, _c = row + (i * coor[0]), col + (i * coor[1])
       if not is_valid(_r, _c): return False
       word_found += _dict[_r][_c]

    return word_found == word

matchs = lambda row, col: len(list(filter(lambda coor: match_from(coor, row, col), coords)))
is_possible = lambda row, col: is_valid(row-1, col-1) and is_valid(row+1, col+1) and is_valid(row+1, col-1) and is_valid(row-1, col+1)
                          
def is_xmas(row, col):
    from_right_up = _dict[row - 1][col - 1] + _dict[row + 1][col + 1]
    from_right_down = _dict[row + 1][col - 1] + _dict[row - 1][col + 1]

    return (from_right_up == MS or from_right_up == SM) and (from_right_down == MS or from_right_down == SM)

for row in range(len(_dict)): 
    for col in range(len(_dict[row])):
        if _dict[row][col] == word[0]: part_1 += matchs(row, col)
        if _dict[row][col] == 'A' and is_possible(row, col):
            part_2 += 1 if is_xmas(row, col) else 0

print('Part 1: ', part_1)
print('Part 2: ', part_2)