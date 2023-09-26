def find(level, s):
    global score
    if level == (N):    # 마지막 행까지 탐색을 완료 했다면
        if score < s:   # 지금까지 결과보다 크다면 값 바꿔주기
            score = s
        return

    for i in range(N):
        if not visited[i]:      # 내가 선택하지 않은 열이라면 선택
            visited[i] = 1
            find(level+1, s + arr[level][i])    # 재귀 호출
            visited[i] = 0      # 방문처리 풀어주기


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    visited = [0]*N
    score = 0
    find(0, 0)
    print(f'#{tc} {score}')