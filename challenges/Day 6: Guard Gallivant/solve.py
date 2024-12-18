input_path = 'challenges/Day 6: Guard Gallivant/input'

from utils import dict_from_file, is_valid, TURN, DIR
guard, _dict = dict_from_file(input_path)

forward = lambda guard: (guard[0][0] + DIR[guard[1]][0], guard[0][1] + DIR[guard[1]][1])

def next_pos(guard, graph):
    next = forward(guard)
    return (guard[0], TURN[guard[1]]) if graph[next[0]][next[1]] == '#' else (next, guard[1])

current, visited, marked = guard, {}, {}
while is_valid(forward(current), _dict) and (str(current) not in visited):
    visited[str(current)] = True
    marked[str(current[0])] = True
    current = next_pos(current, _dict)
    if not is_valid(current[0], _dict): break

print('Part 1:', len(marked) + 1)
