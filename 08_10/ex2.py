n = int(input())
adj = [list(map(int, input().split()))for _ in range(n)]
visited = [0]*3


def DFS(now, level):
    global visited
    visited[level] = str(now)
    if level == 2:
        print(' '.join(visited))
    for i in range(n):
        if adj[now][i] == 1:
            DFS(i, level+1)


DFS(0, 0)

'''
9
0 1 1 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 1 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0


'''