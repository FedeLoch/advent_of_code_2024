input_path = 'challenges/Day 11: Plutonian Pebbles/input'

line = list(map(int, open(input_path).readline().rstrip().split(' '))); memo = {}

def blink(_line, n):
   if n <= 0: return len(_line)

   return sum(map(lambda i: blink_elem(i, n), _line))

def blink_once(elem):
    if elem == 0: return [1]
    s = str(elem)
    if len(s) % 2 == 0: return [int(s[:len(s)//2]), int(s[len(s)//2:])]
    return [elem * 2024]

def blink_elem(elem, depth):
    if depth <= 0: return 1

    if not elem in memo: memo[elem] = {}

    if not depth in memo[elem]:
        memo[elem][depth] = blink(blink_once(elem), depth - 1)

    return memo[elem][depth]

print('Part 1: ', blink(line, 25))
print('Part 2: ', blink(line, 75))
