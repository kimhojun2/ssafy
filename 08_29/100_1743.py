from collections import deque

def BFS(N,M,y, x):
    queue = deque()
    queue.append((y,x))
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    cnt = 0
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0<= ni< N and 0 <= nj < M:
                if arr[ni][nj] == 1:
                    arr[ni][nj] = 0
                    queue.append((ni, nj))
                    cnt +=1
    return cnt

N, M, K = map(int, input().split())
arr = [[0]*(M) for _ in range(N)]
for k in range(K):
    y, x = map(int, input().split())
    arr[y-1][x-1] = 1

big = 0
for y in range(N):
    for x in range(M):
        if arr[y][x] == 1:
            result = BFS(N,M,y,x)
            if result > big:
                big = result
print(big)