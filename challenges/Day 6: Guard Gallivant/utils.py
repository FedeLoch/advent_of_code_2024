TURN = { 'UP': 'RIGHT', 'RIGHT': 'DOWN', 'DOWN': 'LEFT', 'LEFT': 'UP' } # type: ignore
DIR = { 'UP': (-1, 0),  'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1) }

def dict_from_file(input_path):
  row, guard_pos, array = 0, None, []
  with open(input_path) as f:
    for line in f:
      for col in range(len(line[:-1])):
        if line[col] == '^': guard_pos = (row, col)
      array.append([num for num in line[:-1]])
      row +=1

  return (guard_pos, 'UP'), array

is_valid = lambda pos, _dict: False if pos[0] < 0 or  pos[0]  >= len(_dict) or  pos[1]  < 0 or  pos[1]  >= len(_dict[0]) else True