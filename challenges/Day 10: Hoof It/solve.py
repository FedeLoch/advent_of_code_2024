input_path = 'challenges/Day 10: Hoof It/input'

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
trailheads, dict, memo = [], [], {}
with open(input_path) as f:
    i = 0
    for line in f:
        dict.append([int(num) for num in line[:-1]])
        for j, ch in enumerate(line.strip()):
            if ch == '0': trailheads.append((i, j))
        i += 1

def dp(pos, dict, memo):
    i, j = pos
    if dict[i][j] == 9: return [[pos]]

    if not pos in memo:    
        paths = []
        for di, dj in DIRS:
            ni, nj = i + di, j + dj
            if (ni >=0 and nj >=0 and ni < len(dict) and nj < len(dict[0]) and int(dict[ni][nj]) == int(dict[i][j] + 1)):
                paths += list(map(lambda l: [pos] + l, dp((ni, nj), dict, memo)))
        memo[pos] = paths

    return memo[pos]

part_1 = sum(map(lambda init: len(set(map(lambda l: tuple(l[-1]), dp(init, dict, memo)))), trailheads))
print(f'Part 1: {part_1}')
