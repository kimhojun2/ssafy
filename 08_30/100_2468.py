from collections import deque
def BFS(water,y,x, N):
    queue = deque()
    queue.append((y,x))
    # visited[y][x] = 1
    arr[y][x] = water
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0<= ni < N and 0<= nj < N:
                if arr[ni][nj] > water:
                    arr[ni][nj] = water
                    queue.append((ni, nj))
                    # visited[ni][nj] = 1

N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]

water = 100
visited = [[0]*N for _ in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
max_cnt = 0
while water >= 0:
    cnt = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] > water:
                BFS(water,y,x,N)
                cnt +=1
    if max_cnt < cnt:
        max_cnt = cnt
    water -= 1
print(max_cnt)
