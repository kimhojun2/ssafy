def backtrack(start, depth):
    if depth == m:
        print(*temp)
        return

    prev = 0
    for i in range(start, n):
         if not visited[i] and arr[i] != prev:
            prev = arr[i]
            temp.append(arr[i])
            # visited[i] = True
            backtrack(i, depth + 1)
            temp.pop()
            # visited[i] = False


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * (n)
temp = []
backtrack(0, 0)