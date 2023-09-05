T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    max = arr[-1]
    sum1 = 0
    result = 0
    for i in range(N):
        if arr[N-i-1] < max:
            result = (max * 1) - arr[N-i-1]
            sum1 += result
        elif arr[N-i-1] > max:
            max = arr[N-i-1]
    print(f'#{tc} {sum1}')