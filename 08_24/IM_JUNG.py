T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    MAX = 0
    for i in range(N):
        for j in range(i+1, N):
            num = str(numbers[i]*numbers[j])
            for k in range(len(num)-1):
                if int(num[k]) > int(num[k+1]):
                    break
            else:
                if MAX < int(num):
                    MAX = int(num)

    if MAX == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {MAX}')