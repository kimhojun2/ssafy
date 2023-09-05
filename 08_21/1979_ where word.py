def f(arr, N, K):
    cnt = 0
    for j in range(N):
        for i in range(N):
            if arr[i][j] == 1:
                ly = 0
                for d in range(N - i):
                    ni = i + d
                    if 0 <= ni < N:
                        if arr[ni][j] == 0:
                            break
                        else:
                            ly += 1
                    else:
                        break
                if ly == K:
                    if arr[i-1][j] == 0 or i == 0:
                        cnt += 1


    for y in range(N):
        for x in range(N):
            if arr[y][x] == 1:
                lx = 0
                for d in range(N - x):
                    nx = x + d
                    if 0 <= nx < N:
                        if arr[y][nx] == 0:
                            break
                        else:
                            lx += 1
                    else:
                        break
                if lx == K:
                    if arr[y][x-1] == 0 or x == 0:
                        cnt += 1



    return cnt

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]



    print(f'#{tc} {f(arr, N, K)}')