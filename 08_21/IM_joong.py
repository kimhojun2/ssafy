import math
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N+1)]
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 2:
                a = i
                b = j
    R = 0
    for y in range(N+1):
        for x in range(N+1):
            if arr[y][x] == 1:
                D = math.sqrt((a-y)**2 + (b-x)**2)
                if D > R:
                    R = math.ceil(D)

    print(f'#{tc} {R}')