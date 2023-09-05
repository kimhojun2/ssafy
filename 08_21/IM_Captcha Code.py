T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    Sample = list(map(int, input().split()))
    PassCode = list(map(int, input().split()))
    p = 0
    result = 0
    for s in Sample:
        if p < K:
            if s == PassCode[p]:
                p += 1

        else:
            result = 1

    print(f'#{tc} {result}')

