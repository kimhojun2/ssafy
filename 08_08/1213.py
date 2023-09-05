def BruteForce(p, t):
    i = 0
    cnt = 0
    k = 0

    while k < N - M :
        while j < M and i < N:
            if t[i] != p[j]:
                i = i-j
                j = -1
            i = i+1
            j = j+1
        if j == M:
            cnt +=1
            k +=i
            j = 0
        else:
            break
    return cnt


for tc in range(10):
    T = int(input())
    p = input()
    t = input()
    # print(p)
    # print(t)
    M = len(p)
    N = len(t)

    print(f'#{T} {BruteForce(p, t)}')




#
# def BruteForce(p, t):
#     i = 0
#     cnt = 0
#     j = 0
#
#     while j < M and i < N:
#         if t[i] != p[j]:
#             i = i - j
#             j = -1
#         i = i + 1
#         j = j + 1
#
#         if j == M:
#             cnt += 1
#             j = 0
#
#     return cnt
#
#
# for tc in range(10):
#     T = int(input())
#     p = input()
#     t = input()
#     # print(p)
#     # print(t)
#     M = len(p)
#     N = len(t)
#
#     print(f'#{T} {BruteForce(p, t)}')
#
#
#
