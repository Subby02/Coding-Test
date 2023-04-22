import sys

n = int(sys.stdin.readline())

time = [list(map(int , sys.stdin.readline().split())) for _ in range(n)]

d = [0] * (n+1)

# i번째 까지 일을 했을때
for i in range(n):
  # i번째 다음 상담 부터 마지막 상담까지 최대 수익 비교
  for j in range(i+time[i][0] , n+1):
    d[j] = max(d[j] , d[i] + time[i][1]) 
  print(d)

print(d[-1])

# 위 방식은 바텀업 방식

n = int(sys.stdin.readline())

t = []
p = []
for _ in range(n):
  x, y = map(int, sys.stdin.readline().split())
  t.append(x)
  p.append(y)

d = [0] * (n+1)

for i in range(n-1,-1,-1):
  if t[i] + i <= n:
    d[i] = max(p[i]+d[t[i] + i] , d[i+1])
  else:
    d[i] = d[i+1]

print(d[0])

# 1. 못풀었다. 코드를 작성하긴 했는데 케이스 4번에서 자꾸 80이 출력되서 코드를 다시 분석해보니 내가 접근 했던 방식은 그리디였다. 어떤 케이스는 한번 쉬고 다른 상담을 잡으면 더 큰 값이 더해지는데 내가 짠 방식은 최대한 상담이 끝나면 다음 상담을 넣는 방식이어서 특정 케이스에서 답이 틀렸다.
# 2. 다른 방식으로 접근 할려고 했는데 도저히 접근을 어떻게 해야될지 몰랐다. 답을 보기 전에 탑 다운 방식으로 생각을 해보긴 했는데 포기했다.
# 3. 답 설명 부분만 보고 이해를 할려고 했지만 솔직히 이해가 잘 안되서 코드도 보게 되었다. 코드를 보고 직접 다시 작성하면서 얼추 이해가 됬지만 100%이해 했다고 하긴 힘들거 같다. 구글링을 통해 다른 방식을 찾아봤다. 바텀업 방식으로 작성한걸 봤는데 그 방식도 이해가 잘 되진 않았다. 

