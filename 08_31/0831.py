'''
조합
- 서로 다른 n개의 원소 중 r개를 순서 없이 골라낸 것을 조합이라고 한다.
'''
# def ncr(n,r):
#     if r == 0:
#         print(tr)
#     elif n < r:
#         return
#     else:
#         tr[r-1] = a[n-1] #a[n-1] 조합에 포함시키는 경우
#         ncr(n-1, r-1)
#         ncr(n-1, r)     #a[n-1] 조합에 포함시키지 않는 경우
#
# N = 5
# R = 3
# a = [1,2,3,4,5]
# tr = [0]*R
# ncr(N,R)

# def ncr(n, r, s):
#     if r == 0:
#         print(*comb)
#     else:
#         for i in range(s, n-r+1):
#             comb[r-1] = A[i]
#             ncr(n,r-1,i+1)
#
# A = [1,2,3,4,5,6]
# N = len(A)
# R = 2
# comb = [0]*R
# ncr(N,R,0)


# def subset(i, N):
#     if i == N:
#         s = 0
#         for j in range(N):
#             if bit[j]:
#                 s += arr[j]
#         if s == 0 :
#             for j in range(N):
#                 if bit[j]:
#                     print(arr[j], end = ' ')
#             print()
#
#     else:
#         bit[i] = 1
#         subset(i+1, N)
#         bit[i] = 0
#         subset(i+1, N)
#     return
#
#
# arr = [-1,3,-9,6,7,-6,1,5,4,-2]
# N = len(arr)
# bit = [0]*N
# subset(0,N)

N = 10
a = [1,4,1,6,6,10,5,7,3,8,5,9,3,5,8,11,2,13,12,14]

meet = []
for i in range(N):
    meet.append([a[i*2], a[i*2+1]])
print(meet)
meet.sort(key=lambda x:x[1])
print(meet)