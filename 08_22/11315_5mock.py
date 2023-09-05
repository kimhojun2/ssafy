def f(arr, N):

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                width = 1
                for z in range(1,5):
                    nj = j + z
                    if 0 <= nj < N and arr[i][nj] == 'o':
                        width += 1
                    else:
                        break
                if width == 5:
                    return 'YES'

    for x in range(N):
        for y in range(N):
            if arr[y][x] == 'o':
                length = 1
                for zz in range(1, 5):
                    ny = y + zz
                    if 0 <= ny < N and arr[ny][x] == 'o':
                        length += 1
                    else:
                        break
                if length == 5:
                    return 'YES'


    for a in range(N):
        for b in range(N):
            if arr[a][b] == 'o':
                right_diagonal = 1
                left_diagonal = 1
                for zzz in range(1,5):
                    na, nb = a + zzz, b + zzz
                    if 0 <= na <N and 0<= nb < N:
                        if arr[na][nb] == 'o':
                            right_diagonal += 1
                    else:
                        break

                for zzzz in range(1, 5):
                    nna, nnb = a+zzzz, b-zzzz
                    if 0 <= nna <N and 0<= nnb < N:
                        if arr[nna][nnb] == 'o':
                            left_diagonal += 1
                    else:
                        break
                if right_diagonal == 5 or left_diagonal == 5:
                    return 'YES'


    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input())for _ in range(N)]
    print(f'#{tc} {f(arr, N)}')