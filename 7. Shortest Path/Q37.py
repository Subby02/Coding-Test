import sys

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

graph = [[1e9] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
  graph[i][i] = 0

for _ in range(m):
  a , b , c = map(int , sys.stdin.readline().split())
  if graph[a][b]:
    graph[a][b] = min(c,graph[a][b])


for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b] = min(graph[a][b] , graph[a][k]+graph[k][b])

for i in range(1,n+1):
  for j in range(1,n+1):
    if graph[i][j] == 1e9:
      print(0 , end=' ')
    else:
      print(graph[i][j] , end=' ')
  print()

# 1. 플로이드 알고리즘하고 거의 동일 하지만 같은 노선이지만 비용이 다른 버스가 존재 할 수 있다는 점이 다르다. 그래서 그래프에 값을 저장할때 만약 동일 노선이 있으면 비용이 적은 값을 저장 해줘야지 비용의 최소값을 구할 수 있다.