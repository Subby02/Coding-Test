from collections import deque

def get_next_pos(robot_pos , board):
  next_pos = []
  robot_pos = list(robot_pos)
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  #상하좌우 이동
  for i in range(4):
    if board[robot_pos[0][0]+dx[i]][robot_pos[0][1]+dy[i]] == 0 and board[robot_pos[1][0]+dx[i]][robot_pos[1][1]+dy[i]] == 0:
      next_pos.append({(robot_pos[0][0]+dx[i],robot_pos[0][1]+dy[i]),(robot_pos[1][0]+dx[i],robot_pos[1][1]+dy[i])})

  #로봇이 수평일때
  if robot_pos[0][0] == robot_pos[1][0]:
    for i in [1,-1]:
      if board[robot_pos[0][0]+i][robot_pos[0][1]] == 0 and board[robot_pos[1][0]+i][robot_pos[1][1]] == 0 :
        next_pos.append({(robot_pos[0][0],robot_pos[0][1]),(robot_pos[1][0]+i,robot_pos[0][1])})
        next_pos.append({(robot_pos[0][0]+i,robot_pos[1][1]),(robot_pos[1][0],robot_pos[1][1])})
  #로봇이 수직일때
  else:
    for i in [1,-1]:
      if board[robot_pos[0][0]][robot_pos[0][1]+i] == 0 and board[robot_pos[1][0]][robot_pos[1][1]+i] == 0 :
        next_pos.append({(robot_pos[0][0],robot_pos[0][1]),(robot_pos[0][0],robot_pos[1][1]+i)})
        next_pos.append({(robot_pos[1][0],robot_pos[0][1]+i),(robot_pos[1][0],robot_pos[1][1])})

  return next_pos
  


def solution(board):
  visited = []
  n = len(board)
  new_board = [[1] * (n+2) for _ in range(n+2)]
  for x in range(1,n+1):
    for y in range(1,n+1):
      new_board[x][y] = board[x-1][y-1]

  q = deque()
  robot_pos = {(1, 1), (1, 2)}
  q.append((robot_pos , 0))
  visited.append(robot_pos)
  while q:
    robot_pos , cost = q.popleft()
    if (n,n) in robot_pos:
      return cost
    
    for pos in get_next_pos(robot_pos,new_board):
      if pos not in visited:
        q.append((pos,cost+1))
        visited.append(pos)

  return 0

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))

'''
1. 이문제를 보고 맨처음에 별짓을 다한거 같다. 처음에 생각한 방법은 board를 반전 시켜서 벽을 0 길을 1로 바꾸고 bfs를 이용해서 (1,1)에서 갈 수 있는 길한테 +1을 해서 모든 길에 가는 거리를 board에 입력 해주고 dfs를 이용해서 (n,n) 까지 가는 모든 경로를 리스트로 저장한다. 그다음에 그 경로들중에서 코너가 가장 적은 수를 저장한다. 그리고 (n,n) 까지의 거리에서 최소 코너를 뺀 값을 반환한다. 회전을 하면 사실상 2칸을 이동하는 격이므로 코너 수를 빼줬다. 예제를 보면 (n,n) 까지의 거리는 9이고 코너 수가 가장 적은 경로는 2개의 코너를 갖고 있는 코너 이므로 9-2 = 7 답하고 같지만 이게 정확히 맞다는 확신이 들지도 못했고 경로들 중에서 코너를 셀때 회전 가능한 여부도 판단해야 되서 너무 문제가 복잡해져서 이 방법 말고 다른 방식으로 접근 해야 된다는 걸 알게 되었다. 
2. 그래서 생각한 방법은 직접 움직여서 모든 경우의 수를 계산 하자는 생각으로 로봇이 수직일때 수평일때 오른쪽이나 왼쪽 , 위쪽이나 아래쪽을 축으로 하여 회전 하는 함수를 각각 만들다 보니 함수가 16개 이므로 이 방법 보단 좀 더 효율적인 방법이 없나 고민 하게 되었다.
3. 결국 3일 동안 개인정비시간 1시간 씩 투자 해봤지만 진전이 없어 책에 있는 답을 보게 되었고 코드는 보지 않았고 설명을 이해한 다음 내가 직접 코드를 작성하였다. 프로그래머스에 제출을 했는데 자꾸 테스트 13에서 시간 초과가 나서 책의 코드를 보면서 비교해가면서 문제점을 파악 해봤는데 다른점은 로봇의 위치를 나는 리스트로 저장하였고 책은 딕셔너리를 사용했다는 점이 뭔가 싸했다. 그래서 딕셔너리랑 리스트 시간복잡도 차이를 찾아보니 요소가 있는지 검사하는 in 키워드 사용시 리스트는 O(n)이고 딕셔너리는 O(1)인 걸 알게 되었다. 딕셔너리를 변경하니 바로 통과하였다.
4. 앞에 시도 했던 코드들은 결국 중간에 작성하다가 방법을 바꿔서 따로 저장을 해놓지 않았다. 
''' 
