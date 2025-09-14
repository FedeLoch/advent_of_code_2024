input_path = 'challenges/Day 10: Hoof It/bla'
input_path2 = 'challenges/Day 10: Hoof It/bla0'

# fill in the missing hiking trails
# componente conexa ? ( dfs | bfs ? )

# only up, down, left, or right
# todo los caminos, 
# para cada initial ( height 0 ), todos los caminos hacia 9s
# Una vez alcanzado un 9, no cuenta de nuevo.

# Ideas:
 # O uso bellman ford para saber si hay un camino desde cada 0 a cada 9 ( que siempre puede haber más de uno )
 # O uso bfs/dfs para hacer componente conexa y guardarme los 9s visitados ( esa cantidad será el score )

set1 = set()
set0 = set()
with open(input_path) as f:
    for line in f:
        set1.add(line[:-1])

print('\n')
for error in set1:
    print(error, '\n')

# with open(input_path2) as f:
#     for line in f:
#         set0.add(line[:-1])

# print('\n')
# for error in (set1.difference(set0)):
#     print(error, '\n')