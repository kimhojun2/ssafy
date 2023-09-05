from collections import deque
def BFS(n,m,y,x):
    queue = deque()
    visited = [[0]*m for _ in range(n)]
    queue.append((y,x))
    while queue:
        i, j = queue.popleft()
        di = [0,1,0,-1]
        dj = [1,0,-1,0]
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0<= ni < n and 0 <= nj < m:
                if not visited[ni][nj] and arr[ni][nj] == 1:
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append((ni, nj))

    for v in range(len(visited)):
        for vv in range(len(visited[v])):
            if visited[v][vv] == 0 and arr[v][vv] == 1:
                visited[v][vv] = -1


    return visited
n, m = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]

for y in range(n):
    for x in range(m):
        if arr[y][x] == 2:
            A = BFS(n,m,y,x)
            break

for a in A:
    print(*a)