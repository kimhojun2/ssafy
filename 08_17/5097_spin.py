T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    m = 1
    while m <= M:
        num = numbers.pop(0)
        numbers.append(num)
        m += 1

    print(f'#{tc} {numbers[0]}')
