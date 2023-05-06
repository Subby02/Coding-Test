import sys
import heapq

n , m = map(int , sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
  a , b = map(int , sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

distance = [(1e9)] * (n+1)

q = []
heapq.heappush(q, (0 , 1))
distance[1] = 0
while q:
  dist , now = heapq.heappop(q)

  if distance[now] < dist:
    continue

  for i in graph[now]:
    cost = dist+1
    if cost < distance[i]:
      distance[i] = cost
      heapq.heappush(q, (cost , i))

max_dist = max(distance[1:])
num = distance.index(max_dist)
cnt = distance.count(max_dist)

print(num , max_dist , cnt)

# 1. 술래는 항상 1번 헛간에서 출발 하므로 한 노드에서 모든 노드를 가는 다익스트라를 이용하기로 하였고 모든 통로의 비용은 1이고 통로는 양방향인것만 주의 하면 어렵지 않은 문제였다. 출력은 먼저 숨어야할 헛간 거리를 최대 인것으로 골라주고 그 값을 가지는 첫번째 헛간을 저장하고 동일한 거리에 있는 헛간을 카운트 해주면 된다.
# 2. Easy 최단 경로 문제는 확실히 조건만 살짝 수정해주면 되는거 같다.