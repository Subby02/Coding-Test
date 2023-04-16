import sys
n = int(sys.stdin.readline())

array = list(map(int,sys.stdin.readline().split()))

def binary_search(array , start , end):
  if start > end:
    return -1
  mid = (start+end)//2
  
  if mid == array[mid]:
    return mid
  elif array[mid] >= mid:
    return binary_search(array , start , mid-1)
  else:
    return binary_search(array , mid+1 , end)

print(binary_search(array, 0 , len(array) - 1))

# So easy 보자마다 바로 풀 수 있었다. 설명할 것도 없이 그냥 이진탐색에서 조건만 수정하면 바로 풀 수 있다고 생각한다.