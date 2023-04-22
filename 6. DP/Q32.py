import sys

n = int(sys.stdin.readline())

num = []
d = []
for _ in range(n):
  num.append(list(map(int, sys.stdin.readline().split())))
  d.append([0] * len(num[-1]))

d[0] = num[0]

for i in range(n - 1):
  for j in range(len(d[i])):
    d[i + 1][j] = max(d[i][j] + num[i + 1][j], d[i + 1][j])
    d[i + 1][j + 1] = max(d[i][j] + num[i + 1][j + 1], d[i + 1][j + 1])

print(max(d[-1]))

# 1. 문제를 보자마자 31번 문제와 유사하다는 점을 찾았고 그냥 바로 코드를 작성하였다. 답지는 이 방식하고 살짝 다르게 해당 위치에서 역으로 위로 올라가서 찾는 방식이지만 난 그냥 해당 위치에서 갈 수 있는 경우의 수를 저장해주는 방식으로 작성하였다. 답지 방식이 아주 살짝 빠르긴 하지만 큰 의미는 없다고 생각한다.
