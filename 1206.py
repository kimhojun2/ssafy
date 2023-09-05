T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))


    for i in range(N - 2, 2, -1):
        for j in range(2, i):
            if arr[j] > arr[j-1]-2 and arr[j] > arr[j-2]-2 and arr[j] > arr[j+1]




    print(f'#{tc}', count)
