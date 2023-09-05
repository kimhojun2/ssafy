# def fibonacci(n):
#     dp = [0]*(n+1)
#     dp[1], dp[2] = 1, 1
#     cnt2 = 0
#     for i in range(3, n+1):
#         cnt2 += 1
#         dp[i] = dp[i-1]+dp[i-2]
#     return cnt2


# n = int(input())
# print(fib(n), fibonacci(n))

N = int(input())
dp = [0]*20
arr = [list(map(int, input().split()))for _ in range(N)]
for n in range(N):
    