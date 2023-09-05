from collections import deque
def BFS(N,M,y,x):
    visited = [[0]*M for _ in range(N)]
    queue = deque()
    visited[y][x] = 1
    queue.append((y,x))
    lst = deque()
    lst.append((y,x))
    m = True
    while queue and m:
        i, j = queue.popleft()
        for d in range(8):
            ni, nj = i + di[d], j + dj[d]
            if 0<= ni < N and 0<= nj < M:
                if not visited[ni][nj]:
                    if arr[ni][nj] > arr[i][j]:
                        m = False
                        break
                    elif arr[ni][nj] == arr[i][j]:
                        visited[ni][nj] = 1
                        queue.append((ni, nj))
                        lst.append((ni,nj))
    if m:
        lst1.extend(lst)
        return 1
    else:
        return 0



N, M = map(int, input().split())
no = deque()
arr = [list(map(int, input().split()))for _ in range(N)]
cnt = 0
di = [0,1,0,-1,1,1,-1,-1]
dj = [1,0,-1,0,1,-1,1,-1]
lst1 = deque()
for y in range(N):
    for x in range(M):
        if (y, x) not in lst1:
            cnt += BFS(N,M,y,x)
print(cnt)

