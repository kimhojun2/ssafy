# A, B = map(str, input(). split())
#
# cnt = 0
# if B.find(A) != -1:
#     cnt = 0
#
# elif len(A) == len(B):
#     for i in range(0, len(B)):
#         if A[i] != B[i]:
#             cnt += 1
#
# else:
#     cnt_1 = 0
#
#     for j in range(1, len(A)+1):
#         result = B.find(A[(len(A)-j):len(A)])
#         if result != -1:
#             cnt_1 = (len(A)-j)
#
#     cnt_2 = 0
#
#     for l in range(1, len(A)):
#         result = B.find(A[0:l])
#         if result != -1:
#             cnt_2 = l
#     cnt = max(cnt_1,cnt_2)
#
#
# print(cnt)


A, B = map(str,input().split())
cnt = 0

def doubleuse():
    num = []
    for i in range(len(B)-len(A)+1):
        cnt = 0
        for j in range(len(A)):
            if A[j] != B[i+j]:
                cnt += 1
        num.append(cnt)
    num.sort()
    return num[0]

print(doubleuse())