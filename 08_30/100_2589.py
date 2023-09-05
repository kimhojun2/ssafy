from collections import deque
def BFS(y,x,N, M):
    visited = [[0]*M for _ in range(N)]
    queue = deque()
    queue.append((y,x))
    # visited[y][x] = 1
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni <N and 0 <= nj < M and arr[ni][nj] == 'L':
                if ni != y or nj != x:
                    if visited[ni][nj] == 0:
                        visited[ni][nj] = visited[i][j] + 1
                        queue.append((ni, nj))
    mv = 0
    for v in visited:
        if max(v) > mv:
            mv = max(v)

    return mv

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
max_cnt = 0
for y in range(N):
    for x in range(M):
        if arr[y][x] == 'L':
            result = BFS(y,x,N,M)
            if result > max_cnt:
                max_cnt = result
print(max_cnt)

