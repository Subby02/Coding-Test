import sys
import heapq

t = int(sys.stdin.readline())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(t):
  n = int(sys.stdin.readline())

  distance = [[(1e9)] * n for _ in range(n)]
  
  graph = []
  for _ in range(n):
    graph.append(list(map(int ,sys.stdin.readline().split())))

  q = []
  heapq.heappush(q,(graph[0][0] , 0 , 0))
  distance[0][0] = graph[0][0]
  while q:
    dist , x , y = heapq.heappop(q)

    if distance[x][y] < dist:
      continue

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx >= 0 and nx < n and ny >= 0 and ny < n:
        cost = dist+graph[nx][ny]
        if cost < distance[nx][ny]:
          distance[nx][ny] = cost
          heapq.heappush(q,(cost , nx, ny))

  print(distance[-1][-1])

# 1. 문제를 보고 먼저 (0,0) 에서 시작 인걸 보고 한 노드에서 모든 노드를 가는 다익스트라 문제라는걸 알게 되었다. 상하좌우로 노드가 이어져있음을 인지 하고 dx , dy를 이용하여 전 노드와 상하좌우 노드의 비용을 더하여 원래 값 하고 비교 하여 최소 값을 저장 해준다.
# 2. 답지의 코드와 내 코드가 매우 유사하다.. 그리고 문제를 보자마자 막힘 없이 코드를 작성했다. 거의 10분 이내로 문제를 푼거 같다. 최단 경로 문제는 뭔가 원래 알고리즘에서 큰 변화가 없고 살짝 조건을 건들여주면 되는거 같다.