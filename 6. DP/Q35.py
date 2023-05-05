import sys

n = int(sys.stdin.readline())

dp = [True, True]

cnt = 1
num = 2
while cnt != n:
  dp.append(False)
  if num % 2 == 0 and dp[num // 2]:
    dp[num] = True
    cnt += 1
  elif num % 3 == 0 and dp[num // 3]:
    dp[num] = True
    cnt += 1
  elif num % 5 == 0 and dp[num // 5]:
    dp[num] = True
    cnt += 1
  num += 1

print(len(dp) - 1)

# 1. 문제를 보고 고민을 많이 했다. 어떻게 접근을 해야 할지.. 처음에는 단순하게 2, 3 ,5 를 각각 곱해서 중복을 제거 하고 정렬 하는 방식으로 할려고 했는데 순서에 안맞게 나중에 중간(?)에 삽입 되는 값들이 있어서 카운트를 제대로 할 수 없다고 생각했다.
# 2. 그래서 다른 방식으로 접근 해야될거 같아서 고민을 하던중 어차피 못생긴 수에 못생긴 수를 곱해도 못생긴 수 이므로 못생긴 수를 못생긴 수로 나눈어도 나누어 떨어지면 못생긴 수가 맞다는 방식을 이용해서 num을 증가하여 못생긴 수인지 파악하여 카운트하여 해당 카운트에 도달하면 n번째 못생긴 수를 출력 하는 방식으로 작성하였다.
# 3. 답지를 봤을때 솔직히 말해서 직관적으로 이해하기 쉽고 좀 더 dp 같이 푸는 방식은 솔직히 내 방식인거 같다. 하지만 내가 푼 방식은 점점 값들이 커져가면 격차가 커져가서 계산이 많이 필요하다. 하지만 문제에서 n의 최대가 1000이므로 충분히 이 방식으로 풀 수 있을거 같지만 만약 범위가 더 커지면 답지 방식이 맞는거 같다.

import sys

n = int(sys.stdin.readline())

ugly = [0] * n
ugly[0] = 1 

i2 = i3 = i5 = 0
next2, next3, next5 = 2, 3, 5

for l in range(1, n):
  ugly[l] = min(next2, next3, next5)
  if ugly[l] == next2:
      i2 += 1
      next2 = ugly[i2] * 2
  if ugly[l] == next3:
      i3 += 1
      next3 = ugly[i3] * 3
  if ugly[l] == next5:
      i5 += 1
      next5 = ugly[i5] * 5

print(ugly[n - 1])

#1. 답지에 나온 풀이로 최대한 코드를 작성하며 이해할려하고 반복문에 각각 값을 출력하여 분석하였으나 아직 잘 이해가 안되는거 같다. 그래도 얼추 무슨 느낌인지는 알거 같다.
