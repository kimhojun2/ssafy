# from collections import deque
# def BFS(arr,s, N):
#     visited = [0]*(N+1)
#     queue = deque()
#     queue.append(s)
#     while queue:
#         now = queue.popleft()
#         for next in range(1, N+1):
#             if arr[now][next] == 1:
#                 if visited[next] == 0 and next != 1:
#                     visited[next] = visited[now] + 1
#                     queue.append(next)
#
#     print(visited.index(max(visited)), max(visited), visited.count(max(visited)))
#
#
# N, M = map(int, input().split())
# arr = [[0]*(N+1)for _ in range(N+1)]
# for m in range(M):
#     a, b = map(int, input().split())
#     arr[a][b] = 1
#     arr[b][a] = 1
# BFS(arr,1,N)
from collections import deque
def BFS(arr,s, N):
    visited = [0]*(N+1)
    queue = deque()
    queue.append(s)
    while queue:
        now = queue.popleft()
        for next in arr[now]:
            if visited[next] == 0 and next != 1:
                visited[next] = visited[now] + 1
                queue.append(next)

    print(visited.index(max(visited)), max(visited), visited.count(max(visited)))


N, M = map(int, input().split())
arr = [[]for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
BFS(arr,1,N)