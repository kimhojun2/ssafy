# 자리배정
C, R = map(int, input().split())    # C가로 R세로
K = int(input())
arr = [[0]*C for _ in range(R)]
def chair(C, R, K, arr):
    cnt = 1
    # print(cnt)
    start = 0
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    i = R-1
    j = 0
    arr[i][j] = 1
    while cnt != C*R:
        if cnt == K:
            arr[i][j] = cnt
            break
        ni, nj = i + di[start % 4], j + dj[start % 4]

        if 0 <= ni <R and 0 <= nj <C:
            if arr[ni][nj] == 0:
                arr[i][j] = cnt
                cnt += 1
                i, j = ni, nj
            else:
                start += 1
        else:
            start += 1

    return j+1, R - i, cnt


a, b, cnt = chair(C,R,K,arr)
if cnt != K:
    print(0)
else:
    print(a, b)

