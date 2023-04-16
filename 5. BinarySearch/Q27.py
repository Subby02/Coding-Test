import sys

n, x = map(int, sys.stdin.readline().split())

array = list(map(int, sys.stdin.readline().split()))

def left_binary_search(array, target, start, end):
  if start > end:
    return
  mid = (start + end) // 2
  if array[mid] == target and (array[mid - 1] != target or mid == 0):
    return mid
  elif array[mid] >= target:
    return left_binary_search(array, target, start, mid - 1)
  else:
    return left_binary_search(array, target, mid + 1, end)


def right_binary_search(array, target, start, end):
  if start > end:
    return
  mid = (start + end) // 2
  if array[mid] == target and (array[mid + 1] != target
                               or mid == len(array) - 1):
    return mid
  elif array[mid] > target:
    return right_binary_search(array, target, start, mid - 1)
  else:
    return right_binary_search(array, target, mid + 1, end)


left = left_binary_search(array, x, 0, len(array) - 1)
right = right_binary_search(array, x, 0, len(array) - 1)

if left == None:
  print(-1)
else:
  print(right - left + 1)

# 1. 이진 탐색으로 어떻게 접근 해야되는지 생각을 해봤는데 30분 동안 진짜 답이 안나왔다. 그래서 어쩔수 없이 답을 보고 이해하게 되었다. 답을 보고 나니 그렇게 어려웠던 건 아니었는데 첫 이진 탐색 문제이기도 하고 이날 상태가 안좋아서 생각이 잘 안됐던 거 같다.
