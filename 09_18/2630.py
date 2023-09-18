def a1(N):
    global blue_cnt, white_cnt
    blue = 0
    white = 0
    for i1 in range(N//2):
        for j1 in range(N//2, N):
            if arr[i1][j1] == 1:
                blue +=  1
            else:
                white += 1

    if blue == 0:
        white_cnt += 1
    elif white == 0:
        blue_cnt += 1
    else:
        a1(N//2), a2(N//2), a3(N//2), a4(N//2)


def a2(N):
    global blue_cnt, white_cnt
    blue = 0
    white = 0
    for i2 in range(N // 2):
        for j2 in range(N // 2):
            if arr[i2][j2] == 1:
                blue += 1
            else:
                white += 1

    if blue == 0:
        white_cnt += 1
    elif white == 0:
        blue_cnt += 1
    else:
        a1(N//2), a2(N//2), a3(N//2), a4(N//2)


def a3(N):
    global blue_cnt, white_cnt
    blue = 0
    white = 0
    for i3 in range(N // 2, N):
        for j3 in range(N // 2):
            if arr[i3][j3] == 1:
                blue += 1
            else:
                white += 1

    if blue == 0:
        white_cnt += 1
    elif white == 0:
        blue_cnt += 1
    else:
        a1(N//2), a2(N//2), a3(N//2), a4(N//2)


def a4(N):
    global blue_cnt, white_cnt
    blue = 0
    white = 0
    for i4 in range(N // 2, N):
        for j4 in range(N // 2, N):
            if arr[i4][j4] == 1:
                blue += 1
            else:
                white += 1

    if blue == 0:
        white_cnt += 1
    elif white == 0:
        blue_cnt += 1
    else:
        a1(N//2), a2(N//2), a3(N//2), a4(N//2)


N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
blue_cnt = 0
white_cnt = 0

a1(N)
a2(N)
a3(N)
a4(N)
print(white_cnt, blue_cnt)