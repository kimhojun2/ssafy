T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    arr= list(map(int, input().split()))

    current = 0
    count = 0
    while current < N-K:
        numbers = []
        for n in range(K, 0, -1):
            if (current + n) in arr:
                numbers.append(n)

        if numbers != []:
            current += numbers[0]
            count += 1
        else:
            count=0
            break

    print(f'#{tc}', count)
-------------------------------------------------------------------------------------------------------------------
    # ch = [0]*(N+1)
    #
    # for i in arr:
    #     ch[i] += 1
    # current = 0
    # count = 0
    # while current < N:
    #     if ch[current+K]:
    #         current += K
    #         count += 1
    #     else:
    #         for j in range(1, K):
    #             if ch[current + K - j]:
    #                 current += K-j
    #                 break
    #             else:
    #                 count = 0
    #                 break
    #     if current + K >=N:
    #         current = N
 -----------------------------------------------------------------------------------------------------------------
    # curr, cnt = 0, 0
    # #종점 도착 할때 까지 반복
    # # while curr != N:
    # #     # curr + K : 한번 충전으로 갈수 있는 거리, N : 종점까지 거리
    # #     if N <= curr + K:
    # #         curr = N
    # #         break
    # #     #충전소 뒤에서부터 순회
    # #     for i in range(len(arr)-1, -1, -1):
    # #         #리스트 arr의 값이 curr+K(한번 충전으로 갈수 있는 거리) 이내에 있다면
    # #         if arr[i] <= curr + K:
    # #             cnt += 1 #충전 횟수 증가
    # #             curr = arr[i] # 현재 위치를 충전소 위치로 변겅
    # #             arr = arr[i+1:] # 해당 충전소 이후의 정류장만 남기기
    # #             break
    # #         # 충전소를 찾지 못하였다면
    # #         if i ==0:
    # #             cnt = 0
    # #             curr = N #현재 위치를 종점으로
    # #
    # # print(~~~~)