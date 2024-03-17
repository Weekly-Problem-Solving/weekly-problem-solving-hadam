from collections import deque

n = int(input())
g = []
for _ in range(n):
  row = list(map(int, list(input())))
  g.append(row)

def bfs(start, graph):
  house_count = 0
  q = deque([start])
  graph[start[0]][start[1]] = 0

  while q:
    curr_x, curr_y = q.popleft()
    house_count += 1
    for i in range(4):
      next_x, next_y = curr_x + move_x[i], curr_y + move_y[i]
      if 0 <= next_x < n and 0 <= next_y < n:
        if g[next_x][next_y] == 1:
          q.append((next_x, next_y))
          graph[next_x][next_y] = 0
  return house_count

move_x = [0,0,1,-1]
move_y= [1,-1,0,0]
danji_count = 0
home_count_list = []

for i in range(n):
  for j in range(n):
    if g[i][j] == 1:
      home_count = bfs((i,j), g)
      home_count_list.append(home_count)
      danji_count += 1

print(danji_count)

home_count_list.sort()

for count in home_count_list:
  print(count)