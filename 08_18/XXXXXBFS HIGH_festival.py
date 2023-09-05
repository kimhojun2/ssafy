# from collections import deque
# import copy
#
# def BFS(a, b):
#     visited = [0]*10000
#     queue = deque()
#     queue.append(a)
#     visited[a] = 1
#     while queue:
#         t = queue.popleft()
#         for r in range(4):
#             if r == 1:
#                 t1 = copy.copy(t)*2
#                 if t1//10 > 4:
#                     t1 = t1/10000
#                     if not visited[r]:
#                         visited[t1] = visited[t] + 1
#                         queue.append(t1)
#                         if t1 == b:
#                             queue.clear()
#                             break
#             elif r == 2:
#                 t2 = copy.copy(t)-1
#                 if t2 == -1:
#                     t2 = 9999
#
#             elif
#
#
#
#     print(visited[d]-1)
#
#
# # N = int(input())
# # for n in range(N):
# #     A = deque(str(input()))
# #     if len(A) < 4:
# #         while len(A) != 4:
# #             A.appendleft(0)
# #     for a in range(len(A)):
# #         b = A.popleft()
# #         A.append(int(b))
def double(num):
    return (num * 2) % 10000


def subtract(num):
    return (num - 1) if num != 0 else 9999


def left_rotate(num):
    return (num % 1000) * 10 + (num // 1000)


def right_rotate(num):
    return (num % 10) * 1000 + (num // 10)


def bfs(start, target):
    visited = set()
    queue = [(start, "")]

    while queue:
        current, actions = queue.pop(0)
        if current == target:
            return actions

        for action, func in [('D', double), ('S', subtract), ('L', left_rotate), ('R', right_rotate)]:
            next_num = func(current)
            if next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, actions + action))

    return ""


# 입력 받기
N = int(input())
for _ in range(N):
    initial, target = map(int, input().split())
    result = bfs(initial, target)
    print(result)