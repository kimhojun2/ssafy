from collections import deque

def BFS(coco):
    visited = [0]*(N+1)
    que = deque()
    que.append(coco)
    visited[coco] = 1

    while que:
        now = que.popleft()
        for i in range(1, N+1):
            if arr[now][i] == 1 and not visited[i]:
                que.append(i)
                visited[i] = 1

    return visited.count(1)

N = int(input())
M = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
coco = int(input())
result = BFS(coco)
print(result-1)
