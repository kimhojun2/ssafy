def BFS(arr, i, j):
    visited = [[0]*N for _ in range(M)]
    queue = []
    queue.append([i, j])
    visited[i][j] = 1
    arr[i][j] = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while queue:
        t = queue.pop(0)
        v = t[0]
        vv = t[1]
        for d in range(4):
            nv, nvv = v + di[d], vv + dj[d]
            if 0 <= nv < M and 0 <= nvv < N:
                if not visited[nv][nvv] and arr[nv][nvv] == 1:
                    visited[nv][nvv] = 1
                    arr[nv][nvv] = 0
                    queue.append([nv, nvv])



T = int(input())
for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*N for _ in range(M)]
    for b in range(K):
        z, zz = map(int, input().split())
        arr[z][zz] = 1


    cnt = 0
    for y in range(M):
        for x in range(N):
            if arr[y][x] == 1:
                BFS(arr, y, x)
                cnt +=1

    print(cnt)