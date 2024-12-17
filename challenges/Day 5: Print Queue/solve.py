input_path = 'challenges/Day 5: Print Queue/input'

mapping, order, part_1 = True, {}, 0
memo = {}

must_to = lambda left, right: str(left) + '|' + str(right) in order

def dp(l):
    key = str(l)
    if len(l) <= 1: return True

    if key not in memo:
        middle = len(l) // 2
        left, pivot, right = l[:middle], l[middle], l[middle + 1:]
        memo[key] = must_to(left[-1], pivot) and must_to(pivot, right[0]) and dp(left) and dp(right)

    return memo[key] 

with open(input_path) as f:
    for line in f:
        if line == '\n': mapping = False; continue

        if mapping:
            left, right = map(int, line[:-1].split('|'))
            order[line[:-1]] = True
            memo[str([left, right])] = True
            continue

        l = list(map(int, line[:-1].split(',')))
        part_1 += l[len(l) // 2] if dp(l) else 0

print('Part 1: ', part_1)
