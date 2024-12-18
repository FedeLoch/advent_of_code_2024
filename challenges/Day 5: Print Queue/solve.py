input_path = 'challenges/Day 5: Print Queue/input'

memo, order, part_1, part_2, mapping = {}, {}, 0, 0, True
must_to = lambda left, right: str(left) + '|' + str(right) in order

def dp(l):
    key = str(l)
    if len(l) <= 1: return True

    if key not in memo:
        middle = len(l) // 2
        left, pivot, right = l[:middle], l[middle], l[middle + 1:]
        memo[key] = must_to(left[-1], pivot) and must_to(pivot, right[0]) and dp(left) and dp(right)

    return memo[key] 

def ordered(l):
    if dp(l): return l

    middle = len(l) // 2
    left, pivot, right = ordered(l[:middle]), l[middle], ordered(l[middle + 1:])
    return left + [pivot] + right if dp(left + [pivot] + right) else ordered(
            left[:-1] + [pivot] + [left[-1]] + right if must_to(pivot, left[-1]) else
            left + right + [pivot]
    )

with open(input_path) as f:
    for line in f:
        if line == '\n': mapping = False; continue

        if mapping:
            left, right = map(int, line[:-1].split('|'))
            order[line[:-1]] = True
            memo[str([left, right])] = True
            continue

        l = list(map(int, line[:-1].split(',')))
        if (dp(l)): part_1 += l[len(l) // 2]
        else: part_2 += ordered(l)[len(l) // 2]

print('Part 1: ', part_1); print('Part 2: ', part_2)