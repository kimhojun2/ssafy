'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
import heapq

def prim(start):
    heap = []
    # MST 에 포함되었는 지 여부
    MST = [0] * V

    heapq.heappush(heap, (0,start))
    sum_weight = 0
    while heap:
        weight, v = heapq.heappop(heap)

        if MST[v]:
            continue
        MST[v] = 1

        sum_weight += weight

        for next in range(V):
            if graph[v][next] == 0 or MST[next]:
                continue
            heapq.heappush(heap, (graph[v][next], next))
        print(sum_weight)

    return sum_weight


V, E = map(int, input().split())
#인정행렬
graph = [[0]*V for _ in range(V)]

for _ in range(E):
    f, t, w = map(int, input().split())
    graph[f][t] = w
    graph[t][f] = w     # 무방향 그래프
result = prim(0)
print(result)