def solution(N, stages):
  count = [0] * (max(stages)+1)
  
  for i in stages:
    count[i] += 1

  fail_rates = []
  length = len(stages)
  cnt = 0
  for i in range(1,N+1):
    if length-cnt > 0:
      fail_rates.append((count[i]/(length),i))
      length -= count[i]
    else:
      fail_rates.append((0,i))

  fail_rates.sort(reverse=True , key=lambda x : (x[0] , -x[1]))
  for i in range(len(fail_rates)):
    fail_rates[i] = fail_rates[i][1]
    
  return fail_rates

# 1. 문제를 보고 계수 정렬을 이용하면 시간복잡도를 획기적으로 줄일 수 있다 생각해서 계수정렬를 이용해서 카운트를 해주고 1부터 N까지 모든 스테이지의 실패율을 계산해 튜플로 저장하여 정렬 시켰다.
# 2. 튜플로 저장해서 다시 스테이지만 저장하는 부분이 마지막에 있는데 다른 코드를 보니 딕셔너리를 사용해서 정렬하는 것도 공부했다.