from itertools import combinations
import sys

n = int(sys.stdin.readline())

graph = []
for _ in range(n):
  graph.append(list(sys.stdin.readline().split()))

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, 1, -1]


def dfs(x, y, d):
  if d == 0:
    for i in range(1, 5):
      dfs(x + dx[i], y + dy[i], i)
  else:
    if x < 0 or y < 0 or x >= n or y >= n:
      return
    if graph[x][y] == 'O':
      return
    if graph[x][y] == 'S':
      if (x, y) not in students:
        students.append((x, y))
    dfs(x + dx[d], y + dy[d], d)


teachers = []
all_pos = []
for x in range(n):
  for y in range(n):
    if graph[x][y] == 'T':
      teachers.append((x, y))
    elif graph[x][y] == 'X':
      all_pos.append((x, y))

is_possible = False
for combi in combinations(all_pos, 3):
  for x, y in combi:
    graph[x][y] = 'O'

  students = []
  for x, y in teachers:
    dfs(x, y, 0)

  if not students:
    is_possible = True
    break

  for x, y in combi:
    graph[x][y] = 'X'

if is_possible:
  print('YES')
else:
  print('NO')

# 그냥 문제 보고 N의 최대가 6 이므로 36C3은 충분히 브루트포스 할 수 있다 생각해서 조합을 사용했다.
# DFS/BFS 문제이니까 당연히 선생님 상하좌우를 확인 할때 DFS를 쓸 줄 알고 작성하였는데 문제를 풀고 # 풀이를 보니 조합을 사용할때 DFS/BFS를 이용하는거였다.. 여튼 코드는 정상 작동하고
# 괜찮게 접근 했다고 생각한다. 1트 만에 성공~!
