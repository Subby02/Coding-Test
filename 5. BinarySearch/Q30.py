# def solution(words, queries):
#   result = []
#   for query in queries:
#     result.append(0)
#     for word in words:
#       if match(word, query):
#         result[-1] += 1

#   return result

# def match(word, query):
#   if len(word) != len(query):
#     return False

#   for i in range(len(query)):
#     if query[i] == '?':
#       continue
#     if word[i] != query[i]:
#       return False
#   return True

# def solution(words, queries):
#   words.sort()
#   print(words)
#   result = []
#   for query in queries:
#     result.append(0)
#     for word in words:
#       if match(word, query):
#         result[-1] += 1

#   return result

# def match(word, query):
#   if len(word) != len(query):
#     return False
#   if query[0] == '?':
#     for i in range(len(query)-1,-1,-1):
#       if query[i] == '?':
#         break
#       if word[i] != query[i]:
#         return False
#   else:
#     for i in range(len(query)):
#       if query[i] == '?':
#         break
#       if word[i] != query[i]:
#         return False

#   return True

# 1. 그냥 단순하게 '?'스킵하고 나머지만 비교하는 방식으로 이진탐색을 쓰지 않고 작성해봤다. 정확성 테스트는 다 통과하였지만 역시 효율성 테스트는 다 실패했다. 이진탐색으로 풀어볼려고 생각을 많이 해봤다. 그래서 27번 문제처럼 words를 정렬하고 쿼리에 맞는 첫 부분과 마지막 부분의 인덱스를 구해서 개수를 셀려고 했는데 words의 길이가 다 다르다 보니까 정렬이 제대로 되지 않았다. 그부분에 막혀서 이방법은 아니다고 생각하여 다른 방법을 모색했지만 찾지 못해 답을 보게 되었다.

from bisect import bisect_left , bisect_right

def solution(words, queries):
  array = [[] for _ in range(10001)]
  reverse_array = [[] for _ in range(10001)]
  
  for word in words:
    array[len(word)].append(word)
    reverse_array[len(word)].append(word[::-1])
  
  for i in range(10001):
    array[i].sort()
    reverse_array[i].sort()

  cnt_list = []
  for query in queries:
    if query[-1] == '?':
      cnt = count_word(array[len(query)] , query)
      cnt_list.append(cnt)
    else:
      cnt = count_word(reverse_array[len(query)] , query[::-1])
      cnt_list.append(cnt)

  return cnt_list

def query_range(query):
  min_query = ''
  max_query = ''
  for i in range(len(query)):
    if query[i] == '?':
      min_query += 'a'
      max_query += 'z'
    else:
      min_query += query[i]
      max_query += query[i]

  return min_query , max_query

def count_word(array , query):
  min_query , max_query = query_range(query)
  
  left = bisect_left(array,min_query)
  right = bisect_right(array,max_query)

  return right - left

# 1. 답을 보고 내가 생각했던 방법이 맞았다는걸 깨달았다. 그대신 words의 길이에 따라 나누어서 따로 쿼리에 맞춰서 비교하는 방법을 생각하지 못했고 쿼리에 '?'를 'a'와 'z'로  변환하여 비교 할 수 있다는걸 생각 못했다.
# 2. words에서 쿼리에 맞는 첫부분과 마지막부분의 인덱스를 이진탐색으로 직접 구현 할려고 했지만 실패했다..
# 3. 그래서 어쩔수 없이 bisect 라이브러리를 사용했다. 나중에 시간이 남을때 직접 이진탐색을 구현하는 코드를 작성 해봐야될거 같다.
# 4. 맨처음에 word의 최대 길이가 10000인것을 보고 10000개의 배열을 선언하여 길이를 인덱스로 하여 작성할려했지만 뭔가 딕셔너리를 사용하여 더 쉬울거 같아서 딕셔너리로 작성하였는데 '?'가 끝에 있는 쿼리를 처리할때 리버스된 배열이 필요하므로 딕셔너리에 'orign'과 'reverse' 키를 넣어서 따로 저장할려고 했지만 그러면 딕셔너리안의 또다른 딕셔너리를 넣거나 '?'가 끝에 있는 쿼리를 처리 할때 해당 words 배열을 각각 리버스하고 다시 정렬하여 비교하는 방법은 시간 초과가 떳다. 그래서 다시 처음대로 배열로 변경하였다.
# 5. 이진탐색 문제를 풀때 내가 처음에 생각했던 부분이 맞는데 코드를 작성하면서 생기는 문제 때문에 다른 방법이 있겠지라는 생각으로 코드를 작성하게 되어서 자꾸 못푸는거 같다. 확실히 다른 문제를 풀때보다 이진탐색 문제가 좀 더 난이도가 있는거 같다.