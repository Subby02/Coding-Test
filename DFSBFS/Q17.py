# import sys

# n, k = map(int, sys.stdin.readline().split())

# graph = []

# for _ in range(n):
#   graph.append(list(map(int, sys.stdin.readline().split())))

# s , x , y = map(int, sys.stdin.readline().split())

# viruses = [[] for _ in range(k)]
# for i in range(n):
#   for j in range(n):
#     if graph[i][j] != 0:
#       viruses[graph[i][j]-1].append((i, j))

# def dfs(virus, x, y):
#   if x <= -1 or x >= n or y <= -1 or y >= n:
#     return
#   if graph[x][y] == 0:
#     graph[x][y] = virus+1
#     viruses[virus].append((x,y))

# for _ in range(s):
#   # 모든 바이러스
#   for i in range(k):
#     # 해당 바이러스 위치 
#     for _ in range(len(viruses[i])):
#       nx , ny = viruses[i].pop(0)
#       dfs(i, nx - 1, ny)
#       dfs(i, nx, ny - 1)
#       dfs(i, nx + 1, ny)
#       dfs(i, nx, ny + 1)
      
# print(graph[x-1][y-1])

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

graph = []

for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

s , x , y = map(int, sys.stdin.readline().split())

virus = []
for i in range(n):
  for j in range(n):
    if graph[i][j] != 0:
      virus.append((graph[i][j] , i , j))

virus.sort()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
  next_queue = virus[:]
  for _ in range(s):
    queue = deque(next_queue)
    next_queue = []
    while queue:
      virus_type , x , y = queue.popleft()
  
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
          continue
        if graph[nx][ny] != 0:
          continue
        next_queue.append((virus_type,nx,ny))
        graph[nx][ny] = virus_type

bfs()
print(graph[x-1][y-1])

# 1. Q16 문제와 매우 유사해서 자연스럽게 dfs로 풀려고 했으나 결국엔 코드를 해석해보면 bfs로 풀고 있었다. 다행히 답을 맞췄다(?).
# 2. 좀 더 bfs 적으로 풀려고 큐를 이용하여 다시 풀었다. 초를 나누기 위해서 next_queue를 이용하여 queue가 None이면 다시 queue에 next_queue를 추가 하는 방식으로 코드를 작성하였다.