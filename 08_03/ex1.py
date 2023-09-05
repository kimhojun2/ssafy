N, M =map(int, input().split())
K = int(input())

arr = [list(input()) for _ in range(N)]

# print(arr)

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# N = int(input())
# arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == "@":
            for k in range(4):
                for p in range(K+1):
                    ni, nj = i+di[k]*p, j+dj[k]*p
                    if 0 <=ni<N and 0<=nj<M:
                        if arr[ni][nj] == "#":
                            break
                        else:
                            arr[ni][nj] = "%"
for row in arr:
    print(*row, sep='')


#
# '''
# 3 5
# 2
# _#_#@
# _#_#@
# @___#
#
# '''


# N, M =map(int, input().split())
# K = int(input())
# arr = [list(input()) for _ in range(N)]
#
# directions = [(0,1), (0,-1), (-1,0), (1,0)]
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == '@':
#             for dy, dx in directions:
#                 for k in range(1, K+1):
#                     ny, nx = i +(k*dy), j + (k*dx)
#                     if 0<= ny<N and 0<=nx<M:
#                         if arr[ny][nx] == '_':
#                             arr[ny][nx] = '%'
#                         if arr[ny][nx] == '#':
#                             break
#
#             arr[i][j] = '%'
# for row in arr:
#     print(*row, sep='')