# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = []
#     for i in range(M+1):
#         arr.append(i)
#
#     bridge = 0
#     for i in range(1<<M):
#         lst = []
#         for j in range(M):
#             if i & (1<<j):
#                 lst.append(arr[j])
#         if len(lst) == N:
#             bridge +=1
#
#     print(bridge)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    bridge_1 = 1
    for i in range(M,M-N,-1):
        bridge_1 *= i
    bridge_2 = 1
    for j in range(1,N+1):
        bridge_2 *= j
    print(bridge_1//bridge_2)

