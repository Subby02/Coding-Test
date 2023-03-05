from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())

INF = 1e9
visited = [INF for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)


def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = 0
  while queue:
    v = queue.popleft()

    for i in graph[v]:
      if visited[i] == INF:
        queue.append(i)
        visited[i] = visited[v] + 1
      else:
        visited[i] = min(visited[i], visited[v] + 1)


bfs(graph, x, visited)

isNone = True
for i in range(len(visited)):
  if visited[i] == k:
    isNone = False
    print(i)

if isNone:
  print(-1)
