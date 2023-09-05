import copy
N,M = map(int, input().split())
lst = list(map(int, input().split()))
path = []
visited = [0] * N
Min = 21e8
result = []

def DFS(level, Sum):
    global Min, path, result
    if level == M:      # 패를 모두 선택했다면
        if Sum < Min:   # 현재 곱한 값이 최소값 보다 작으면 최소값 업데이트
            Min = Sum
            result = copy.deepcopy(path)
        return

    for i in range(N):
        if visited[i] == 1:     # 사용된 패는 건너뜀
            continue
        path.append(lst[i])
        visited[i] = 1
        DFS(level + 1, Sum * lst[i])    # 다음 패르 ㄹ선택으로 넘어가며 재귀호출
        visited[i] = 0      #복구 (백트래킹)
        path.pop()

DFS(0,1) # 초기레벨은 0 초기곱은 1
result.sort()
print(*result)

