N = int(input())
num = int(input())
arr = [[0]*N for _ in range(N)]

def snail(N, num, arr):
    cnt = N*N
    # print(cnt)
    start = 0
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    y = 0
    x = 0
    i = 0
    j = 0
    while cnt != 0:
        if cnt == num:
            y = i + 1
            x = j + 1
            arr[i][j] = 1
        if cnt == 1:
            arr[i][j] = 1
            break

        ni, nj = i + di[start % 4], j + dj[start % 4]

        if 0 <= ni <N and 0 <= nj <N:
            if arr[ni][nj] == 0:
                arr[i][j] = cnt
                i, j = ni, nj
                cnt -= 1
            else:
                start += 1
        else:
            start += 1

    return y, x


y, x = snail(N, num, arr)
for rows in arr:
    print(*rows)

print(y, x)


