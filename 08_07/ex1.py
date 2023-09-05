T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    sample = list(map(int, input().split()))
    code = list(map(int, input().split()))

    cnt = 0
    result = 0

    for i in range(N):
        if code[cnt] == sample[i]:
            cnt+=1
        if cnt == K:
            result = 1
            break

    print(f'#{tc} {result}')
