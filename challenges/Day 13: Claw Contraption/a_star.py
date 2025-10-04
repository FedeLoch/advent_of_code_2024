from queue import PriorityQueue

def a_star(graph, initialNode, h):
  pqueue = PriorityQueue()
  _min = float('inf')
  visited = set()
  pqueue.put( ( h(initialNode), initialNode, 1 ) ) # priority, node, time
  while not pqueue.empty():
    priority, node, time = pqueue.get_nowait()
    if h(node) == 0: # if the distance is 0
      cost = node[1][0] * 3 + node[1][1]
      if (cost < _min): return node
        # _min = cost; final_node = node; continue # Updates the minimum
    for target_node in graph[(node, time)]:
      if (target_node, time) not in visited:
        visited.add((target_node, time))

        pqueue.put((
          priority + h(target_node),
          target_node,
          time + 1
        ))

  return initialNode

class Prize:
  def __init__(self, a, b, goal):
    self.a = a
    self.b = b
    self.goal = goal

  def h(self):
    return lambda node: abs(self.goal[0] - node[0][0]) + abs(self.goal[1] - node[0][1])

  def __getitem__(self, state):
    node, _ = state
    res = []
    new_a = ((node[0][0] + self.a[0], node[0][1] + self.a[1]), (node[1][0] + 1, node[1][1]))
    new_b = ((node[0][0] + self.b[0], node[0][1] + self.b[1]), (node[1][0], node[1][1] + 1))
    if (node[0][0] > self.goal[0]): return []
    if (node[0][1] > self.goal[1]): return []
    if (self.h()(new_a) >= 0): res.append(new_a)
    if (self.h()(new_b) >= 0): res.append(new_b)

    return res