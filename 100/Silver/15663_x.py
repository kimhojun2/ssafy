# N, M = map(int, input().split())
# arr = list(sorted(list(map(int, input().split()))))
# path = []
# visited = [0] * N
# lst = []
#
# def f(level):
#     if level == M:
#         print(lst)
#         if path not in lst:
#             lst.append(path)
#             print(*path)
#         return
#
#     for i in range(N):
#         if visited[i] == 1:
#             continue
#         path.append(arr[i])
#         visited[i] = 1
#         f(level + 1)
#         visited[i] = 0
#         path.pop()
#
# f(0)
N, M = map(int, input().split())
arr = list(sorted(list(map(int, input().split()))))
path = []
visited = [0] * N
lst = []

def f(level):
    if level == M:
        if path not in lst:
            lst.append(path.copy())
            print(*path)
        return

    for i in range(N):
        if visited[i] == 1:
            continue
        path.append(arr[i])
        visited[i] = 1
        f(level + 1)
        visited[i] = 0
        path.pop()

f(0)
