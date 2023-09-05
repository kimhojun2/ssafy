T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))

    # print(cards)
    max_value = max(cards)
    count_arr = [0] * (max_value + 1)

    for num in cards:
        count_arr[num] += 1

    max_count = max(count_arr)

    print(max_count)