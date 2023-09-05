N = int(input())
adj = [list(map(int, input().split()))for _ in range(N)]


def DFS(now):
    print(now, end = ' ')
    for i in range(N):
        if adj[now][i] == 1:
            DFS(i)

DFS(0)

'''
5
0 1 1 0 0
0 0 0 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
'''