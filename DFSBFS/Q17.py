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