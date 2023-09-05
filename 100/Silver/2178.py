def BFS(arr, N, M):
    visited = [[0]*M for _ in range(N)]
    queue = []
    visited[0][0] = 1
    queue.append([0, 0])
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]


    while queue:
        t = queue.pop(0)
        y = t[0]
        x = t[1]
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0<=ny<N and 0<=nx<M:
                if not visited[ny][nx] and arr[ny][nx] == '1':
                    queue.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1

    print(visited[N-1][M-1])

N, M = map(int, input().split())
arr = [list(input())for _ in range(N)]
BFS(arr,N, M)