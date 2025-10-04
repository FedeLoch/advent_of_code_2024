from functools import reduce
input_path = 'challenges/Day 13: Claw Contraption/input'
from a_star import a_star, Prize

# 3 tokens to push A
# 1 token to push B
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

cost = lambda state: state[1][0] * 3 + state[1][1]
p = reduce(lambda total, prize: total + cost(a_star(prize, initial_state, prize.h())), prizes, 0)

print('Part 1:', p)

# Button A: X+94, Y+34 -> (94, 34)
# Button B: X+22, Y+67 -> (22, 67)
# Prize: X=8400, Y=5400 -> (8400, 5400)

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279