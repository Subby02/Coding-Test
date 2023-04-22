import sys

n = int(sys.stdin.readline())

soldier = list(map(int, sys.stdin.readline().split()))

d = [0] * (n + 1)

cnt = 0
for i in range(n - 1, -1, -1):
  for j in range(i, n):
    d[j] = soldier[i]
    if soldier[i] < soldier[j]:
      cnt += 1
