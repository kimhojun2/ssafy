# # def BFS(arr, v, vv):
# #     visited = [[0]*(N+1)for _ in range(N+1)]
# #     queue = []
# #     queue.append([v, vv, 0])
# #     visited[v][vv] = 1
# #     while queue:
# #         dir = queue.pop(0)
# #         x, y, cnt= dir[0], dir[1], dir[2]
# #         for z in range(4):
# #             ny, nx = x + di[z], y + dj[z]
# #             if 0 <= ny <N and 0 <= nx <N:
# #                 cnt +=1
# #                 if arr[ny][nx] == '3':
# #                     return cnt
# #                 elif not visited[ny][nx] and arr[ny][nx] == '0':
# #                     visited[ny][nx] = 1
# #                     queue.append([ny, nx, cnt +1])
# #                 else:
# #                     cnt -=1
# #     return 0
# #
# #
# # T = int(input())
# # for tc in range(1, T+1):
# #     N = int(input())
# #     arr = [list(input())for _ in range(N)]
# #     di = [0,1,0,-1]
# #     dj = [1,0,-1,0]
# #     a = 0
# #     b = 0
# #     for i in range(N):
# #         for j in range(N):
# #             if arr[i][j] == '2':
# #                 a = i
# #                 b = j
# #                 break
# #
# #     result = BFS(arr, a, b)
# #
# #     print(f'#{tc} {result}')
#
# def BFS(arr, v, vv):
#     visited = [[0] * (N + 1) for _ in range(N + 1)]
#     queue = []
#     queue.append([v, vv, 0])
#     visited[v][vv] = 1
#
#     while queue:
#         dir = queue.pop(0)
#         x, y, cnt = dir[0], dir[1], dir[2]
#
#         for z in range(4):
#             ny, nx = x + di[z], y + dj[z]
#             if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
#                 if arr[ny][nx] == '3':
#                     return cnt
#                 elif arr[ny][nx] == '0':
#                     visited[ny][nx] = 1
#                     queue.append([ny, nx, cnt + 1])
#
#     return 0
#
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N)]
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     a = 0
#     b = 0
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '2':
#                 a = i
#                 b = j
#                 break
#
#     result = BFS(arr, a, b)
#
#     print(f'#{tc} {result}')

# 강사님 코드
'''
def bfs(y,x):
    queue = []
    queue.append((y,x))
    visited[y][x] = 1
    while queue:
        cy, cx = queue.pop(0)
        if arr[cy][cx] =='3'
            return visited[cy][cx] - 2
        for dy, dx in direction:
            ny = cy + dy
            nx = cx + dx
            if 0<=ny<N and 0<=nx<N:
                if arr[ny][nx] != '1':
                    visited[ny][nx] = visited[cy][cx] + 1
                    queue.append((ny, nx))
    return 0
'''