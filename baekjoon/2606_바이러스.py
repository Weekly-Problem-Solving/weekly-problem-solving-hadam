from collections import deque

com_count = int(input())
line_count = int(input())
v = [False for i in range(com_count+1)]
g = [[] for i in range(com_count+1)]

for i in range(line_count):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)

def bfs(start, graph, visited):
  queue = deque([start])
  visited[start] = True
  n = 0

  while queue:
    curr_x = queue.pop()
    for linked_x in graph[curr_x]:
      if visited[linked_x] == False:
        n += 1
        queue.append(linked_x)
        visited[linked_x] = True

  return n

print(bfs(1, g, v))