N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
K = int(input())
di = [1, 1, -1, -1]
dj = [-1, 1, 1, -1]

max_monster = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            for p in range(1, K+1):
                ni, nj = i + di[k]*p, j + dj[k]*p
                if 0 <= ni < N and 0 <= nj < N:
                    cnt += arr[ni][nj]

        if max_monster < cnt:
            max_monster = cnt
print(f'{max_monster}')