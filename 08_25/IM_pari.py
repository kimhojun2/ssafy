T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    max_pari = 0
    for i in range(N):
        for j in range(N):
            pari1 = arr[i][j]
            pari2 = arr[i][j]
            di = [0,1,0,-1]
            dj = [1,0,-1,0]
            for d in range(4):
                for p in range(1, M):
                    ni, nj = i +di[d]*p, j + dj[d]*p
                    if 0<= ni <N and 0 <= nj < N:
                        pari1 += arr[ni][nj]
            dy = [1,1,-1,-1]
            dx = [1,-1,1,-1]
            for dd in range(4):
                for pp in range(1,M):
                    ny, nx = i + dy[dd]*pp, j + dx[dd]*pp
                    if 0 <= ny <N and 0 <= nx < N:
                        pari2 += arr[ny][nx]

            if max(pari2, pari1) > max_pari:
                max_pari = max(pari2, pari1)

    print(f'#{tc} {max_pari}')
