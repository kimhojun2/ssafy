# # # def fibo2(n):
# # #     f = [0] * (n+1)
# # #     f[0] = 0
# # #     f[1] = 1
# # #     for i in range(2, n + 1):
# # #         f[i] = f[i-1] + f[i-2]
# # #
# # #     return f[n]
# # #
# # # cnt = 0
# # # def fibo(n):
# # #     global cnt
# # #     cnt+=1
# # #     if n < 2:
# # #         return n
# # #     else:
# # #         return fibo(n-1) + fibo(n-2)
# # #
# # # print(fibo(30), cnt)
# #
# # def fibo(n):
# #     global cnt
# #     # global memo ------> 배열은 글로벌 선언 안해도 된다
# #     cnt +=1
# #     if n <2:
# #         return memo[n]
# #     else:
# #         if memo[n] ==0:
# #             memo[n] = fibo(n-1) + fibo(n-2)
# #         return memo[n]
# # cnt = 0
# # N = 30
# # memo = [0]*(N+1)
# # memo[0] = 0
# # memo[1] = 1
# # print(fibo(N), cnt)
#
#
# def fibo(n):
#     dp = [0]*(n+1)
#     dp[0] = 0
#     dp[1] = 1
#     for i in range(2, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
#     return dp[n]
#
# print(fibo(100))

'''
DPS 예시
1. 초기상태 : 배열 visted를 False로 초기화하고, 공백 스택을 생성
2. 정점 A를 시작으로 깊이 우선 탐색을 시작
    visited[A] <-- True
3. 정점 A에 방문하지 않은 정점 B,C가 있으므로 A를 스택에 push하고, 인접정점 B와 C중에서
    오름차순에 따라 B를 선택하여 탐색으로 계속한다
    stack[0] = A, visited[B] <-- True
4. 정점에서 방문하지 않은 인접 정점이 없으면, 마지막 정점으로 돌아가기 위해 stack에서 poop
    하여 받은 정점으로 이동하여 다시 탐색
5. stack이 공백이 되면 깊이 우선 탐색을 종료

저장방식 중요
'''
def DFS(n, V, adj_m):
    stack = []                      # stack 생성
    visited = [0] * (V+1)           # visited 생성
    visited[n] = 1                  # 시작점 방문
    print(n)                        # do[n]
    while True:
        for w in range(1, V):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n) # push(v)
                n = w
                print(n)        # do(w)
                visited[n] = 1  # w 방문 표시
                break

        else:
            if stack: # 스택에 지나온 정점이 남아있으면
                n = stack.pop() # pop()해서 다시 다른 w 찾기
            else:   # 스택이 비어있으면
                break # while True 탐색 끝끝




V, E =map(int, input().split())
arr = list(map(int, input().split()))
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1
