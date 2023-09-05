from collections import deque

def BFS(s,N):
    visited = [0]*(N+1)
    queue = deque()
    queue.append(s)
    while queue:
        now = queue.popleft()
        for next in range(1,N+1):
            if arr[now][next] == 1:
                if next != s:
                    if visited[next] != 0:
                        if visited[next] > visited[now] + 1:
                            visited[next] = visited[now] + 1
                            queue.append(next)
                    else:
                        visited[next] = visited[now] + 1
                        queue.append(next)
    return max(visited)


N = int(input())
arr = [[0]*(N+1) for _ in range(N+1)]
a,b = 0, 0
while a != -1 and b != -1:
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1


max_score = 10e5
lst = []
for start in range(1,N+1):
    result = BFS(start, N)
    if max_score > result:
        max_score = result
        lst.clear()
    if result == max_score:
        lst.append(start)
lst.sort()
print(max_score, len(lst))
print(*lst)