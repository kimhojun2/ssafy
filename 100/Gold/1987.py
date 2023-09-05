# 알파벳
R, C = map(int, input().split())
arr = [list(input())for _ in range(R)]
def f(C, R, arr):
    stack = []
    alpah = []
    visited = [[1]*C for _ in range(R)]
    visited[0][0] = 1
    alpah.append(arr[0][0])
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    i = 0
    j = 0
    cnt = 0
    mv = 0
    while True:
        for d in range(4):
            ni, nj = i + di[d], j + dj[d]
            if 0 <= ni < R and 0 <= nj < C:
                if arr[ni][nj] not in alpah:
                    visited[ni][nj] += visited[i][j]
                    if visited[ni][nj] >mv:
                        mv = visited[ni][nj]
                    alpah.append(arr[ni][nj])
                    stack.append((i, j))
                    i, j = ni, nj
                    break
        else:
            if stack:
                p = stack.pop()
                i, j = p[0], p[1]
            else:
                break
    for z in visited:
        cnt += z.count(1)

    print(visited)
f(C, R, arr)

# stack = []
# visited = [[0]*C for _ in range(R)]
# for i in range(R):
#     for j in range(C):
#         if not visited:
#             stack.append(arr[i][j])
#             visited[i][j] = 1
#             di = [0,1,0,-1]
#             dj = [1,0,-1,0]
#             for d in range(4):
#                 ni, nj = i + di[d], j + dj[d]
#                 if 0<= ni < R and 0 <= nj < C:
#                     if visited[ni][nj] == 0:
#
#
#
#
# # print(visited)