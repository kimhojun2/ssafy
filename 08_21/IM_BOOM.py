T = int(input())
for tc in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            cnt += arr[i][j]
            for d in range(4):
                for p in range(1, P+1):
                    ni, nj = i + di[d]*p, j +dj[d]*p
                    if 0<= ni <N and 0<= nj <N:
                        cnt+=arr[ni][nj]

            if cnt > max_cnt:
                max_cnt = cnt

    print(f'#{tc} {max_cnt}')