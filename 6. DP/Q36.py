import sys

a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

values = []

def edit_dist(i , a , b , cnt):
  if a == b:
    values.append(cnt)

  if len(a) <= i or len(b) <= i:
    return
    
  if a[i] == b[i]:
    edit_dist(i+1,a,b, cnt)
  
  #삽입
  b.insert(i,a[i])
  edit_dist(i+1 , a , b[:] ,cnt+1)
  b.pop(i)
  #삭제
  temp = b.pop(i)
  edit_dist(i , a , b[:] ,cnt+1)
  b.insert(i,temp)
  #교체
  b[i] = a[i]
  edit_dist(i+1 , a , b[:] ,cnt+1)

edit_dist(0,a,b,0)

print(min(values))

# 1. dp 문제가 결국엔 반복되는 연산을 메모이제이션 하여서 연산속도를 늘리는거라고 생각해서 먼저 브루트포스로 접근하여 반복되는 부분을 메모이제이션 할려고 했다. 그래서 먼저 브루트포스를 이용하여 최소 편집거리를 출력하는 코드를 작성하였다.
# 2. 이제 메모이제이션을 어떻게 할지 고민하다가 딕셔너리를 사용하여 해당 문자열의 최소 편집거리를 계산하자는 생각으로 작성 할려고 했는데 막상 하기 힘들었다. 그래서 답지를 보게 되었다.

import sys

a = list(sys.stdin.readline().rstrip())
b = list(sys.stdin.readline().rstrip())

dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]

for i in range(len(b)+1):
  dp[0][i] = i
for i in range(len(a)+1):
  dp[i][0] = i

for i in range(1,len(a)+1):
  for j in range(1,len(b)+1):
    if a[i-1] == b[j-1]:
      dp[i][j] = dp[i-1][j-1]
    else:
      dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

print(dp[-1][-1])

# 1. 답지를 보고 이해하는데 좀 시간이 걸렸지만 다른 dp 문제 보다 이해가 더 잘되는 느낌이었다. 간단하게 설명하면 'sunday'에서 'saturday'로 변경할때 ''처럼 비어있는 문자열에서 's'가 되기 위해선 's'를 삽입 하면 되기 때문에 1이고 ''에서 'sa'로 변경할때 아까 빈 문자열에서 's'가 되는 1에다가 'a'가 'u'로 교체되는 값인 1을 더해서 저장해준다. 이처럼 차근차근 문자열의 길이를 늘려나가면서 최소 편집 거리를 저장하는 방식이었다.
# 2. dp 문제를 풀으면서 가장 dp 문제가 어렵고 dp 스럽게(?) 생각 하는 방식이 부족한거 같다. 이 책이 끝나면 dp를 집중적으로 공부 해야 될 거 같다.

