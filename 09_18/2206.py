from collections import deque
def BFS(N,M):
    visited = [[0]*M for _ in range(N)]
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = 1
    while queue:
        y, x, c = queue.popleft()
        for d in range(4):
            ny, nx = y+di[d], x+dj[d]
            if 0<= ny < N and 0<= nx <M:
                if c == 0:
                    if arr[ny][nx] == '0':
                        if visited[ny][nx] == 0 or visited[ny][nx] >= visited[y][x] + 1:
                            visited[ny][nx] = visited[y][x] + 1
                            queue.append((ny, nx, 0))
                    if arr[ny][nx] == '1':
                        if visited[ny][nx] == 0 or visited[ny][nx] >= visited[y][x] + 1:
                            visited[ny][nx] = visited[y][x] + 1
                            queue.append((ny, nx, 1))

                else:
                    if arr[ny][nx] == '0':
                        if visited[ny][nx] == 0 or visited[ny][nx] >= visited[y][x] + 1:
                            visited[ny][nx] = visited[y][x] + 1
                            queue.append((ny, nx, 1))
    if visited[N-1][M-1] == 0:
        print(-1)
        print(visited)
    else:
        print(visited[N-1][M-1])

N, M = map(int, input().split())
arr = [list(input())for _ in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
BFS(N,M)