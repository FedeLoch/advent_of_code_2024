input_path = 'challenges/Day 6: Guard Gallivant/input'

from utils import dict_from_file, is_valid, TURN, DIR
guard, _dict = dict_from_file(input_path)

forward = lambda guard: (guard[0][0] + DIR[guard[1]][0], guard[0][1] + DIR[guard[1]][1])

def next_pos(guard, graph):
    next = forward(guard)
    return (guard[0], TURN[guard[1]]) if is_valid(next, graph) and graph[next[0]][next[1]] == '#' else (next, guard[1])

current, visited, marked = guard, {}, {}
while is_valid(current[0], _dict) and (str(current) not in visited):
    visited[str(current)] = True
    marked[str(current[0])] = True
    current = next_pos(current, _dict)
    if not is_valid(current[0], _dict): break

print('Part 1:', len(marked))

def has_a_loop():
    current, local_visited = guard, {}
    while is_valid(current[0], _dict):
        local_visited[str(current)] = True
        current = next_pos(current, _dict)
        if str(current) in local_visited: return True
    return False

def produce_a_loop(i):
    r, c = list(map(int, i[1:-1].split(',')))
    _dict[r][c] = '#'; value = has_a_loop(); _dict[r][c] = '.'
    return value

print('Part 2: ', len(list(filter(produce_a_loop, marked))))