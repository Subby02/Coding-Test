# from itertools import combinations
# import sys

# n, m = map(int, sys.stdin.readline().split())

# graph = []
# for i in range(n):
#   graph.append(list(map(int, sys.stdin.readline().split())))

# num = [i for i in range(n * m)]
# combos = combinations(num, 3)

# virus = []
# for x in range(n):
#   for y in range(m):
#     if graph[x][y] == 2:
#       virus.append([x, y])


# def dfs(x, y):
#   if x <= -1 or x >= n or y <= -1 or y >= m:
#     return
#   if graph[x][y] == 0:
#     graph[x][y] = 2
#     dfs(x - 1, y)
#     dfs(x, y - 1)
#     dfs(x + 1, y)
#     dfs(x, y + 1)


# compare_graph = [item[:] for item in graph]

# min_safe = 0
# for combo in list(combos):

#   # 선정된 3개 위치에 벽을 설치
#   for wall in combo:
#     x = wall // m
#     y = wall % m

#     graph[x][y] = 1

#   # dfs로 바이러스 확산 시킴
#   for v in virus:
#     dfs(v[0] - 1, v[1])
#     dfs(v[0], v[1] - 1)
#     dfs(v[0] + 1, v[1])
#     dfs(v[0], v[1] + 1)

#   # 안전 지역 카운트
#   count = 0
#   for x in range(n):
#     for y in range(m):
#       if graph[x][y] == 0:
#         count += 1

#   # 감염 시켰던 곳 복구
#   graph = [item[:] for item in compare_graph]

#   min_safe = max(min_safe, count)

# print(min_safe)
# 1. n , m의 최대가 8이므로 벽을 설치 할 수 있는 곳은 최대 64곳이므로 64C3 = 41664의 경우의 수만 탐색하면 되므로 완전 탐색을 할 수 있다.
# 2. 위 접근방식으로 코드를 작성하였고 슬라이싱을 이용한 2차원 배열 깊은 복사를 하여 모든 경우의 수를 테스트 하고 다시 복구 하는 코드를 작성하였다. 
# 3. 위 코드를 제출 하였더니 37%에서 자꾸 틀렸다고 나왔다. 솔직히 모든 경우의 수를 탐색하는게 맞다고 100% 확신이 들었기 때문에 내가 빠뜨리고 있는게 있다고 생각해서 계속 노력 해봤지만 알아내지 못했고 답지에서 한글로 설명만 되어있는 부분을 읽었는데 벽이 설치 된 곳을 제외 하지 않고 넣어서 벽이 중첩되서 설치되어 더 많은 안전지역을 만들 수 있다는 점을 빠뜨리고 있다는 걸 알게 되었다. (답지에 있는 코드는 보지 않았다.)

from itertools import combinations
import sys

n, m = map(int, sys.stdin.readline().split())

graph = []
for i in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

# 0으로 되어있는 부분만으로 조합 구성
num = []
cnt = 0
for x in range(n):
  for y in range(m):
    if graph[x][y] == 0:
      num.append(cnt)
    cnt+=1
combos = combinations(num, 3)

# 바이러스 위치 저장
virus = []
for x in range(n):
  for y in range(m):
    if graph[x][y] == 2:
      virus.append([x, y])

# dfs
def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return
  if graph[x][y] == 0:
    graph[x][y] = 2
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)


compare_graph = [item[:] for item in graph]

min_safe = 0
for combo in list(combos):

  # 선정된 3개 위치에 벽을 설치
  for wall in combo:
    x = wall // m
    y = wall % m

    graph[x][y] = 1

  # dfs로 바이러스 확산 시킴
  for v in virus:
    dfs(v[0] - 1, v[1])
    dfs(v[0], v[1] - 1)
    dfs(v[0] + 1, v[1])
    dfs(v[0], v[1] + 1)

  # 안전 지역 카운트
  count = 0
  for x in range(n):
    for y in range(m):
      if graph[x][y] == 0:
        count += 1

  # 감염 시켰던 곳 복구
  graph = [item[:] for item in compare_graph]

  min_safe = max(min_safe, count)

print(min_safe)
