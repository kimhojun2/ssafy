def ddd(N,miro):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    a = 0
    b = 0
    for i in range(N):
        for j in range(N):
            if miro[i][j] == '3':
                a, b = i, j
                break
        if miro[i][j] == '3':
            break

    stack = []
    result = 1
    while miro[a][b] != '2':
        for k in range(4):
            na, nb = a + di[k], b + dj[k]
            if 0 <= na < N and 0 <= nb < N:
                if miro[na][nb] == '0':
                    stack.append([a, b])
                    a, b = na, nb
                    miro[a][b] = '1'
                    break
                elif miro[na][nb] == '2':
                    a, b = na, nb
                    break


        else:
            if miro[a][b] == '2':
                break
            elif len(stack) != 0:
                A = stack.pop()
                a, b = A[0], A[1]
            else:
                result = 0
                break
    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(str, input()))for _ in range(N)]
    way = ddd(N,miro)
    print(f'#{tc} {way}')


#강사님코드
# def maze():
#     while stack:
#         y, x = stack.pop()
#         arr[y][x] = -1
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= nx < N and 0 <= ny < N:
#                 if arr[nx][ny] == 3:
#                     return 1
#                 elif arr[nx][ny] == 0:
#                     stack.append((nx, ny))
#     return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split()))for _ in range(N)]
#     dy = [0, 1, 0, -1]
#     dx = [1, 0, -1, 0]
#     for y in range(N):
#         for x in range(N):
#             if arr[y][x] == 2:
#                 stack = [(y, x)]
#                 break
#     print(f'#{tc} {maze()}')