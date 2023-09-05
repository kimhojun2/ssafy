from collections import deque
def BFS(arr, K, X):
    visited = [0]*(N+1)
    queue = deque()
    queue.append(X)
    while queue:
        now = queue.popleft()
        for next in range(1, N+1):
            if arr[now][next] == 1:
                if visited[next] == 0 and visited[now] ==K-1:
                    print(next)
                visited[next] = visited[now] + 1
                queue.append(next)

    if K not in visited:
        print(-1)


# arr =[
#     [0, 0, 1, 0]
#     [0, 0, 1, 0]
#     [1, 1, 0, 1]
#     [0, 0, 1, 0]
# ]
# graph = {
#     0: [2]
#     1: [2]
#     2: [0, 1, 3]
#     3: [2]
# }
# graph = [(2, 0), (2, 1), (2, 3)]


N, M, K, X = map(int, input().split())
graph = {}
for i in range(N):
    
# for m in range(M):
#     x1, x2 = map(int, input().split())
#     arr[x1][x2] = 1

BFS(arr,K,X)
# from collections import defaultdict, deque
#
#
# def BFS(adj_list, K, X):
#     visited = {}
#     queue = deque()
#     queue.append((X, 0))
#
#     while queue:
#         now, steps = queue.popleft()
#
#         if now in visited and visited[now] <= steps:
#             continue
#
#         visited[now] = steps
#
#         if steps == K:
#             print(now)
#
#         if steps > K:
#             break
#
#         for next_node in adj_list[now]:
#             queue.append((next_node, steps + 1))
#
#     if K not in visited.values():
#         print(-1)
#
#
# N, M, K, X = map(int, input().split())
# adj_list = defaultdict(list)
#
# for _ in range(M):
#     x1, x2 = map(int, input().split())
#     adj_list[x1].append(x2)
#
# BFS(adj_list, K, X)
