# import sys

# n, c = map(int, sys.stdin.readline().split())

# array = []

# for _ in range(n):
#   array.append(int(sys.stdin.readline()))

# def binary_search(array, target, start, end):
#   if start > end:
#     return -1
#   mid = (start + end) // 2
#   if array[mid] >= target:
#     return mid
#   else:
#     return binary_search(array, target, mid + 1, end)

# def solution(n , c , array):
#   array.sort()
  
#   max_distance = (array[-1]-array[0])//(c-1)
  
#   for distance in range(max_distance , 0 , - 1):
#     cnt = 1
#     num = array[0]
#     while True:
#       i = binary_search(array, num+distance, 0, n-1)
#       if i != -1:
#         num = array[i]
#         cnt+=1
#       else:
#         break
#     if cnt == c:
#       return distance


# print(solution(n , c , array))

# 1. 솔직히 문제 보고 어떻게 이진탐색으로 풀 수 있는지 감이 안왔다. 그래서 걍 최소,최대값으로 최대 거리를 구해서 c-1로 나누어서 인접한 공유기의 사이의 최대 거리를 지정해주고 낮춰가면서 가능 여부를 판단할때 이진탐색을 이용하는 방법으로 작성하였는데 틀렸다. 역시 이 논리는 아닌거 같아서 답을 보게 되었다.

import sys

n, c = map(int, sys.stdin.readline().split())

array = []

for _ in range(n):
  array.append(int(sys.stdin.readline()))

def solution(n , c , array):
  array.sort()

  min_gap = 1
  max_gap = array[-1] - array[0]
  result = 0
  
  while min_gap <= max_gap:
    mid_gap = (min_gap + max_gap) // 2
    value = array[0]
    cnt = 1
    for a in array:
      if a >= value+mid_gap:
        cnt+=1
        value = a
    if cnt < c:
      max_gap = mid_gap-1
    elif cnt >= c:
      min_gap = mid_gap+1
      result = mid_gap

  return result


print(solution(n , c , array))

# 1. 이진탐색 문제여서 무조건 '탐색'에만 너무 집중 하고 변형 하지 않고 풀려하는거 같다. 내가 작성한 코드 부분에서 최소 거리를 이용하여 공유기의 개수를 세는 부분 코드는 답지랑 아주 유사하다고 생각이 든다. 너무 탐색에 갇혀있지 말고 이진에 집중을 해야될거 같다.
