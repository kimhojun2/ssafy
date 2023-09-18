from collections import deque
def BFS(A,B,N,M):
    visited = [0]*100001
    queue = deque()
    queue.append(N)
    while queue:
        now = queue.popleft()
        D = [now+1, now-1, now+A, now-A, now+B, now-B, now*A, now*B]
        if now == M:
            print(visited[M])
            break
        for d in D:
            if 0<= d < 100001 and visited[d] == 0:
                visited[d] = visited[now] + 1
                queue.append(d)

A, B, N, M = map(int, input().split())
BFS(A,B,N,M)