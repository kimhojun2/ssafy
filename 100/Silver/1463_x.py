# N = int(input())
#
# cnt = 0
# while N != 1:
#     if N % 3 == 0:
#         N /= 3
#         cnt += 1
#     elif N % 2 == 0:
#         if N % 3 == 1:
#             N -= 1
#             cnt += 1
#         else:
#             N /= 2
#             cnt += 1
#     else:
#         N -= 1
#         cnt += 1
# print(cnt)
#
#

N = int(input())

arr = [0] * (N + 1)

for i in range(2, N + 1):
    arr[i] = arr[i - 1] + 1

    if i % 2 == 0:
        arr[i] = min(arr[i], arr[i // 2] + 1)

    if i % 3 == 0:
        arr[i] = min(arr[i], arr[i // 3] + 1)

print(arr[N])

# dp 다이나믹 프로그래밍 알고리즘 사용필요