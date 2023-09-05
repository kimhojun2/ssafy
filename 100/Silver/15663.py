# N, M = map(int, input().split())
# arr = list(sorted(list(map(int, input().split()))))
# path = []
# visited = [0] * N
# lst = []
#
# def f(level):
#     if level == M:
#         if path not in lst:
#             lst.append(path.copy())
#             print(*path)
#         return
#     r = 0
#     for i in range(N):
#         if visited[i] == 1 and arr[i] == r:
#             continue
#         r = arr[i]
#         path.append(arr[i])
#         visited[i] = 1
#         f(level + 1)
#         visited[i] = 0
#         path.pop()

# f(0)
def backtrack(depth):
    if depth == m:
        print(*temp)
        return

    prev = 0
    for i in range(n):
         if not visited[i] and arr[i] != prev:
            prev = arr[i]
            temp.append(arr[i])
            visited[i] = True
            backtrack(depth + 1)
            temp.pop()
            visited[i] = False


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visited = [False] * (n)
temp = []
backtrack(0)