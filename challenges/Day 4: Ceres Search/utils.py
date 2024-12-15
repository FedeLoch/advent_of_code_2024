def dict_from_file(input_path):
  array = []
  with open(input_path) as f:
    for line in f: array.append([num for num in line[:-1]])
  return array

coords = [
    (1, 0),   #'UP'
    (-1, 0),  #'DOWN'
    (0, -1),  #'LEFT'
    (0, 1),   #'RIGHT' 
    (-1, -1), # UP LEFT
    (-1, 1),  # UP RIGHT
    (1, -1),  # DOWN LEFT
    (1, 1),   # DOWN RIGHT
]