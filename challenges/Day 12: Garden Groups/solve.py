from collections import defaultdict
from functools import reduce
input_path = 'challenges/Day 12: Garden Groups/input'

DIRS, graph = [(0, 1), (1, 0), (0, -1), (-1, 0)], []

with open(input_path) as f:
    for line in f: graph.append(line[:-1])

def components(graph):
    visited, components = set(), []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if (i, j) not in visited: components.append(bfs(graph, i, j, visited))
    return components

def bfs(graph, i, j, visited):
    queue = [(i, j)]
    component = []
    while queue:
        i, j = queue.pop(0)
        if (i, j) in visited: continue
        visited.add((i, j))
        component.append((i, j))
        for ni, nj in neighbors(graph, i, j):
            if (ni, nj) not in visited and graph[ni][nj] == graph[i][j]: queue.append((ni, nj))
    return component

neighbors = lambda graph, i, j: [(i + di, j + dj) for di, dj in DIRS if 0 <= i + di < len(graph) and 0 <= j + dj < len(graph[0])]
perimeter = lambda c: sum(1 for i, j in c for di, dj in DIRS if (i + di, j + dj) not in c)

def exposed_oriented_edges(component):
    S, edges = set(component), set()
    for x, y in S:
        if (x, y+1) not in S: edges.add(((x, y+1), (x+1, y+1)))
        if (x+1, y) not in S: edges.add(((x+1, y+1), (x+1, y)))
        if (x, y-1) not in S: edges.add(((x+1, y), (x, y)))
        if (x-1, y) not in S: edges.add(((x, y), (x, y+1)))
    return edges

build_directed_adj = lambda edges: reduce(lambda dict, elem: dict[elem[0]].append(elem[1]) or dict, edges, defaultdict(list))

def extract_cycles_oriented(edges):
    unused, adj, cycles = set(edges), build_directed_adj(edges), []
    while unused:
        u, v = next(iter(unused))
        cycle = [u, v]
        unused.discard((u, v))
        while True:
            curr = cycle[-1]
            next_edge = None
            for w in adj[curr]:
                if (curr, w) in unused: next_edge = (curr, w); break
            if next_edge is None: break
            unused.discard(next_edge)
            cycle.append(next_edge[1])
            if cycle[-1] == cycle[0]: cycle = cycle[:-1]; break
        cycles.append(cycle)
    return cycles

def compress_collinear(cycle):
    n, kept = len(cycle), []
    for i in range(n):
        prev = cycle[i-1]
        curr = cycle[i]
        nex = cycle[(i+1) % n]
        vx1, vy1 = curr[0]-prev[0], curr[1]-prev[1]
        vx2, vy2 = nex[0]-curr[0], nex[1]-curr[1]
        if vx1*vy2 == vy1*vx2: continue
        kept.append(curr)
    return kept

def polygon_vertex_count(component):
    edges = exposed_oriented_edges(component)
    if not edges: return 0
    return sum(len(compress_collinear(cyc)) for cyc in extract_cycles_oriented(edges))

cost2 = lambda component: polygon_vertex_count(component) * len(component)
all_components = components(graph)
cost1 = lambda c: len(c) * perimeter(c)

print('Part 1:', sum(map(cost1, all_components)))
print('Part 2:', sum(map(cost2, all_components)))