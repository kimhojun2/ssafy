T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input().split('0'))
    print(f'#{tc}', len(list(set(sorted(arr)))[-1]))

    # numbers = []
    # for i in range(len(arr)):
    #     a = int(arr[i])
    #     numbers.append(a):