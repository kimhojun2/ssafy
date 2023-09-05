T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    num = 0
    for i in range(1<<12):
        total = 0
        lst = []
        for j in range(12):
            if i & (1<<j):
               total += arr[j]
               lst.append(arr[j])

        if len(lst) == N and total == K:
            num+=1


    print(f'#{tc} {num}')



