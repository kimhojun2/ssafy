from heapq import heappush, heappop
n, m =map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
dist = [[float('inf')]*m for _ in range(n)]

dy = [0,0,1,-1]
dx = [-1,1,0,0]

def dijkstra():
    pq = []
    dist[0][0] = MAP[0][0]  # 시작 지점의 최단거리는 해당 지점의 값
    heappush(pq, (MAP[0][0],0,0))   # 시작 지점 우선순위 큐에 넣기
    while pq:
        cost, y, x = heappop(pq)    # 현재지점 y, x 그 지점 까지 거리 cost
        # 이미 확인한 조표일 경우 (더 짧은 경로를 발견한 경우 ) continue
        if dist[y][x] < cost:
            continue
        for i in range(4):
            ny, nx = y +dy[i], x + dx[i]
            # 맵 범위를 벗어나는 경우 continue
            if ny < 0 or nx < 0 or ny >=n or nx >=m:
                continue
            nextcost = cost + MAP[ny][nx]   # 다음 지점 까지의 거리
            # 이미 발견한 경로가 더 짧을 경우 continue
            if dist[ny][nx] <= nextcost:
                continue
            dist[ny][nx] = nextcost
            heappush(pq,(nextcost, ny, nx))

    return dist[n-1][m-1]


print(dijkstra())