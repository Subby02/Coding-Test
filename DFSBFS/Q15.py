from collections import deque

n, m, k, x = map(int, input().split())

INF = 1e9
visited = [INF for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
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
      # else:
      #   visited[i] = min(visited[i], visited[v] + 1) <--- 필요없는 부분


bfs(graph, x, visited)

isNone = True
for i in range(len(visited)):
  if visited[i] == k:
    isNone = False
    print(i)

if isNone:
  print(-1)

# 백준 input 딜레이로 계속 시간 초과 떠서 내 로직이 틀린줄 알았는데 sys로 변경 하니까 성공 근데 다른 노드에서 이미 방문을 해서 visited 값이 있을때 앞에 노드에 +1 한 값이랑 원래 값을 비교 하는 코드를 넣었는데 생각해보니 bfs 임으로 무조건 원래 값이 작다는걸 생각하지 못하고 있었음 어차피 무조건 걸러지는 부분이어서 답에는 큰 영향이 없음