from functools import reduce
input_path = 'challenges/Day 13: Claw Contraption/input'
from a_star import a_star, Prize

prizes = []
with open(input_path) as f:
    a, b, goal = None, None, None
    for line in f:
        if line == '\n':
            prizes.append(Prize(a, b, goal))
            a, b, goal = None, None, None; continue
        if line.startswith('Button A:'):
            a = tuple(map(int, line.strip().split('X+')[1].split(', Y+')))
        elif line.startswith('Button B:'):
            b = tuple(map(int, line.strip().split('X+')[1].split(', Y+')))
        elif line.startswith('Prize:'):
            goal = tuple(map(int, line.strip().split('X=')[1].split(', Y=')))
    prizes.append(Prize(a, b, goal))

initial_state = ((0, 0), (0, 0))

cost = lambda node: node[1][0] * 3 + node[1][1]
part1 = reduce(lambda total, prize: total + cost(a_star(prize, initial_state, prize.h())), prizes, 0)

print('Part 1:', part1)