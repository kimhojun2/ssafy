T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = []

    while len(numbers)>0:
        max_value = max(numbers)
        numbers.remove(max_value)
        result.append(max_value)

        min_value = min(numbers)
        numbers.remove(min_value)
        result.append(min_value)

    print(f'#{tc}', *result[:10])