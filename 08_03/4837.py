T = int(input())
for tc in range(1, T+1):
    N, K =map(int, input().split())
    arr = [i for i in range(1, 13)]
    result = 0
    #1<<12 --> 이진수 1을 왼쪽으로 12비트 이동 --> 1000000000000 = 2 ** 12
    for i in range(1<<12):
        sum_sub = 0
        subset = []
        for j in range(12):
            # i의 j번째 비트가 1인지 아닌지 알수 있다.
            # 12의 이진수 1100, 5의 이진수 0101 -> 1100 & 0101 -> 0100
            if 1 & (1<<j):
                sum_sub += arr[j]
                subset.append(arr[j])
                # print(subset)

        if len(subset) == N and sum_sub == K:
            result += 1
    print(f'#{tc} {result}')














    # count = 0
    # arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    # for i in range(1<<N):
    #     for j in range(N):
    #         if i & (1<<j):
    #             print(arr[j], end=', ')
    #
    #
    #
    #
    #
    #
    #
    # # lst = []
    # # start = 1
    # # while len(lst) <=N:
    # #
    # #     for i in range(1, 13):
    # #     start += 1
    # # print(count)
