# 인접 행렬
# 장점 : 구현이 쉽다
# 단점: 메모리 낭비(0도 표시를 하기 때문에)
# graph = [
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 1, 1],
#     [0, 1, 0, 0, 0],
#     [1, 1, 0, 0, 1],
#     [0, 1, 0, 1, 0]
# ]

# if arr[0][1] == 1:
#     갈 수 있다
'''
def dfs(start):
    visited = []
    stack = [start]
    while stack:
        now = stack.pop()
        if now in visited:
            continue
        visited.append(now)

        for next in range(5):
            if graph[now][next] == 0:
                continue
            if next in visited:
                continue
            stack.append(next)
    return visited


print(*dfs(0))
'''


'''
visited = [0]*5
path = []
def dfs(now):
    visited[now] = 1
    print(now, end=" ")
    for next in range(5):
        if graph[now][next] == 0:
            continue
        if visited[next]:
            continue

        dfs(next)
dfs(0)
'''

# 인접리스트
# graph = [
#     [1,3],
#     [0,2,3,4],
#     [0,1,4],
#     [1,3]
# ]
