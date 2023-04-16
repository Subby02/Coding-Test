def solution(words, queries):
  words.sort()
  print(words)
  result = []
  for query in queries:
    result.append(0)
    for word in words:
      if match(word, query):
        result[-1] += 1

  return result

def match(word, query):
  if len(word) != len(query):
    return False
  if query[0] == '?':
    for i in range(len(query)-1,-1,-1):
      if query[i] == '?':
        break
      if word[i] != query[i]:
        return False
  else:
    for i in range(len(query)):
      if query[i] == '?':
        break
      if word[i] != query[i]:
        return False
        
  return True


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
