'''
RKFCBICM
0 1 1 1 0 0 0 0
0 0 0 0 1 1 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
'''
# 그래프의 기본 구성 요소 :  노드, 간선
# 인접행렬
lst = list(input())
N = len(lst)
adj = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)] # 방문 여부를 지정하는 리스트
def DFS(v):
    print(lst[v], end='')
    visited[v] = True

    for i in range(N):
        if adj[v][i] and not visited[i]:
            DFS(i)


DFS(0)