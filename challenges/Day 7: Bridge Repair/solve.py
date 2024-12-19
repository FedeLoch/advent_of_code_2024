input_path = 'challenges/Day 7: Bridge Repair/input'

sum_op = lambda x, y: x + y; mul_op = lambda x, y: x * y; or_op = lambda x, y: int(str(x) + str(y))

base_operations = [ sum_op, mul_op ]
complex_operations = [ sum_op, mul_op, or_op ]

def is_valid(value, current, numbers, operations, memo):
    if len(numbers) == 0: return current == value
    key = str((value, current, numbers))

    if key not in memo:
        new_value = False
        for op in operations:
            new_current = op(current, numbers[0])
            new_value = new_value or is_valid(value, new_current, numbers[1:], operations, memo)
            if new_value: break
        memo[key] = new_value

    return memo[key]

part_1, part_2 = 0, 0
with open(input_path) as f:
    for line in f:
        test_value, numbers = line[:-1].split(':')
        numbers = list(map(int, numbers.strip().split(' ')))
        test_value = int(test_value)
        part_1 += test_value if is_valid(test_value, numbers[0], numbers[1:], base_operations, {}) else 0
        part_2 += test_value if is_valid(test_value, numbers[0], numbers[1:], complex_operations, {}) else 0

print('Part 1: ', part_1); print('Part 2: ', part_2)