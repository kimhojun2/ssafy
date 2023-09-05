from collections import deque

def BFS(arr, N, M):
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    day = 0
    while queue:
        y, x, cnt = queue.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0<=ny<M and 0<=nx<N:
                if arr[ny][nx] == 0:
                    queue.append((ny, nx, cnt + 1))
                    arr[ny][nx] = 2
                    if cnt + 1 > day:
                        day = cnt
    for rows in arr:
        if 0 in rows:
            day = -1
            break

    print(day)


N, M = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(M)]
queue = deque()
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1:
            queue.append((i, j, 1))

BFS(arr, N, M)