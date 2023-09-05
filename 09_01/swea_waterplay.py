from collections import deque
def BFS(N,M,y,x,arr):
    # visited = [[0]*M for _ in range(N)]
    queue = deque()
    queue.append((y,x))
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == 'L':
                    if visited[ni][nj] == 0:
                        visited[ni][nj] = visited[i][j] + 1
                        queue.append((ni, nj))
                    elif visited[ni][nj] > visited[i][j] + 1:
                        visited[ni][nj] = visited[i][j] + 1
                        queue.append((ni, nj))





T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input())for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    visited = [[0] * M for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 'W':
                BFS(N,M,y,x,arr)
    total = 0
    for v in visited:
        total += sum(v)
    print(f'#{tc} {total}')