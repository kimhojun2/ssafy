# '''
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
# '''
#
# V = int(input())
# E = int(input())
# adj = [[0]*(V+1)for _ in range(V+1)]
#
# for i in range(E):
#     a, b = map(int, input().split())
#     adj[a][b] = 1
#
# def DFS(n, V, adj):
#     cnt = 0
#     stack = []
#     visited = [0] * (V+1)
#     visited[n] = 1
#
#
#     while True:
#         for w in range(1, V):
#             if adj[n][w] == 1 and visited[w] == 0:
#                 stack.append(n)
#                 n = w
#                 cnt +=1
#
#
#                 visited[n] = 1
#                 break
#
#         else:
#             if stack:
#                 n = stack.pop()
#             else:
#                 break
#
#     return cnt
#
# print(DFS(1,V,adj))



N = int(input())
M = int(input())
arr = [[0]*N for _ in range(N)]
visited = [0] * N
for _ in range(M):
    c1, c2 = map(int, input().split())
    arr[c1-1][c2-1] = arr[c2-1][c1-1] = 1

def DFS(v):
    visited[v] = 1
    for i in range(N):
        if arr[v][i] == 1 and not visited[i]:
            DFS(i)

DFS(0)
print(sum(visited)-1)