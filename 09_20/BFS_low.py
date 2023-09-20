from collections import deque

def BFS(start):
    visited = [0]*(N+1)
    que = deque()
    que.append(start)

    while que:
        now = que.popleft()
        if now in gk:
            for i in graph[now]:
                if not visited[i[0]]:
                    que.append(i[0])
                    if visited[now] + i[1] <= K:
                        visited[i[0]] = visited[now] + i[1]
    return visited



N, M, K = map(int, input().split())
graph = {}
gk = graph.keys()
for a in range(M):
    n, m, k = map(int, input().split())
    if n in gk:
        graph[n].append([m,k])
    else:
        graph[n] = [[m,k]]

result = BFS(0)
for r in range(len(result)):
    if result[r] :
        print(r, end=' ')


