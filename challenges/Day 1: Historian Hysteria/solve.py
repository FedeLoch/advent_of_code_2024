input_path = 'challenges/Day 1: Historian Hysteria/input'

left, right, part_1, part_2  = [], [], 0, 0
with open(input_path) as f:
  for line in f:
    l, r = line[:-1].split('  '); left.append(int(l)); right.append(int(r))
left.sort(); right.sort()

for i in range(len(left)): part_1 += abs(left[i] - right[i])
for i in range(len(left)): part_2 += right.count(left[i]) * left[i]
print('Part 1: ', part_1)
print('Part 2: ', part_2)