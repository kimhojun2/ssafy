# import sys
# N, M = map(int, input().split())
# arr = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
#
# for m in range(M):
#     cnt = 0
#     x1,y1,x2,y2 = map(int, sys.stdin.readline().split())
#     for i in range(x1-1, x2):
#         for j in range(y1-1, y2):
#             cnt += arr[i][j]
#     print(cnt)

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) +fib(n-2)


def fibonacci(n):
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 1
    cnt2 = 0
    for i in range(3, n+1):
        cnt2 += 1
        dp[i] = dp[i-1]+dp[i-2]
    return cnt2


n = int(input())
print(fib(n), fibonacci(n))