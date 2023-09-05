def BFS(G, N, s, cnt):
    visited = [0]*(N+1)
    queue = []
    SUM = 0
    queue.append(s)
    visited[s] = 0
    while queue:
        t = queue.pop(0)
        for i in range(1, N+1):
            if not visited[i] and arr[t][i] == 1:
                visited[i] = visited[t] + 1
                queue.append(i)
                if visited[i] <= cnt:
                    SUM += 1

    print(SUM)


N, M = map(int, input().split())
arr = [[0]*(N+1)for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

s, cnt = map(int, input().split())

BFS(arr, N, s, cnt)