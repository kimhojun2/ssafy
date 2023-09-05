#
# #
# #
# #
# #
# # V, E =map(int, input().split())
# # arr = list(map(int, input().split()))
# # adj_m = [[0]*(V+1) for _ in range(V+1)]
# # for i in range(E):
# #     v1, v2 = arr[i*2], arr[i*2+1]
# #     adj_m[v1][v2] = 1
# #     adj_m[v2][v1] = 1
#
#
# def DFS(n, g, V, adj_m):
#     stack = []                      # stack 생성
#     visited = [0] * (V+1)           # visited 생성
#     visited[n] = 1                  # 시작점 방문
#     result = 1
#     while True:
#         for w in range(1, V):
#             if n == g:
#                 result = 1
#
#             elif adj_m[n][w] == 1 and visited[w] == 0:
#                 stack.append(n) # push(v)
#                 n = w
#                 visited[n] = 1  # w 방문 표시
#                 break
#
#             else:
#                 if stack: # 스택에 지나온 정점이 남아있으면
#                     n = stack.pop() # pop()해서 다시 다른 w 찾기
#                 else:   # 스택이 비어있으면
#                     result = 0
#                     break # while True 탐색 끝끝
#         return result
#
#
# T = int(input())
# for tc in range(1, T+1):
#     V, E = map(int, input().split())
#     S, G = map(int, input().split())
#     adj_m = [[0] * (V + 1) for _ in range(V + 1)]
#
#     for i in range(E):
#         v1, v2 = map(int, input().split())
#         adj_m[v1][v2] = 1
#
#     way = DFS(S, G, V, adj_m)
#
#     print(f'#{tc} {way}')

def dfs(now, visited):
    visited[now] = True

    for next in graph[now]:
        if not visited[next]:
            dfs(next, visited)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[0] for _ in range(V+1)]
    visited = [False] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
    S, E = map(int, input().split())
    dfs(S, visited)
    print(f'#{tc} 1' if visited[E] else f'#{tc} 0')

