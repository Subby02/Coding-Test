def solution(p):
  if p == '':
    return p

  u , v = divide(p)
  print(u,v)
  if isCorrect(u):
    return u + solution(v)
  else:
    return '(' + solution(v) + ')' + reverse(u[1:-1])

def reverse(w):
  new_w = ''
  for word in w:
    if word == '(':
      new_w+=')'
    else:
      new_w+='('
  return new_w
  
def divide(w):
  left = 0
  right = 0
  for i in range(len(w)):
    if w[i] == '(':
      left+=1
    elif w[i] == ')':
      right+=1
    if left == right:
      u = w[:i+1]
      v = w[i+1:]
      break
  return u , v

def isCorrect(w):
  stack = []
  for i in range(len(w)):
    if w[i] == '(':
      stack.append(w[i])
    elif w[i] == ')':
      if not stack:
        return False
      if stack[-1] == '(':
        stack.pop()
      else:
        return False
  return True
  
def isBalance(w):
  left = 0
  right = 0
  for i in range(len(w)):
    if w[i] == '(':
      left+=1
    elif w[i] == ')':
      right+=1
  if left == right:
    return True
  return False

print(solution('(()())()'))

# 1. 문제를 이해 하는데 살짝 시간이 걸렸지만 이해하고 나서 그냥 '용어의 정의'부분만 구현하면 어려운 문제는 아닌거 같다.
# 2. 다른 사람들의 풀이를 보니 정말 파이썬 하게 푼거 보고 감탄했다. 좀 더 파이썬적으로 풀 수 있도록 노력 해야 될 거 같다.