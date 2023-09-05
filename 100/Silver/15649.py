N, M = map(int,input().split())
arr = [i for i in range(1,N+1)]
path = []
visited = [0] * N
def f(level):
    global path, result
    if level == M:
        print(*path)
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        path.append(arr[i])
        visited[i] = 1
        f(level + 1)
        visited[i] = 0
        path.pop()

f(0)
