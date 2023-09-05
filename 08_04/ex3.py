# di = 1
# dj = 1
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split()))for _ in range(N)]
#     lst = []
#     for i in range(N):
#         for j in range(N):
#             for l in range(N):
#                 ni = i +di*l
#                 nj = j +dj*l
#
#                 if 0<=ni<N and 0<=nj<N:
#                     # print(ni, nj)
#                     if arr[i][j] == arr[ni][j]:
#                         lst.append(l+1)
#                     elif arr[i][j] == arr[i][nj]:
#                         lst.append(l+1)
#                     elif arr[i][j] == arr[ni][nj]:
#                         lst.append(2*(l+1))
#
#     print(lst.count(max(lst)))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input().split()))for _ in range(N)]

    maxarea = 0
    cnt = 0

    for y in range(N):
        for x in range(N):
            cur = MAP[y][x]
            for ny in range(y, N):
                for nx in range(x, N):
                    if MAP[ny][nx] ==cur:
                        area = (ny-y+1)*(nx-x+1)
                        if area > maxarea:
                            maxarea = area
                            cnt = 1
                        elif area == maxarea:
                            cnt +=1
    print(f'#{tc} {cnt}')