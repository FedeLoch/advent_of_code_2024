input_path = 'challenges/Day 12: Garden Groups/input'

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

graph = []
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

print('Part 1:', sum(map(lambda c: len(c) * perimeter(c), components(graph))))