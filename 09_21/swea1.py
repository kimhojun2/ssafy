# 해당 노드의 최상위 부모를 찾는 함수(부모 노드를 찾는 함수)
n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
parent = [i for i in range(n)]


def Find(node):
    if node == parent[node]:    # 현재 노드가 자신의 대표 노드인 경우
        return node     # 해당 노드를 반환

    parent[node] =Find(parent[node])    # 현재 노드가 대표 노드가 아닌경우, 재귀적으로 부모 노드 탐색
    return parent[node] # 최상위 부모 노드 반환

# 두 노드를 연결하는 함수
def Union(a, b):
    pa = Find(a)
    pb = Find(b)
    if pa != pb:    # 두 노드의 루트가 다르다면
        parent[pb] = pa # b의 루트를 a의 루트로 변경

for i in range(n):
    for j in range(i+1, n):
        # 두 노드(i,j)가 연결되어 있지 않으면 continue
        if arr[i][j] == 0:
            continue
        # 만약 두 노드의 최상위 부모(루트)가 같다면
        if Find(i) == Find(j):
            print('WARNING')
            exit()

        # 두 노드 연결
        Union(i, j)
        print(1)
print("STABLE")