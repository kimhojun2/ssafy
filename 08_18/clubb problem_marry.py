from collections import deque


def bfs(coco, par, arr):
    d = deque()
    visited = [0] * (N + 1)
    d.append(coco)
    visited[coco] = 1
    while d:
        v = d.popleft()
        for i in range(1, N + 1):
            if visited[i] == 0 and arr[v][i] == 1:
                d.append(i)
                visited[i] = 1
                if i == par:
                    return 'YES'

    return 'NO'



N = int(input())
T = int(input())
jung = [list(map(int, input().split())) for _ in range(T)]
arr = [[0] * (N + 1) for _ in range(N + 1)]
for k in range(T):
    x, y = jung[k][0], jung[k][1]
    arr[x][y] = 1
    arr[y][x] = 1

coco = int(input())
par = int(input())

print(bfs(coco, par, arr))
