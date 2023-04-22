import sys

t = int(sys.stdin.readline())

dy = [1, 0, -1]

for _ in range(t):
  n, m = map(int, sys.stdin.readline().split(' '))
  golds = list(map(int, sys.stdin.readline().split(' ')))

  d = []
  for i in range(n):
    d.append(golds[m * i:m * (i + 1)])

  for i in range(1, m):
    for j in range(n):
      array = []
      for k in range(3):
        if 0 <= j - dy[k] < n:
          array.append(d[j - dy[k]][i - 1])
      d[j][i] = max(array) + d[j][i]

  max_gold = 0
  for i in range(n):
    max_gold = max(d[i][m - 1], max_gold)

  print(max_gold)

# 1. DP가 하도 오랜만이어서 앞에 다른 예제를 보면서 공부 했는데 어떻게 접근해야될지 모르겠어서 다른 예제를 찾아보다가 하필 이 문제 설명을 살짝 읽어버려서.. 아이디어를 얻어서 코드를 작성하였다.
# 2. 전 위치에 매장된 금이 큰 걸 현재 위치에 매장된 금이랑 합하는 방식으로 dy라는 변수를 이용하여 왼쪽 위 , 왼쪽 , 왼쪽 아래 값을 비교하는데 범위를 넘어가면 array에 추가 하지 않아서 인덱스 에러를 방지 했다.
# 3. 생각 보다 좋은 문제인거 같진 않다.. 뭔가 인덱스가 더러운 느낌?

