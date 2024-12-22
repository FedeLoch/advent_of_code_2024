input_path = 'challenges/Day 8: Resonant Collinearity/input'
from utils import nodes_from_file, is_valid
graph, nodes, indexed_nodes = nodes_from_file(input_path)

def neighbors(node, graph):
    res, freq = [], graph[node[0]][node[1]]
    for neighbor in indexed_nodes[freq]:
        if node == neighbor: continue
        if graph[neighbor[0]][neighbor[1]] == graph[node[0]][node[1]]: res.append(neighbor)
    return res

def nexts_antinodes(antinode, diff, graph):
    if antinode == None: return []
    antinodes, current = [], antinode

    while (is_valid(current, graph)):
        antinodes.append(current)
        current = (current[0] + diff[0], current[1] + diff[1])
    return antinodes

def next_until_antinode(origin, diff, graph):
    current = origin
    while (is_valid(current, graph)):
        next = (current[0] + diff[0], current[1] + diff[1])
        if not is_valid((next[0], next[1]), graph): return None
        if graph[next[0]][next[1]] == graph[current[0]][current[1]]: current = next; continue
        return next
    return None

def antinodes(graph, nodes, resonance = False):
    antinodes = []
    for node in nodes:
        for neighbor in neighbors(node, graph):
            diff = (neighbor[0] - node[0], neighbor[1] - node[1])
            antinode = next_until_antinode(neighbor, diff, graph)
            next_antinodes = (nexts_antinodes(antinode, diff, graph) + [neighbor] if resonance else [ antinode ])
            antinodes += list(filter(lambda x: x != None, next_antinodes))
        
    return list(set(antinodes))

print('Part 1: ', len(antinodes(graph, nodes)))
print('Part 2: ', len(antinodes(graph, nodes, True)))
