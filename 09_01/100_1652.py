N = int(input())
arr = [list(input())for _ in range(N)]


garo = 0
for i in range(N):
    cnt1 = 0
    for j in range(N):
        if arr[i][j] == '.':
            cnt1 += 1
        elif arr[i][j] == 'X':
            if cnt1 >= 2:
                garo += 1
                cnt1 = 0
            else:
                cnt1 = 0
    if cnt1 >= 2:
        garo += 1

sero = 0
for x in range(N):
    cnt2 = 0
    for y in range(N):
        if arr[y][x] == '.':
            cnt2 += 1
        elif arr[y][x] == 'X':
            if cnt2 >= 2:
                sero += 1
                cnt2 = 0
            else:
                cnt2 = 0
    if cnt2 >= 2:
        sero += 1

print(garo, sero)