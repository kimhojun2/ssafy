N, M = map(int, input().split())
arr = list(sorted(list(map(int, input().split()))))
path = []
visited = [0] * N

def f(level, start):
    if level == M:
        print(*path)
        return

    for i in range(start, N):
        if visited[i] == 1:
            continue
        path.append(arr[i])
        visited[i] = 1
        f(level + 1, i+1)
        visited[i] = 0
        path.pop()

f(0, 0)