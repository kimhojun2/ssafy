# # def DFS(n, N, adj):
# #     stack = []
# #     visited = [0]*(N+1)
# #     visited[n] = 1
# #     cnt = [n]
# #     print(n)
# #     while True:
# #         for w in range(N, 0, -1):
# #             if adj[n][w] == 1 and visited[w] == 0:
# #                 stack.append(n)
# #                 n = w
# #                 cnt.append(n)
# #                 print(n)
# #                 visited[n] = 1
# #                 break
# #
# #         else:
# #             if stack:
# #                 n = stack.pop()
# #             else:
# #                 break
# #     return cnt
# #
# # N, M, R = map(int, input().split())
# # arr = [list(map(int, input().split()))for _ in range(M)]
# # adj = [[0]*(N+1) for _ in range(N+1)]
# # for i in range(M):
# #     v1, v2 = arr[i][0], arr[i][1]
# #     adj[v1][v2] = 1
# #     adj[v2][v1] = 1
# #
# # DFS(R, N, adj)
import sys
from collections import deque
def DFS(n, N, adj):
    stack = deque()
    visited = [0]*(N+1)
    visited[n] = 1
    cnt = [n]
    while True:
        found_next = False
        for w in range(N, 0, -1):
            if adj[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                cnt.append(n)
                visited[n] = 1
                found_next = True
                break

        if not found_next:
            if stack:
                n = stack.pop()
            else:
                break
    # 도착하지 못하는 정점을 0으로 표시
    for i in range(1, N+1):
        if visited[i] == 0:
            cnt.append(0)
    return cnt

N, M, R = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split()))for _ in range(M)]
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    v1, v2 = arr[i][0], arr[i][1]
    adj[v1][v2] = 1
    adj[v2][v1] = 1

result = DFS(R, N, adj)
for z in range(len(result)):
    print(result[z])

import sys
# from collections import deque

# N, M, R = map(int, sys.stdin.readline().split())
# adj = [[] for _ in range(N+1)]
# for _ in range(M):
#     src, dst = map(int, sys.stdin.readline().split())
#     adj[src].append(dst)
#     adj[dst].append(src)
# for x in range(1, N+1):
#     adj[x] = sorted(adj[x])
#
# visited = [0] * (N+1)
# nodes_cnt = [0] * (N+1)
# order = 1  # 방문순서 체크 변수
# stack = deque()
# stack.append(R)
#
#
# while stack:
#     cur_node = stack.pop()
#     visited[cur_node] = 1
#     if nodes_cnt[cur_node] == 0:
#         nodes_cnt[cur_node] = order
#         order += 1
#
#     for next_node in adj[cur_node]:
#         if visited[next_node] == 0:
#             stack.append(next_node)
#
# for i in range(1, len(nodes_cnt)):
#     print(nodes_cnt[i])