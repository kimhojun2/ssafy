N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]


def dfs(u):
    global cnt
    stack = []
    stack.append(u)
    while stack:
        now = stack.pop()
        visited[now] = True
        for next in range(1, N + 1):
            if graph[now][next] and not visited[next]:
                stack.append(next)
    cnt += 1
    for i in range(1,N + 1):
        if visited[i] == False:
            next_num = i
            dfs(next_num)
    return cnt


cnt = 0
visited = [False] * (N + 1)
for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
print(dfs(1))