# from itertools import permutations
# import sys

# n = int(sys.stdin.readline())
# nums = list(map(int,sys.stdin.readline().split()))
# operaters = list(map(int,sys.stdin.readline().split()))

# opers = []
# for i in range(4):
#   for _ in range(operaters[i]):
#     opers.append(i)

# max_value = -1e9
# min_value = 1e9
# for oper in permutations(opers,len(opers)):
#   value = nums[0]
#   for i in range(n-1):
#     if oper[i] == 0:
#       value+=nums[i+1]
#     elif oper[i] == 1:
#       value-=nums[i+1]
#     elif oper[i] == 2:
#       value*=nums[i+1]
#     elif oper[i] == 3:
#       value = int(value/nums[i+1])
#   max_value = max(max_value , value)
#   min_value = min(min_value , value)

# print(max_value)
# print(min_value)
# 1. 브루트포스 방식으로 풀어봤다. 예제는 다 맞는데 시간초과가 났다. 이방법으로는 힘들거 같다고 생각이 들기도 했고 DFS/BFS 문제인데 이렇게 풀면 안될거 같아서 접근방식을 바꾸기로 하였다.
# 2. 나중에 문제를 풀고 다른 방식을 찾아보다가 이 방법도 PyPy 3로 하면 가능하다는 것을 알게 되었다. 살짝에 실수로 에러가 있었지만 조금만 수정하고 해보니 정상 작동하였다. 살짝 뿌듯 ㅎ

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

values = []


def dfs(value, i):
  global add, sub, mul, div

  if i == n:
    values.append(value)
    return

  if add > 0:
    add -= 1
    dfs(value + nums[i], i + 1)
    add += 1
  if sub > 0:
    sub -= 1
    dfs(value - nums[i], i + 1)
    sub += 1
  if mul > 0:
    mul -= 1
    dfs(value * nums[i], i + 1)
    mul += 1
  if div > 0:
    div -= 1
    dfs(int(value / nums[i]), i + 1)
    div += 1


dfs(nums[0], 1)

print(max(values))
print(min(values))

# 1. dfs로 접근하여 풀어봤다. 원래 global을 사용하지 않고 파라미터를 이용해서 계속 값을 변경 하도록 했는데 배열을 이용해서 그런지 깊은 복사를 하지 않아 원래 배열이 다 바뀌는거 같았다. 그래서 다른 방식을 생각해볼려고 했는데 도무지 생각이 안나서 책을 봤다.
# 2. 책을 보고 매우 놀랐다. 내가 짠 코드와 거의 유사하다는걸 알았다. 책에서 global을 이용하여 각각 값을 변경하는걸 보고 수정하였다. 다른 방식을 찾아보다가 파라미터로 넘기는 방식을 이용하는것도 있긴 했는데 그러면 너무 함수 파라미터가 길어져서 더러워 보였다. global도 딱히 깨끗해(?) 보이진 않는다.
