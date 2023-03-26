import sys
import heapq

n = int(sys.stdin.readline())
 
card = []
for _ in range(n):
    card.append(int(sys.stdin.readline()))

heapq.heapify(card)

total = 0
for _ in range(n-1):
    sum = heapq.heappop(card)+heapq.heappop(card)
    total += sum
    heapq.heappush(card,sum)
    
print(total)

# 1. 문제를 키니까 성공이 떠있어서 뭐지 했는데 알고보니 6개월 전에 한번 풀었던 문제였다. 그래서 문제를 다시 읽어보니 우선순위큐를 이용해서 풀었던게 기억이 났다. 일단 우선순위 큐를 사용하지 않고 다시 풀어봤는데 계속 시간초과가 떳다 ㅎ 아무리 최적화 해도 안되서 우선순위 큐 밖에 답이 없다는 걸 알았다. 코드는 6달 전에 풀었던 코드이다.