from collections import deque

def BFS(n,m,y,x,arr):
    queue = deque()
    arr[y][x] = 0
    queue.append((y,x))
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    cnt = 1
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0<= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 1:
                    arr[ni][nj] = 0

                    queue.append((ni, nj))
                    cnt += 1

    return cnt


n, m = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(n)]

counting = 0
ans = 0
for y in range(n):
    for x in range(m):
        if arr[y][x] == 1:
            result = BFS(n,m,y,x,arr)
            counting +=1
            if result > ans:
                ans = result

print(counting)
print(ans)