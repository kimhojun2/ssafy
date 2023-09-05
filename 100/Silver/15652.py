# N, M = map(int,input().split())
# arr = [i for i in range(1,N+1)]
# path = []
# visited = [0] * N
# def f(level, start):
#     global path, result
#     if level == M:
#         print(*path)
#         return
#
#     for i in range(start, N):
#         if visited[i] == 1:
#             continue
#         path.append(arr[i])
#         visited[i] = 1
#         f(level + 1, i)
#         visited[i] = 0
#         path.pop()
#
# f(0, 0)
N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
path = []
visited = [0] * N

def f(level, start):
    if level == M:
        print(*path)
        return

    for i in range(start, N):
        if visited[i] == 1:
            continue
        path.append(arr[i])
        visited[i] = 1
        f(level + 1, i)  # 다음 숫자부터 선택하도록 start 값을 유지
        visited[i] = 0
        path.pop()

f(0, 0)
