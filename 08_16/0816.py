# # def f(i, n):
# #     if i == N:
# #         return
# #     else:
# #         B[i] = A[i]
# #         f(i+1, N)
# #         return
# #
# # N = 3
# # A = [1, 2, 3]
# # B = [0] * N
# # f(0,N)
# # print(B)
#
# def f(i,N):
#     if i == N:
#         print(bit, end=' ')
#         s = 0
#         for j in range(N):
#             if bit[j]:
#                 s += A[j]
#                 # print(A[j], end =' ')
#         print(f' : {s}')
#         return
#     else:
#         bit[i] = 1
#         f(i+1, N)
#         bit[i] = 0
#         f(i+1, N)
#         return
#
# A = [1,2,3]
# bit = [0]*3
# f(0,3)
# #
# def f(i, N, s):
#     if i == N:
#         print(bit, end = ' ')
#         print(f' : {s}')
#         return
#
#     else:
#         bit[i] = 1
#         f(i+1, N, s+A[i])
#         bit[i] = 0
#         f(i+1, N, s)
#         return
#
# A = [1,2,3]
# bit = [0]*3
# f(0, 3, 0)
#
# def f(i, N, s, t):
#     global cnt
#     cnt += 1
#     if s == 10:
#         print(bit)
#         return
#
#     elif i == N:
#         return
#
#     elif s > t:
#         return
#
#     else:
#         bit[i] = 1
#         f(i+1, N, s+A[i], t)
#         bit[i] = 0
#         f(i+1, N, s, t)
#         return
# N = 10
# A = [i for i in range(1, N+1)]
# bit = [0]*N
# cnt = 0
# f(0, N, 0, 55)
# print(cnt)
#
def f(i,N):
    if i == N:
        print(A)
    else:
        for j in range(i, N):       # 자신부터 오른쪽끝까지
            A[i], A[j] = A[j], A[i]
            f(i+1, N)
            A[i], A[j] = A[j], A[i]


A = [1,2,3]
f(0,3)

# def f1(b, e):
#     global cnt1
#
#     if b == 0:
#         return 1
#     r = 1
#     for i in range(e):
#         r *= b
#         cnt1 += 1
#     return r
#
#
# def f2(b, e):
#     global cnt2
#
#     if b == 0 or e == 0:
#         return 1
#     if e%2:     #홀수면
#         r = f2(b, (e-1)//2)
#         cnt2 += 1
#         return r*r*b
#     else:       #짝수면
#         r = f2(b, e//2)
#         cnt2 += 1
#         return r*r
# cnt1 = 0
# cnt2 = 0
# print(f1(2,20), cnt1)
# print(f2(2,20), cnt2)