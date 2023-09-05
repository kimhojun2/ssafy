def BFS(G, N, T):
    visited = [0]*(N+1)
    queue = []
    queue.append(1)
    visited[1] = 0
    visited[T] = 1
    while queue:
        t = queue.pop(0)
        for i in range(1, N+1):
            if visited[i] == 0 and arr[t][i] == 1:
                visited[i] = visited[t] + 1
                queue.append(i)
                if i == N:
                    print(visited[i])

    if visited[N] == 0:
        print(-1)



N, M = map(int, input().split())
arr = [[0]*(N+1)for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
T = int(input())

BFS(arr, N, T)


