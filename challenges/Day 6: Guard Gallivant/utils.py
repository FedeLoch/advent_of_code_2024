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

DIR = { 'UP': (1, 0),  'DOWN': (-1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1) }

def dict_from_file(input_path):
  row, guard_pos, array = 0, None, []
  with open(input_path) as f:
    for line in f:
      for col in range(len(line[:-1])):
        if line[col] == '^': guard_pos = (row, col)
      array.append([num for num in line[:-1]])
      row +=1

  return (guard_pos, DIR['UP']), array

