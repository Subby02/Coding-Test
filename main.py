dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
all_root = []


def dfs(x, y, root):
  n = len(board)
  if x == n and y == n:
    all_root.append(root)
    return

  root.append((x, y))

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or ny < 0 or nx >= n or ny >= n:
      continue

    if board[nx][ny] == 1:
      continue

    dfs(nx, ny, root)


def solution(board):
  dfs(0, 0, [])
  for root in all_root:
    print(root)


board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]
solution(board)