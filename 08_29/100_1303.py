from collections import deque
def BFS_W(N,M,y,x):
    queue = deque()
    queue.append((y, x))
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    w_cnt = 0
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0<= ni < M and 0 <= nj < N:
                if arr[ni][nj] == 'W':
                    arr[ni][nj] = 0
                    queue.append((ni, nj))
                    w_cnt +=1

    if w_cnt == 0:
        w_cnt = 1

    return w_cnt


def BFS_B(N, M, y, x):
    queue = deque()
    queue.append((y, x))
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    b_cnt = 0
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < M and 0 <= nj < N:
                if arr[ni][nj] == 'B':
                    arr[ni][nj] = 0
                    queue.append((ni, nj))
                    b_cnt += 1
    if b_cnt == 0:
        b_cnt = 1
    return b_cnt


N, M = map(int, input().split())
arr = [list(input())for _ in range(M)]
W = 0
B = 0
for y in range(M):
    for x in range(N):
        if arr[y][x] == 'W':
            result = BFS_W(N,M,y,x)
            W += result**2
        if arr[y][x] == 'B':
            result = BFS_B(N,M,y,x)
            B += result ** 2

print(W, B)