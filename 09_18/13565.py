from collections import deque
def BFS(i,j, M, N):
    global result
    queue = deque()
    # visited[i][j] = 1
    queue.append((i,j))
    while queue:
        y, x = queue.popleft()
        if y == (M-1):
            result = 'YES'
            break
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0<= ny < M and 0<= nx <N:
                if arr[ny][nx] == '0':
                    arr[ny][nx] = '1'
                    queue.append((ny,nx))


M, N = map(int, input().split())
arr = [list(input())for _ in range(M)]
# visited = [[0] * N for _ in range(M)]
result = 'NO'
dy = [0,1,0,-1]
dx = [1,0,-1,0]
for x in range(N):
    if arr[0][x] == '0':
        BFS(0,x,M,N)
        if result == 'YES':
            break
print(result)