def nodes_from_file(input_path):
  row, array, nodes, indexed_nodes = 0, [], [], {}
  with open(input_path) as f:
    for line in f:
      array.append([num for num in line[:-1]])
      for col in range(len(line[:-1])):
        if line[col] != '.':
          if line[col] not in indexed_nodes: indexed_nodes[line[col]] = []
          indexed_nodes[line[col]].append((row, col))
          nodes.append((row, col))
      row +=1
    
  return array, nodes, indexed_nodes

is_valid = lambda pos, _dict: False if pos[0] < 0 or  pos[0]  >= len(_dict) or  pos[1]  < 0 or  pos[1]  >= len(_dict[0]) else True