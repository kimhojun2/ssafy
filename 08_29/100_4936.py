from collections import deque

def BFS(arr,i,j,w,h):
    global cnt
    visited = [[0]*(w) for _ in range(h)]
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    arr[i][j] = 2
    di = [0,1,0,-1,1,1,-1,-1]
    dj = [1,0,-1,0,1,-1,1,-1]
    while queue:
        t = queue.popleft()
        v = t[0]
        vv = t[1]
        for d in range(8):
            nv, nvv = v + di[d], vv + dj[d]
            if 0<= nv < h and 0<= nvv < w:
                if not visited[nv][nvv] and arr[nv][nvv] == 1:
                    visited[nv][nvv] = 1
                    arr[nv][nvv] = 2
                    queue.append((nv, nvv))
    cnt += 1


while True:
    cnt = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    else:
        arr = [list(map(int, input().split()))for _ in range(h)]

        for y in range(h):
            for x in range(w):
                if arr[y][x] == 1:
                    BFS(arr, y, x, w, h)
    print(cnt)