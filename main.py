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
