# queue
T = 10
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    q = []

    while numbers[-1] != 0:
        for i in range(1, 6):
            num = numbers.pop(0)
            if num - i <= 0:
                numbers.append(0)
                break
            else:
                numbers.append(num - i)
    print(f'#{tc}', end =' ')
    print(*numbers)