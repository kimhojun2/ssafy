# N =int(input())
# dp = [0]*(N+1)
# dp[1] = 1
# dp[2] = 0
# dp[3] = 1
# dp[4] = 1
# for i in range(5, N+1):
#     if dp[i-4:i].count(1) !=4 :
#         dp[i] = 1
#     else:
#         dp[i] = 0
#
# if dp[N] == 1:
#     print('SK')
# else:
#     print('CY')
N = int(input())

# dp[i]는 돌이 i개 남았을 때 이기는 사람 // True면 상근 승, False면 창영 승
dp = [False] * (N + 1)

for i in [1, 3, 4]:
    if i <= N:
        dp[i] = True

for i in range(5, N + 1):
    dp[i] = not (dp[i-1] and dp[i-3] and dp[i-4])

print("SK" if dp[N] else "CY")