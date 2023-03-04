# 접근 #1
# def solution(n, weak, dist):
#   dist.sort(reverse=True)

#   min_person = 1e9
#   #시작 취약지점을 지정
#   for i in range(len(weak)):
#     #취약지점 기준으로 취약지점 한바퀴 돌기
#     person = 0
#     check_weak = []
#     for j in range(len(weak)):
#       turn = weak[(i+j)%len(weak)]
#       if turn in check_weak:
#         continue
#       right_check_weak = []
#       left_check_weak = []

#       #weak[(i+j)%len(weak)]
#       #오른쪽 , 왼쪽 중에서 많은 취약지점을 가는 방향을 선택
#       for j in range(dist[person]+1):
#         if (turn-j)%n in weak:
#           right_check_weak.append((turn-j)%n)
#       for j in range(dist[person]+1):
#         if (turn+j)%n in weak:
#           left_check_weak.append((turn+j)%n)

#       if len(right_check_weak) >= len(left_check_weak):
#         check_weak+=right_check_weak
#       else:
#         check_weak+=left_check_weak

#       person+=1
#       if person >= len(dist):
#         person = 1e9
#         break
#       check_weak = list(set(check_weak))
#       check_weak.sort()
#       if check_weak == weak:
#         break
#     min_person = min(person,min_person)

#   if min_person == 1e9:
#     return -1

#   return min_person

# 채점 결과
# 정확성: 72.0
# 합계: 72.0 / 100.0
# 어떻게 접근 해야 될지 잘 몰라서 그리디하게 접근을 해봤는데 상당히 좋은 점수를 받았지만 이방법이 아닌걸 알게 되었음.

from itertools import permutations


def solution(n, weak, dist):
  length = len(weak)
  for i in range(length):
    weak.append(weak[i] + n)
  answer = len(dist) + 1

  for start in range(length):
    for friend in permutations(dist, len(dist)):
      count = 1
      position = weak[start] + friend[count - 1]
      for index in range(start, start + length):
        if position < weak[index]:
          count += 1
          if count > len(dist):
            break
          position = weak[index] + friend[count - 1]
      answer = min(answer, count)

  if answer > len(dist):
    return -1
  return answer


# 1. 조건을 읽고 완전탐색으로 할 수 있다는걸 판별 하고 모든 경우의 수를 검사하는 방법을 좀 더 생각할 수 있는 능력을 길려내야 될 거 같음
# 2. 접근 #1에선 배열의 인덱스를 나눠서 나머지를 이용하여 접근 하였지만 배열을 2배로 늘려서 한바퀴를 설정 할 수 있는 방법을 알게됨
# 3. position 변수를 이용해서 position 보다 높으면 count를 1 증가하고 position을 반영 해주는 방법을 떠 올리지 못해서 책을 보고 코드를 이해함
