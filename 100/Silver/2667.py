def BFS(G, i, j):
    visited = [[0]*N for _ in range(N)]
    queue = []
    queue.append([i, j])
    visited[i][j] = 1
    arr[i][j] = '4'
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    SUM = 1
    while queue:
        t = queue.pop(0)
        v = t[0]
        vv = t[1]
        for d in range(4):
            nv, nvv = v + di[d], vv + dj[d]
            if 0<= nv <N and 0<= nvv <N:
                if not visited[nv][nvv] and arr[nv][nvv] == '1':
                    visited[nv][nvv] = 1
                    arr[nv][nvv] = '4'
                    queue.append([nv, nvv])
                    SUM +=1

    return SUM


N = int(input())
arr = [list(input())for _ in range(N)]

cnt = 0
lst = []
for y in range(N):
    for x in range(N):
        if arr[y][x] == '1':
            a = BFS(arr, y, x)
            lst.append(a)
            cnt += 1
lst.sort()
print(cnt)
for a in lst:
    print(a)

'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''