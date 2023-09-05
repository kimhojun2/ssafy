from collections import deque
def BFS(N,M,y,x,T):
    visited = [[0]*M for _ in range(N)]
    queue = deque()
    queue.append((y,x,0,False))
    gram = False
    key = 0
    while queue:
        i, j, t, g = queue.popleft()
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0<= ni <N and 0<= nj <M:
                if not g:
                    if arr[ni][nj] == 0:
                        if visited[ni][nj] == 0:
                            visited[ni][nj] = visited[i][j] + 1
                            nt = t + 1
                            queue.append((ni,nj,nt,False))
                        else:
                            if visited[ni][nj] > visited[i][j] + 1:
                                visited[ni][nj] = visited[i][j] + 1
                                nt = t + 1
                                queue.append((ni, nj, nt, False))


                    if arr[ni][nj] == 2:
                        gram = True
                        if visited[ni][nj] == 0:
                            visited[ni][nj] = visited[i][j] + 1
                            nt = t + 1
                            queue.append((ni,nj,nt,True))
                            key = visited[ni][nj] + (N - 1 - ni) + (M - 1 - nj)
                        else:
                            if visited[ni][nj] > visited[i][j] + 1:
                                visited[ni][nj] = visited[i][j] + 1
                                nt = t + 1
                                queue.append((ni, nj, nt, True))
                            if key > visited[ni][nj] + (N - ni) + (M - nj):
                                key = visited[ni][nj] + (N - ni) + (M - nj)

                elif g:
                    if arr[ni][nj] == 0:
                        if visited[ni][nj] == 0:
                            visited[ni][nj] = visited[i][j] + 1
                            nt = t + 1
                            queue.append((ni,nj,nt,True))
                        else:
                            if visited[ni][nj] > visited[i][j] + 1:
                                visited[ni][nj] = visited[i][j] + 1
                                nt = t + 1
                                queue.append((ni, nj, nt, True))
                    if arr[ni][nj] == 1:
                        if visited[ni][nj] == 0:
                            visited[ni][nj] = visited[i][j] + 1
                            nt = t + 1
                            queue.append((ni, nj, nt, True))
                        else:
                            if visited[ni][nj] > visited[i][j] + 1:
                                visited[ni][nj] = visited[i][j] + 1
                                nt = t + 1
                                queue.append((ni, nj, nt, True))

    # print(gram)
    # print(key)
    # print(visited[N-1][M-1])
    if not visited[N-1][M-1] and not gram:
        return 'Fail'
    elif visited[N-1][M-1] and gram:
        if min(visited[N-1][M-1], key) > T:
            return 'Fail'
        else:
            return min(visited[N-1][M-1], key)
    elif visited[N-1][M-1] and not gram:
        if visited[N-1][M-1] > T:
            return 'Fail'
        else:
            return visited[N-1][M-1]
    else:
        if key > T:
            return 'Fail'
        else:
            return key


N,M,T = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
di = [0,1,0,-1]
dj = [1,0,-1,0]
result = BFS(N,M,0,0,T)
print(result)
