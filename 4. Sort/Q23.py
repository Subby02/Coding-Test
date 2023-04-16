import sys

n = int(sys.stdin.readline())

score = []
for _ in range(n):
  value = list(map(str,sys.stdin.readline().split()))
  score.append([int(value[1]),int(value[2]),int(value[3]),value[0]])

score.sort(reverse = False , key = lambda x : (-x[0] , x[1] , -x[2] , x[3]))

for k , e , m , name in score:
  print(name)

# 1. So Easy 근데 이걸 sort 정렬을 사용하지 않고 직접 작성가능할 진 잘 모르겠다..
