N, M = map(int, input().split())
arr = list(sorted(list(map(int, input().split()))))
path = []
visited = [0] * N

def f(level):
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