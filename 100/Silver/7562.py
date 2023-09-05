def BFS(N, sy, sx, ey, ex):
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append([sy, sx])
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    if sy == ey and sx == ex:
        return 0

    while queue:
        t = queue.pop(0)
        y = t[0]
        x = t[1]
        for d in range(8):
            ny, nx = y + dy[d], x + dx[d]
            if 0<=ny<N and 0<=nx<N:
                if not visited[ny][nx]:
                    queue.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1
                    if ny == ey and nx == ex:
                        queue.clear()
                        return visited[ey][ex]

    # print(visited[ey][ex])


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    print(BFS(N, sy, sx, ey, ex))