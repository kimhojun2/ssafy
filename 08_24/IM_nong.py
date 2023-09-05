T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input())for _ in range(N)]
    ox = N//2

    profit = 0
    for i in range(N):
        profit += int(arr[i][ox])
        if 0 < i <= (N//2):
            for j in range(1, i+1):
                profit += int(arr[i][ox+j])
                profit += int(arr[i][ox-j])
        elif i > (N//2):
            for k in range(1, N-i):
                profit += int(arr[i][ox+k])
                profit += int(arr[i][ox-k])

    print(f'#{tc} {profit}')