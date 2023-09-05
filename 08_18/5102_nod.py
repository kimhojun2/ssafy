def BFS(G, s, E):
    visited = [0]*(V+1)
    queue = []
    queue.append(s)
    visited[s] = 1

    while queue:
        t = queue.pop(0)
        for i in range(V+1):
            if not visited[i] and arr[t][i] == 1:
                visited[i] = visited[t] + 1
                queue.append(i)
                if i == E:
                    queue.clear()
                    break
    if visited[E] == 0:
        return 0

    return visited[E]-1


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0]*(V+1)for _ in range(V+1)]
    for e in range(E):
        y, x = map(int, input().split())
        arr[y][x] = 1
        arr[x][y] = 1

    S, E = map(int, input().split())
    result = BFS(arr, S, E)
    print(f'#{tc} {result}')

