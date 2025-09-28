input_path = 'challenges/Day 12: Garden Groups/input2'

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

removes = {
    (0, -1): set([(0, -1), (-1, 0), (1, 0)]), (-1, 0): set([(0, -1), (-1, 0), (0, 1)]),
    (0, 1): set([(-1, 0), (0, 1), (1, 0)]), (1, 0): set([(0, -1), (1, 0), (0, 1)])
}

def external_sides(component):
    total, seen = 0, set()
    for i, j in component:
        external = set(DIRS)
        for di, dj in DIRS:
            neighbor = (i + di, j + dj)
            if neighbor in component:
                if neighbor in seen: external -= removes[(di, dj)]
                else: external -= set([(di, dj)])
        total += len(external)
        seen.add((i, j))
    return total

def includes(c1, c2): # TODO
    min_i1, max_i1 = min(c1, key=lambda x: x[0])[0], max(c1, key=lambda x: x[0])[0]
    min_j1, max_j1 = min(c1, key=lambda x: x[1])[1], max(c1, key=lambda x: x[1])[1]
    min_i2, max_i2 = min(c2, key=lambda x: x[0])[0], max(c2, key=lambda x: x[0])[0]
    min_j2, max_j2 = min(c2, key=lambda x: x[1])[1], max(c2, key=lambda x: x[1])[1]
    return min_i1 <= min_i2 and max_i1 >= max_i2 and min_j1 <= min_j2 and max_j1 >= max_j2

def compute_external_sides(components):
    external_sides_ = {}
    for c in components: external_sides_[c[0]] = external_sides(c)
    return external_sides_

all_components = components(graph)
all_external_sides = compute_external_sides(all_components)

def internal_size_of(c1):
    res = 0
    for c2 in all_components:
        if c1 != c2 and includes(c1, c2): res += all_external_sides[c2[0]]
    return res

cost1 = lambda c: len(c) * perimeter(c)
def cost2(component):
    print('Component:', graph[component[0][0]][component[0][1]], 'Size:', len(component), 'External sides:', all_external_sides[component[0]], 'Internal sides:', internal_size_of(component))
    return (all_external_sides[component[0]] + internal_size_of(component)) * len(component)
# cost2 = lambda component: (all_external_sides[component[0]] + internal_size_of(component)) * len(component)

print('Part 1:', sum(map(cost1, all_components)))
print('Part 2:', sum(map(cost2, all_components)))