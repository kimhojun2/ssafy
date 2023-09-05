# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     result = []
#     for n in range(N):
#         A, B = map(int, input().split())
#
#         for s in range(A, B+1):
#             result.append(s)
#     P = int(input())
#     r =[]
#     for p in range(1, P+1):
#         c = int(input())
#         r.append(result.count(c))
#     print(f'#{tc}', end = ' ')
#     print(*r)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stop = [0]*5001
    for n in range(N):
        A, B = map(int, input().split())
        for s in range(A, B+1):
            stop[s] += 1
    P = int(input())
    result = []
    for p in range(1, P+1):
        result.append(stop[int(input())])
    print(f'#{tc}', *result)

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cnt = [0] * 5001
#     for _ in range(N):
#         A, B = map(int, input().split())
#         for i in range(A, B+1):
#             cnt[i] += 1
#     P = int(input())
#     c_list = [int(input()) for _ in range(P)]
#     result = [cnt[k] for k in c_list]
#     print(f'#{tc}', *result)


'''
1
2
1 3
2 5
5
1
2
3
4
5
'''