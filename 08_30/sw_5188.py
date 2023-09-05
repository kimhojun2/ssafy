dir = [(0,1), (1,0)]

def dfs(x,y,sum_v):
    global result
    # 가지치기 : 불필요한 경롤르 차단 -> 조건에 맞지 않으면 탐색하지 않는다
    if sum_v >= result:
        return
    if x == N-1 and y == N-1:
        if sum_v < result:
            result = sum_v
        return

    for dx, dy in dir:
        nx, ny = x+dx, y+dy
        if -1 < nx<N and -1<ny<N:
            dfs(nx, ny, sum_v+arr[ny][nx])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    result = float('inf') # 무한대 표현, 음의 무한대 -float('inf')
    dfs(0,0,arr[0][0])
    print(f'#{tc} {result}')