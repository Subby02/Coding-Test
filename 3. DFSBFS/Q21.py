import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())

graph = []
visited = [[False] * n for _ in range(n)]
union = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def gap(x, y):
  if x > y:
    return x - y
  else:
    return y - x


def bfs(x, y):
  if visited[x][y]:
    return
  union.append([])
  q = deque()
  q.append((x, y))
  visited[x][y] = True
  union[-1].append((x, y))

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or ny < 0 or nx >= n or ny >= n:
        continue
      if visited[nx][ny]:
        continue
      if l <= gap(graph[x][y], graph[nx][ny]) <= r:
        union[-1].append((nx, ny))
        visited[nx][ny] = True
        q.append((nx, ny))

  if len(union[-1]) == 1:
    union.remove(union[-1])


def solution():
  global union, visited

  day = 0
  for x in range(n):
    for y in range(n):
      bfs(x, y)

  while union:
    for u in union:
      total = 0
      for x, y in u:
        total += graph[x][y]
      avg = total // len(u)
      for x, y in u:
        graph[x][y] = avg

    union = []
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
      for y in range(n):
        bfs(x, y)

    day += 1

  print(day)


solution()
# 1. 이 문제를 보자마자 DFS/BFS 실전 문제인 음류수 얼려 먹기를 이용하면 될 거 같다는 생각이 바로 # 들었다. 그래서 바로 bfs를 이용하여 코드를 작성하였다.
# 2. 코드를 작성하면서 연합한 국가 들을 어떻게 저장할지에 대해서 고민을 많이 했다. 맨처음에 책 풀이# 처럼 union 2차원 배열에 각 위치에 연합 숫자로 하는 방식으로 작성 할려고 했는데
# 나중에 인구를 평균화(?) 할 때 복잡해질거 같아서 union 배열에 각 연합에 위치를 따로
# 저장하는 방식을 선택해서 코드를 작성하여 나중에 평균화 할 때
# 배열을 불러내 다 더하기 쉽게 작성하였다.
# 3. 그런데 문제를 풀고 풀이를 보니 어차피 bfs가 한번 진행되면 연합이 하나 나오기 때문에
# 바로 평균화를 해도 된다는 점을 간과 하고 있었다. 내가 풀었던 방식은 모든 국가들에 대해서
# 연합을 구하고 마지막으로 각각 연합을 평균화 시켰다. 그래서 방법이 좀 복잡해졌던거 같다.
# 4. 그리고 맨처음에 제출 했을때 visited 배열을 사용하지 않고 그냥 union 배열에서
# 해당 좌표가 있는지 탐색하는 함수를 만들어서 사용했는데 그거 땜에 80%에서 계속 시간 초과가 났다.
# 여기서 좀 막혀서 질문 게시판을 봤는데 많은 사람들이 80%에서 막힌걸 보고 최적화 하던중
# visited 배열을 사용하면 탐색하는 함수에 있는 반복문을 않써도 된다는 점을 알게 되어서
# 변경하였더니 통과하였다.
